import requests
from bs4 import BeautifulSoup

def get_page_links(base_url):
    # Get the initial page content
    response = requests.get(base_url)
    soup = BeautifulSoup(response.text, 'lxml')
    
    # Find all pagination links
    pages = soup.find('nav', class_='pagination')
    urls = [base_url]  # Start with the first page URL
    
    if pages:
        links = pages.find_all('a')
        for link in links:
            num = link.text.strip()
            if num.isdigit():
                href = link.get('href')
                urls.append(href if href.startswith('http') else base_url + href)
    
    return urls

def extract_dress_info(url, count):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    dresses = soup.find_all('div', class_='w-full rounded border')
    for dress in dresses:
        count += 1
        info = dress.find('div', class_='p-4')
        itemName = info.find('h4').text.strip()
        price = info.find('h5').text.strip()
        with open('dressInfo.txt','a') as file:
            file.write(f"{count}, {itemName}, {price}\n")
        
    return count

def main():
    base_url = 'https://scrapingclub.com/exercise/list_basic/'
    urls = get_page_links(base_url)
    count = 0
    for url in urls:
        count = extract_dress_info(url, count)

if __name__ == "__main__":
    main()

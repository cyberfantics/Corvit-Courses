import requests
from bs4 import BeautifulSoup

# Define the URL
url = 'http://quotes.toscrape.com/'

# Make a request to the website
response = requests.get(url)

# Parse the content of the request
soup = BeautifulSoup(response.text, 'lxml')

# Find all quotes, authors, and tags
quotes = soup.find_all("span", class_="text")
authors = soup.find_all("small", class_="author")
tags = soup.find_all("div", class_="tags")

# Open the file in append mode
with open('quotes.txt', 'a') as file:
    for i in range(len(quotes)):
        quote_text = quotes[i].text
        author_text = authors[i].text
        quote_tags = tags[i].find_all('a', class_='tag')
        tag_list = [tag.text for tag in quote_tags]
        
        # Write the quote, author, and tags to the file
        file.write(f"{quote_text}-+- {author_text}-+- {tag_list}\n")

print("Quotes have been written to 'quotes.txt'.")

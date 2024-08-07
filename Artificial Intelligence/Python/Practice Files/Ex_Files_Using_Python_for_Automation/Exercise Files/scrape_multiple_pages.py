# import relevant libraries
import requests 
from bs4 import BeautifulSoup
from time import sleep

# for loop to iterate over the range of page numbers you want to scrape from
# note: python includes the first argument and excludes the second argument in the range function
for page_number in range(1,4):

    # define the url
    url = "https://www.feedbooks.com/publicdomain/browse/top?lang=en&page="+str(page_number)

    # send a request to get html code from that url
    response = requests.get(url, headers={"Accept": "text/html"}) 

    # parse the response
    parsed_response = BeautifulSoup(response.text, "html.parser") 

    # extract all the elements specific to book titles from that page
    title_elements = parsed_response.find_all("a", class_="block__item-title")

    # extract all the elements specific to book authors from that page
    author_elements = parsed_response.find_all("a", class_="block__item-author")

    # print out the page number 
    print("\nPage Number:", page_number)

    # print out the book titles appearing on that page after formatting the text 
    print("\nBook Titles:", list(map(lambda x: x.text.strip(), title_elements)))

    # print out the book authors appearing on that page after formatting the text 
    print("\nBook Authors:", list(map(lambda x: x.text.strip(), author_elements)))

    # pause the program for 1 second between iterations of the loop
    sleep(1)
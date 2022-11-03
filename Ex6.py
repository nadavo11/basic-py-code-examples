"""
______________________________________________________________________________

                                EX 6


        Use the BeautifulSoup library and requests Python packages
        to print out a list of all the article titles on the
        New York Times homepage
_____________________________________________________________________________
"""
import requests
from bs4 import BeautifulSoup

# create an html session
url = 'https://www.nytimes.com/'
html = requests.get(url)

# create a beautiful soup instance
bs = BeautifulSoup(html.text, 'html.parser')

# loop over all the titles
for i,  title in enumerate(bs.find_all(class_="indicate-hover")):
    print(f'title no. {i}:\t{title.string}\n')

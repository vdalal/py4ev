# https://www.freecodecamp.org/learn/scientific-computing-with-python/python-for-everybody
# www.py4e.org

# web scraping with beautifulsoup library (chapter 12)
import urllib.request
from bs4 import BeautifulSoup

url = input('Enter URL e.g. http://www.dr-chuck.com/page1.htm : ') # e.g. http://www.dr-chuck.com/page1.htm
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all the anchor tags
tags = soup('a')
for tag in tags:
    print('Print all a tags:', tag.get('href', None))

# Retrieve all the h1 tags
tags = soup('h1')
for tag in tags:
    print('Print all h1 tags:', tag.get('href', None))

fhandle = urllib.request.urlopen(url)
for line in fhandle:
    print(line.decode().strip())
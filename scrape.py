from bs4 import BeautifulSoup
import requests

source = requests.get('https://agarwalshalini.wordpress.com/blog-feed/').text # adding text at the end to get the source code from the response object returned by the requests.get() command

soup = BeautifulSoup(source, 'lxml')

for article in soup.find_all('article'):

    headline = article.h2.a.text
    print(headline)

    summary = article.find('div', class_ = 'entry-content').p.text
    print(summary)

    img_src = article.img['src']
    print(img_src)
    
    print()
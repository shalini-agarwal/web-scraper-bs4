from bs4 import BeautifulSoup
import requests

source = requests.get('https://agarwalshalini.wordpress.com/blog-feed/').text # adding text at the end to get the source code from the response object returned by the requests.get() command

soup = BeautifulSoup(source, 'lxml')

article = soup.find('article')

# print(article.prettify())

# headline = article.h2.a.text
# print(headline)

# summary = article.find('div', class_ = 'entry-content').p.text
# print(summary)

#unlike before we don't want to grab the text from this tag. We want to get the value of the 'src' attribute of the tag. If we want to get a value from the attribute of a tag, then we need to access it like a dictionary.
img_src = article.img['src']
print(img_src)
from bs4 import BeautifulSoup
import requests


with open('simple.html') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')

#1
# print(soup.prettify())

#2
# match = soup.title.text

#3
# match = soup.div

#4
# with this find method we can pass in arguments of attributes that narrow down what tag we actually want
# these arguments can match any arguments that the tag might have for eg, if we want to see a div with an id, we can just pass 'id=' in the find method.
# but we need an underscore after class is because class is a special keyword in python
# match = soup.find('div', class_='footer') 

# 5
# article = soup.find('div', class_='article')

# print(article)

# headline = article.h2.a.text

# print(headline)

# summary = article.p.text

# print(summary)

for article in soup.find_all('div', class_='article'):
    headline = article.h2.a.text
    print(headline)

    summary = article.p.text
    print(summary)

    print()
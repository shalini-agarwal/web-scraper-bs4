from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('https://agarwalshalini.wordpress.com/blog-feed/').text # adding text at the end to get the source code from the response object returned by the requests.get() command

soup = BeautifulSoup(source, 'lxml')

csv_file = open('cms_scrape.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['headline', 'summary', 'video_link'])

for article in soup.find_all('article'):

    headline = article.h2.a.text
    print(headline)

    summary = article.find('div', class_ = 'entry-content').p.text
    print(summary)

    try:
        img_src = article.img['src']
    except Exception as e:
        img_src = None 
        
    print(img_src)
    print()

    csv_writer.writerow([headline, summary, img_src])

csv_file.close()


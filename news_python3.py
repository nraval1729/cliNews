from lxml import html
import requests

# print "hello world, soon I will scrape!"

page = requests.get('https://news.google.com/')
tree = html.fromstring(page.content)

news = tree.xpath('//div[@class="section top-stories-section section-toptop"]//h2[@class="esc-lead-article-title"]/a/span[@class="titletext"]/text()')

summary = tree.xpath('//div[@class="section top-stories-section section-toptop"]//div[@class="esc-lead-snippet-wrapper"]/text()')

print ("Here's some top stories to kickstart your day!\r\n")
print ("HEADLINES\r\n")

for headline, description in zip(news, summary):
    print (headline)
    print ("--> " ,description,"\r\n\r\n")

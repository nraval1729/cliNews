from lxml import html
import requests

# print "hello world, soon I will scrape!"

page = requests.get('https://news.google.com/')
tree = html.fromstring(page.content)

news = tree.xpath('//div[@class="section top-stories-section section-toptop"]//h2[@class="esc-lead-article-title"]/a/span[@class="titletext"]/text()')

summary = tree.xpath('//div[@class="section top-stories-section section-toptop"]//div[@class="esc-lead-snippet-wrapper"]/text()')

# print "Summary"
#
# for s in summary:
#     print "--> ",s
#     print
#     print
#
# # print "buyers: ", buyers
# # print "prices: ", prices
#
# print "Headlines"
#
# for newstory in news:
#     # print "*************************************"
#     print "-->" ,newstory
#     print
#     print
#     # print "*************************************"

print "Here's some top stories to kickstart your day!"
print
print "HEADLINES"
print

for headline, description in zip(news, summary):
    print headline
    print "--> " ,description
    print
    print


# //div[@class="section top-stories-section section-toptop"]

# /html/body/div[3]/div[1]/div/div/div[3]/div/div[1]/table/tbody/tr/td[1]/div/div/div[1]/div[2]/div[2]/div/div/div/div[2]/table/tbody/tr/td[2]/div[1]/h2/a/span

# /html/body/div[3]/div[1]/div/div/div[3]/div/div[1]/table/tbody/tr/td[1]/div/div/div[1]/div[2]/div[4]/div/div/div/div[2]/table/tbody/tr/td[2]/div[3]

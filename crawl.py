from pyquery import PyQuery as pq

alliance_url = 'https://us.battle.net/forums/en/wow/topic/6933305306?page=1'
horde_url = 'https://us.battle.net/forums/en/wow/topic/6933305306?page=2'

def crawl(url):
    d = pq(url)
    for item in d('.TopicPost-bodyContent:gt(0) strong'):
        item = pq(item)
        head = item.text()
        body = str(item).replace(item.outerHtml(), '').strip()
        if head == 'Guild:':
            print(body)

print('Alliance\n')
crawl(alliance_url)
print('\nHorde\n')
crawl(horde_url)

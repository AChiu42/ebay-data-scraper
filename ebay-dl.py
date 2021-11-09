import argparse
import requests
from bs4 import BeautifulSoup
import json
import csv

def parse_price(text):  # price filter
    num = ''
    for characters in text:
        if characters in '1234567890':
            num += characters
    if '$' in text:
        numbers = int(num)
        return numbers

def parse_items_sold(text):
    '''
    Takes as input a string and returns the number of items sold, as specified in the string

    >>> parse_itemsold('38 sold')
    38
    >>> parse_itemsold('14 watchers')
    0
    >>> parse_itemsold('Almost gone')
    0
    '''
    num = ''
    for characters in text:
        if characters in '1234567890':
            num += characters
    if 'sold' in text:
        return int(num)
    else:
        return 0

parser = argparse.ArgumentParser(description='ebay item scraper')
parser.add_argument('search_term')
parser.add_argument('--csv', default=True)
args = parser.parse_args()
print('args.search_term=', args.search_term)

# all items on ebay webpages
items = []
for pgn in range(1,2): # change back to 11 later
    # building url
    url = 'https://www.ebay.com/sch/i.html?_from=R40&_nkw='
    url += args.search_term
    url += '&_sacat=0&_dmd=1&_pgn='
    url += str(pgn)
    url += '&rt=nc'
    print('url=', url)

    # downloading html
    r = requests.get(url)
    status = r.status_code
    print('status=', status)
    html = r.text
    # print('html=', html[:50])

    #processing html
    soup = BeautifulSoup(html, 'html.parser')
    
    tags_items = soup.select('.s-item')
    for tag_item in tags_items:
        print('tag_item=', tag_item)

        name = None
        tags_name = tag_item.select('.s-item__title')
        for tag in tags_name:
            name = tag.text

        price = None
        tags_name = tag_item.select('.s-item__price')
        for tag in tags_name:
            price = parse_price(tag.text)

        status = False
        tags_name = tag_item.select('.SECONDARY_INFO')
        for tag in tags_name:
            status = tag.text

        shipping = 0
        tags_name = tag_item.select('.s-item__shipping')
        for tag in tags_name:
            shipping = parse_price(tag.text)
                
        free_returns = False
        tags_free_returns = tag_item.select('.s-item__free-returns')
        for tag in tags_free_returns: 
            free_returns = True

        items_sold = 0
        tags_items_sold = tag_item.select('.s-item__hotness')
        for tag in tags_items_sold: 
            items_sold = parse_items_sold(tag.text)

        item = {
            'name': name, 
            'price': price,
            'status': status,
            'shipping': shipping,
            'freereturns': free_returns,
            'itemssold': items_sold
        }
        items.append(item)
        print('len(tags_item)=', len(tags_items))
        print('len(items)=', len(items))

if args.csv == False:
    filename = args.search_term+'.json'
    with open(filename, 'w', encoding='ascii') as f:
        f.write(json.dumps(items))

else:
    fields = ['name', 'price', 'status', 'shipping', 'freereturns', 'itemssold']
    filename = args.search_term+'.csv'
    with open(filename, 'w', encoding = 'utf-8') as c:
        writer = csv.DictWriter(c, fields)
        writer.writeheader()
        writer.writerows(items)
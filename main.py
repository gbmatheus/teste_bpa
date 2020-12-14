import requests
import csv
from bs4 import BeautifulSoup as bs

def save_data_csv (archive_name, data):
    with open(archive_name+'.csv', 'w', newline='') as file:
        writer = csv.writer(file, delimiter= '|')
        writer.writerow(['product_name','price'])
        writer.writerows(data)

def main ():
    products = list ()

    url_amazon_home = 'https://www.amazon.com.br/'

    url_amazon_search = 'https://www.amazon.com.br/s?k='
    item_search = 'iphone'

    url = url_amazon_search + item_search

    response_amazon = requests.get(url)

    soup = bs(response_amazon.text, 'html.parser')

    last_divs = soup.find_all('div', {'class':'s-widget'})

    for div in last_divs:
        div.decompose()

    # products_list = soup.find('div', {'class':'s-main-slot s-result-list s-search-results sg-row'})

    products_list_items = soup.find_all(class_ = 's-result-item')

    for item in products_list_items:
        name = ''
        price = ''

        name_item = item.find(class_ = 'a-size-base-plus')
        name = name_item.contents[0]

        price_item = item.find(class_ = 'a-offscreen')
        if(price_item == None):
            price = 'No price'
        else:
            price = price_item.contents[0]

        products.append([name, price])

    save_data_csv('amazon_iphone_search', products)

if __name__ == "__main__":
    main()
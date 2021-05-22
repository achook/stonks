from requests import get
from bs4 import BeautifulSoup
from datetime import date

def get_generali_quotes(names):
    quotes = {}
    
    webpage = get('https://generali-investments.pl/contents/pl/klient-indywidualny/wyceny-funduszy-otwartych')
    soup = BeautifulSoup(webpage.text, 'html.parser')

    raw_date = soup.find('input', id='valuation-date')['value']
    quote_date = date.fromisoformat(raw_date)

    return quotes

def get_investors_quotes(names):
    quotes = {}

    webpage = get('https://investors.pl/fundusze-inwestycyjne/')
    soup = BeautifulSoup(webpage.text, 'html.parser')

    raw_date = soup.find('form', 'filter-funds').find('span', 'l').get_text()
    raw_date = raw_date[9:-1]
    [day, month, year] = raw_date.split('.')
    day, month, year = int(day), int(month), int(year)
    quote_date = date(year, month, day)

    table = soup.find('table', 'table-funds')
    table = table.find('tbody')

    for row in table.find_all('tr', recursive=False):
        name = row.find('td', 'col-name').h2.a.get_text()
        
        if name not in names:
            continue

        value = row.find('td', 'col-val').contents[0]
        value = float(value)

        quotes[name] = {
            'quote': value,
            'date': quote_date
        }

    return quotes

def get_nn_quotes(names):
    quotes = {}

    webpage = get("https://www.nntfi.pl/notowania")
    soup = BeautifulSoup(webpage.text, 'html.parser')
    table = soup.find('tbody', 'table_body')

    for element in table.contents:
        row = element.find('td', 'coll_2')
        name = None

        if row.a :
            name = row.a.get_text()
        else:
            name = row.contents[0]

        if name not in names:
            continue

        value = row.find('div', 'mobile_date').contents[0]
        value = value[:-4]
        value = value.replace(',','.')
        value = float(value)

        raw_date = row.find('span', 'quotes-date').get_text()
        [day, month, year] = raw_date.split('.')
        day, month, year = int(day), int(month), int(year)
        quote_date = date(year, month, day)

        quotes[name] = {
            'quote': value,
            'date': quote_date
        }

    return quotes

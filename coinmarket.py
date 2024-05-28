# %%
# This example uses Python 2.7 and the python-request library.
import pandas as pd
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
    'start': '1',
    'limit': '5000',
    'convert': 'USD'
}
headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': '68617460-3b63-4796-8610-b5a31a990caf',
}

session = Session()
session.headers.update(headers)

try:
    response = session.get(url, params=parameters)
    data = json.loads(response.text)
    print(data)
except (ConnectionError, Timeout, TooManyRedirects) as e:
    print(e)
data = data['data']
data[0].keys()
data[0]['quote']['USD'].keys()
a = ['id', 'name', 'symbol', 'circulating_supply']
b = ['price', 'volume_24h', 'market_cap', 'percent_change_1h', 'percent_change_24h',
     'percent_change_7d', 'market_cap']
attributes = a+b
crypto = []
for i in data:
    tmp = []
    for j in a:
        tmp.append(i[j])
    for k in b:
        tmp.append(i['quote']['USD'][k])
    crypto.append(tmp)
crypto
dataframe = pd.DataFrame(crypto, columns=attributes)
dataframe.to_csv(
    'crypto.csv', index=0)

import requests

order_currency = 'BTC'
payment_currency ='KRW'
URL = f'https://api.bithumb.com/public/ticker/ALL_{payment_currency}'

response = requests.get(URL)
print(response)
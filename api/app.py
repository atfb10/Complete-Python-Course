# Example using OpenExchangeRates
from libs.openexchangerates import OpenExchangeClient

APP_ID = '19c836dd741041b4bd0df80c12e6e851'

client = OpenExchangeClient(APP_ID)

amount = float(input('Enter amount: '))
exchange = input('Enter exchange: ')
convert_to = input('Enter currency you want: ')

requested_currency_amount = client.convert(amount, exchange, convert_to)
print(requested_currency_amount)
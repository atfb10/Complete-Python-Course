import requests
from cachetools import cached, TTLCache

class OpenExchangeClient:
    BASE_URL = 'https://openexchangerates.org/api'

    def __init__(self, app_id):
        self.app_id = app_id

    @property
    @cached(cache=TTLCache(maxsize=2, ttl=3600))
    def latest(self):
        '''
        cache the function so you don't have to hit the server every call
        only wish to cache for 1 hour, to ensure data is up to date ttl = time to live
        3600 is seconds in an hour
        '''
        return requests.get(f"{self.BASE_URL}/latest.json?app_id={self.app_id}").json()

    def convert(self, amount: float, start_currency: str, desired_currency: str) -> float:
        '''
        if usd start currency, convert immediately
        if not usd start currency, convert to usd, then return proper amount
        if user input error, return -1.00
        '''
        rates = self.latest['rates']
        to_rate = rates[desired_currency]

        if to_rate == None:
            return -1.00
        elif start_currency == 'USD':
            return round(amount * to_rate, 2)
        else: 
            usd_amount = amount / rates[start_currency]
            return round(usd_amount * to_rate, 2)
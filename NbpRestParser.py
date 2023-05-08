import json

import requests

from ExchangeRates import ExchangeRates
from Rate import Rate


class NbpRestParser:

    def parse(self):
        print("parsing")
        res = requests.get("http://api.nbp.pl/api/exchangerates/tables/b?format=json")
        print(res.text)

        js = '''{"currency":"afgani (Afganistan)","code":"AFN","mid":0.047834}'''
        j = json.loads(js)
        rate = Rate(**j)

        print(rate)
        data = res.json()[0]

        table = data['table']
        no = data['no']
        effective_date = data['effectiveDate']
        rates = [Rate(rate['currency'], rate['code'], rate['mid']) for rate in data['rates']]

        exchange_rates = ExchangeRates(table, no, effective_date, rates)

        print(exchange_rates)

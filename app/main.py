import requests

from app.nbp_rate_saver import save_list_of_rate_to_csv
from nbp_rate_fetcher import process_response_json

if __name__ == '__main__':

    table_a_url = "http://api.nbp.pl/api/exchangerates/tables/a?format=json"
    table_b_url = "http://api.nbp.pl/api/exchangerates/tables/b?format=json"

    table_a_response = requests.get(table_a_url)
    table_a_response.raise_for_status()

    table_b_response = requests.get(table_b_url)
    table_b_response.raise_for_status()

    table_a_rates = process_response_json(table_a_response.json()[0])
    table_b_rates = process_response_json(table_b_response.json()[0])

    merged_rates = table_a_rates + table_b_rates
    merged_rates = sorted(merged_rates, key=lambda rate: rate.code)

    save_list_of_rate_to_csv(merged_rates)

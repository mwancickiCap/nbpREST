import datetime
from unittest import TestCase
from unittest.mock import patch, mock_open

from app.Rate import Rate
from app.nbp_rate_fetcher import process_response_json
from app.nbp_rate_saver import save_list_of_rate_to_csv


class TestNbpRestParser(TestCase):
    valid_response_json = {
        'table': 'B',
        'no': '018/B/NBP/2023',
        'effectiveDate': '2023-05-02',
        'rates': [
            {'currency': 'afgani (Afganistan)', 'code': 'AFN', 'mid': 0.047834},
            {'currency': 'ariary (Madagaskar)', 'code': 'MGA', 'mid': 0.000951}
        ]
    }

    invalid_response_json1 = {
        'table': 'B',
        'no': '018/B/NBP/2023',
        'rates': [
            {'currency': 'afgani (Afganistan)', 'code': 'AFN', 'mid': 0.047834},
            {'currency': 'ariary (Madagaskar)', 'code': 'MGA', 'mid': 0.000951}
        ]
    }

    invalid_response_json2 = {
        'table': 'B',
        'no': '018/B/NBP/2023',
        'effectiveDate': '2023-05-02'
    }

    def test_response_json_maps_to_entity(self):
        exchange_rates = process_response_json(self.valid_response_json)

        self.assertEqual(len(exchange_rates), 2)
        self.assertEqual(exchange_rates[0].currency, 'afgani (Afganistan)')
        self.assertEqual(exchange_rates[0].code, 'AFN')
        self.assertEqual(exchange_rates[0].mid, 0.047834)
        self.assertEqual(exchange_rates[1].currency, 'ariary (Madagaskar)')
        self.assertEqual(exchange_rates[1].code, 'MGA')
        self.assertEqual(exchange_rates[1].mid, 0.000951)

    def test_assert_raise_if_no_effective_date(self):
        with self.assertRaises(RuntimeError) as exc:
            process_response_json(self.invalid_response_json1)

        self.assertEqual(str(exc.exception), 'Failed to process response JSON: Invalid JSON data structure')

    def test_assert_raise_if_no_rates(self):
        with self.assertRaises(RuntimeError) as exc:
            process_response_json(self.invalid_response_json2)

        self.assertEqual(str(exc.exception), 'Failed to process response JSON: Invalid JSON data structure')

    @patch('builtins.open', new_callable=mock_open)
    def test_save_list_of_rate_to_csv(self, mock_file_open):
        rates = [
            Rate('USD', 'USD', 1.0, '2023-05-10'),
            Rate('EUR', 'EUR', 0.9, '2023-05-10')
        ]
        expected_filename = str(datetime.date.today()) + '-rates.csv'

        save_list_of_rate_to_csv(rates)

        mock_file_open.assert_called_once_with(expected_filename, mode='w', newline='')

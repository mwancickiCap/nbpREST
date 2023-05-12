from unittest import TestCase

from app.Rate import Rate
from app.nbp_rate_fetcher import process_response_json


class TestNbpRestParser(TestCase):
    expected_list_of_rates = [Rate('afgani (Afganistan)', 'AFN', 0.047834, '2023-05-02'),
                              Rate('ariary (Madagaskar)', 'MGA', 0000.000951, '2023-05-02')]

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

        self.assertEqual(exchange_rates, self.expected_list_of_rates)

    def test_assert_raise_if_no_effective_date(self):
        with self.assertRaises(RuntimeError) as exc:
            process_response_json(self.invalid_response_json1)

        self.assertEqual(str(exc.exception), 'Failed to process response JSON: Invalid JSON data structure')

    def test_assert_raise_if_no_rates(self):
        with self.assertRaises(RuntimeError) as exc:
            process_response_json(self.invalid_response_json2)

        self.assertEqual(str(exc.exception), 'Failed to process response JSON: Invalid JSON data structure')
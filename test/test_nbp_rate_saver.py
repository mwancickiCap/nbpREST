import datetime
from unittest import TestCase
from unittest.mock import patch, mock_open

from app.Rate import Rate
from app.nbp_rate_saver import save_list_of_rate_to_csv


class Test(TestCase):
    @patch('builtins.open', new_callable=mock_open)
    def test_save_list_of_rate_to_csv(self, mock_file_open):
        rates = [
            Rate('USD', 'USD', 1.0, '2023-05-10'),
            Rate('EUR', 'EUR', 0.9, '2023-05-10')
        ]
        expected_filename = str(datetime.date.today()) + '-rates.csv'

        save_list_of_rate_to_csv(rates)

        mock_file_open.assert_called_once_with(expected_filename, mode='w', newline='')

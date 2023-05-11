import csv
import datetime


def save_list_of_rate_to_csv(rates):
    fieldnames = ['currency', 'code', 'mid', 'effective_date']
    filename = str(datetime.date.today()) + '-rates.csv'

    with open(filename, mode='w', newline='') as rates_file:
        writer = csv.DictWriter(rates_file, fieldnames=fieldnames, delimiter=',', quotechar='"',
                                quoting=csv.QUOTE_MINIMAL)
        writer.writeheader()
        writer.writerows([
            {
                'currency': rate.currency,
                'code': rate.code,
                'mid': rate.mid,
                'effective_date': rate.effective_date}
            for rate in rates
        ])

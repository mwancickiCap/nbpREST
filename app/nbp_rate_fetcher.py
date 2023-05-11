from app.Rate import Rate


def process_response_json(response_json):
    try:
        if 'effectiveDate' not in response_json or 'rates' not in response_json:
            raise ValueError('Invalid JSON data structure')
        effective_date = response_json['effectiveDate']
        rates = [Rate(rate['currency'], rate['code'], rate['mid'], effective_date) for rate in response_json['rates']]
        return rates
    except ValueError as e:
        raise RuntimeError(f"Failed to process response JSON: {str(e)}")


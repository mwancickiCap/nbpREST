from Rate import Rate


class ExchangeRates:
    def __init__(self, table, no, effective_date, rates):
        self.table = table
        self.no = no
        self.effectiveDate = effective_date
        self.rates = rates

    def __str__(self):
        return "{0} ,{1}, {2}, {3}".format(self.table, self.no, self.effectiveDate, self.rates)

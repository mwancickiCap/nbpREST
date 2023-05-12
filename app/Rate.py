class Rate:
    def __init__(self, currency, code, mid, effective_date):
        self.currency = currency
        self.code = code
        self.mid = mid
        self.effective_date = effective_date

    def __str__(self):
        return "{0} ,{1}, {2}, {3}".format(self.currency, self.code, self.mid, self.effective_date)

    def __eq__(self, other):
        if isinstance(other, Rate):
            return (
                    self.currency == other.currency and
                    self.code == other.code and
                    self.mid == other.mid and
                    self.effective_date == other.effective_date
            )
        return False

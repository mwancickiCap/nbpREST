class Rate:
    def __init__(self, currency, code, mid):
        self.currency = currency
        self.code = code
        self.mid = mid

    def __str__(self):
        return "{0} ,{1}, {2}".format(self.currency, self.code, self.mid)

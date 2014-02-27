import calendar


def make_month(year, month):
    return Month(year, month)


class Month(object):

    def __init__(self, year, month):
            days = ['Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa', 'Su']
            self.first, self.last = calendar.monthrange(year, month)
            self.days = days[self.first - 1::] + days[:self.first - 1:]

    def day(self, value):
        if 0 < value <= self.last and int(value):
            return self.days[(value) % 7]
        raise ValueError('Date does not exist within that month')

import unittest
import make_month
import datetime


class DayTest(unittest.TestCase):

    def setUp(self):
        self.month = make_month.Month(2012, 2)
        self.days = ['Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa', 'Su']

    def test_correct(self):
        for i in range(1, 20):
            self.assertEqual(self.days[datetime.date(2012, 2, i).weekday()],
                             self.month.day(i))

    def test_upper(self):
        with self.assertRaises(ValueError):
            self.month.day(32)

    def test_negtive(self):
        with self.assertRaises(ValueError):
            self.month.day(-4)

    def test_non_int(self):
        with self.assertRaises(ValueError):
            for i in [True, 'This', 3.14, (1, 2, 3), ['list'], {'dict': 6}]:
                self.month.day(i)


if __name__ == '__main__':
    unittest.main()

import unittest
from evaluate import *


class MyTestCase(unittest.TestCase):
    def test_complex_power(self):
        self.assertEqual(complex_power(1, 1j), 1)
        self.assertEqual(complex_power(2, 2), 4)
        self.assertEqual(complex_power(2, 2j), cmath.exp(-1j*2*math.log(2)))

    def test_Bernoulli(self):
        self.assertEqual(B(2), 1/6)
        self.assertEqual(B(3), 0)


if __name__ == '__main__':
    unittest.main()

import unittest
import sys
sys.path.insert(0, '..')
from ipynb.fs.full.index import (term_output, output_at, delta_f, derivative_of)

class IntroToDerivatives (unittest.TestCase):
    def test_term_output(self):
        self.assertEqual(term_output((3, 2), 2), 12)

    def test_output_at(self):
        three_x_squared_minus_eleven = [(3, 2), (-11, 0)]
        self.assertEqual(output_at(three_x_squared_minus_eleven, 2), 1)
        self.assertEqual(output_at(three_x_squared_minus_eleven, 3), 16)

    def test_delta_f(self):
        four_x_plus_fifteen = [(4, 1), (15, 0)]
        self.assertEqual(delta_f(four_x_plus_fifteen, 2, 1), 4)

    def test_derivative_of(self):
        four_x_plus_fifteen = [(4, 1), (15, 0)]
        self.assertEqual(derivative_of(four_x_plus_fifteen, 3, 2), 4)

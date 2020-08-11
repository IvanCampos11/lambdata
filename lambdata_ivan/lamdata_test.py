"""Tests for lamdata modules."""

import unittest

from lambdata_ivan.example_module import fibonacci


class FibonacciTest(unittest.TestCase):
    """Tests the instatiation and use of DFMod"""

    def test_fionacci(self):
        x1 = 9
        y1 = fibonacci(x1)
        x2 = 100
        y2 = fibonacci(x2)
        self.assertEqual(y1, 21)
        self.assertEqual(y2, 4181)

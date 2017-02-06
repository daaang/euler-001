from hamcrest import *
import unittest

from .euler import sum_of_multiples

class SumOfMultiplesTestBase (unittest.TestCase):

    factors = [ ]

    def assert_sum (self, ceiling, expected):
        args = tuple(self.factors + [ceiling])
        assert_that(sum_of_multiples(*args), is_(equal_to(expected)))

class GivenNoFactors (SumOfMultiplesTestBase):

    def test_sum_up_to_zero_is_zero (self):
        self.assert_sum(0, 0)

    def test_sum_up_to_one_is_zero (self):
        self.assert_sum(1, 0)

    def test_sum_up_to_1000_is_zero (self):
        self.assert_sum(1000, 0)

class GivenFactorOfOne (SumOfMultiplesTestBase):

    factors = [1]

    def test_sum_up_to_zero_is_zero (self):
        self.assert_sum(0, 0)

    def test_sum_up_to_one_is_one (self):
        self.assert_sum(1, 1)

    def test_sum_up_to_two_is_three (self):
        self.assert_sum(2, 3)

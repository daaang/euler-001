from hamcrest import *
import unittest

from .euler import sum_of_multiples

class SumOfMultiplesTestBase (unittest.TestCase):

    factors = [ ]

    def assert_sum (self, ceiling, expected):
        args = tuple(self.factors + [ceiling])
        assert_that(sum_of_multiples(*args), is_(equal_to(expected)))

    def test_sum_below_zero_is_zero (self):
        self.assert_sum(0, 0)

    def test_sum_below_one_is_zero (self):
        self.assert_sum(1, 0)

class GivenNoFactors (SumOfMultiplesTestBase):

    def test_sum_below_1000_is_zero (self):
        self.assert_sum(1000, 0)

class GivenFactorOfOne (SumOfMultiplesTestBase):

    factors = [1]

    def test_sum_below_two_is_one (self):
        self.assert_sum(2, 1)

    def test_sum_below_three_is_three (self):
        self.assert_sum(3, 3)

    def test_sum_below_ten_is_45 (self):
        self.assert_sum(10, 45)

class GivenFactorOfTwo (SumOfMultiplesTestBase):

    factors = [2]

    def test_sum_below_two_is_zero (self):
        self.assert_sum(2, 0)

    def test_sum_below_three_is_two (self):
        self.assert_sum(3, 2)

    def test_sum_below_ten_is_twenty (self):
        self.assert_sum(10, 20)

class GivenFactorOfThree (SumOfMultiplesTestBase):

    factors = [3]

    def test_sum_below_two_is_zero (self):
        self.assert_sum(2, 0)

    def test_sum_below_three_is_zero (self):
        self.assert_sum(3, 0)

    def test_sum_below_ten_is_18 (self):
        self.assert_sum(10, 18)

class GivenFactorOfFive (SumOfMultiplesTestBase):

    factors = [5]

    def test_sum_below_ten_is_five (self):
        self.assert_sum(10, 5)

class GivenFactorsOfTwoAndThree (SumOfMultiplesTestBase):

    factors = [2, 3]

    def test_sum_below_three_is_two (self):
        self.assert_sum(3, 2)

    def test_sum_below_four_is_five (self):
        self.assert_sum(4, 5)

    def test_sum_below_seven_is_fifteen (self):
        self.assert_sum(7, 15)

class GivenFactorsOfThreeAndFive (SumOfMultiplesTestBase):

    factors = [3, 5]

    def test_sum_below_1000_is_233168 (self):
        self.assert_sum(1000, 233168)

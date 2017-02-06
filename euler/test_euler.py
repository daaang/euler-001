from hamcrest import *
import unittest

from .euler import sum_of_multiples

class GivenNoFactors (unittest.TestCase):

    def test_sum_up_to_zero_is_zero (self):
        assert_that(sum_of_multiples(0), is_(equal_to(0)))

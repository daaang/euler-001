class MultipleSummer:

    def __init__ (self, *args):
        self.factors = list(args)
        self.ceiling = self.factors.pop()
        self.remove_invalid_factors()

    def __call__ (self):
        return sum(self.unique_multiples_under_ceiling())

    def remove_invalid_factors (self):
        valid_factors = []
        for factor in self.factors:
            if factor > 0:
                valid_factors.append(factor)
        self.factors = valid_factors

    def unique_multiples_under_ceiling (self):
        self.mutable_factors = list(self.factors)
        return self.range_without_duplicates()

    def range_without_duplicates (self):
        while self.mutable_factors:
            factor = self.mutable_factors.pop(0)
            yield from self.get_multiples_of(factor)

    def get_multiples_of (self, factor):
        for i in self.all_multiples_under_ceiling(factor):
            if self.is_not_a_multiple_of_another_factor(i):
                yield i

    def all_multiples_under_ceiling (self, factor):
        return range(0, self.ceiling, factor)

    def is_not_a_multiple_of_another_factor (self, n):
        return all(n % f != 0 for f in self.mutable_factors)

def sum_of_multiples (*args):
    x = MultipleSummer(*args)
    return x()

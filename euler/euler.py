class MultipleSummer:

    def __init__ (self, *args):
        self.factors = list(args)
        self.ceiling = self.factors.pop()

    def __call__ (self):
        return sum(self.unique_multiples_under_ceiling())

    def unique_multiples_under_ceiling (self):
        self.mutable_factors = list(self.factors)
        return self.range_without_duplicates()

    def range_without_duplicates (self):
        while self.mutable_factors:
            factor = self.mutable_factors.pop(0)
            yield from self.get_multiples_of(factor)

    def get_multiples_of (self, factor):
        for i in self.all_multiples_under_ceiling(factor):
            if all(i%j != 0 for j in self.mutable_factors):
                yield i

    def all_multiples_under_ceiling (self, factor):
        return range(0, self.ceiling, factor)

def sum_of_multiples (*args):
    x = MultipleSummer(*args)
    return x()

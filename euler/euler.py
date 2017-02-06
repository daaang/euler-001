class MultipleSummer:

    def __init__ (self, *args):
        self.factors = list(args)
        self.ceiling = self.factors.pop()

    def __call__ (self):
        return sum(self.unique_multiples_under_ceiling())

    def unique_multiples_under_ceiling (self):
        factors = list(self.factors)

        while factors:
            factor = factors.pop(0)
            yield from self.range_without_duplicates(factor, factors)

    def range_without_duplicates (self, factor, factors):
        for i in range(0, self.ceiling, factor):
            if all(i%j != 0 for j in factors):
                yield i

def sum_of_multiples (*args):
    x = MultipleSummer(*args)
    return x()

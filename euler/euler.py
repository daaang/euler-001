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
            yield from range_without_duplicates(self.ceiling, factor, factors)

def range_without_duplicates (ceiling, factor, factors):
    for i in range(0, ceiling, factor):
        if all(i%j != 0 for j in factors):
            yield i

def sum_of_multiples (*args):
    x = MultipleSummer(*args)
    return x()

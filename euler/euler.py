def sum_of_multiples (*args):
    factors = list(args)
    ceiling = factors.pop()

    return sum(range(0, ceiling, factors[0])) if factors else 0

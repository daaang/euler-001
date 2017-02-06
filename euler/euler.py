def sum_of_multiples (*args):
    factors = list(args)
    ceiling = factors.pop()

    return sum(range(ceiling)) if factors else 0

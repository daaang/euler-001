def sum_of_multiples (*args):
    factors = list(args)
    ceiling = factors.pop()

    return sum(range(ceiling+1)) if factors else 0

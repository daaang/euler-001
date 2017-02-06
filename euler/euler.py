def sum_of_multiples (*args):
    factors = list(args)
    ceiling = factors.pop()

    return ceiling if factors else 0

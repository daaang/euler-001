def sum_of_multiples (*args):
    factors = list(args)
    ceiling = factors.pop()

    return sum(sum(range(0, ceiling, f)) for f in factors) \
            if factors else 0

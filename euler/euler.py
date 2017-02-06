def range_without_duplicates (ceiling, factor, factors):
    for i in range(0, ceiling, factor):
        if all(i%j != 0 for j in factors):
            yield i

def sum_of_multiples (*args):
    factors = list(args)
    ceiling = factors.pop()

    result = 0
    while factors:
        factor = factors.pop(0)
        result += sum(range_without_duplicates(ceiling,
                                               factor,
                                               factors))

    return result

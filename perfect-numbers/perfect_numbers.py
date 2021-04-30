def classify(number):
    if number < 1:
        raise ValueError('Number must be positive integer')
    max_divisor = number // 2
    factors = get_factors(number)
    dividers = get_natural_dividers(factors)
    sum_of_natural_dividers = sum(divider for divider in dividers if divider <= max_divisor)
    if sum_of_natural_dividers == number:
        return 'perfect'
    if sum_of_natural_dividers > number:
        return 'abundant'
    return 'deficient'


def get_natural_dividers(factors):
    dividers = {1}
    for factor in factors:
        new_dividers = [factor * divider for divider in dividers]
        dividers = dividers.union(set(new_dividers))
    return list(dividers)


def get_factors(number):
    result = number
    factors = []
    num = 2
    while result != 1:

        rest = result % num
        if not rest:
            result = result // num
            factors.append(num)
            num = 2
        else:
            num += 1
    return factors

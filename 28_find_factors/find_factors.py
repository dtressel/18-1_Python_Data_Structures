def find_factors(num):
    """Find factors of num, in increasing order.

    >>> find_factors(10)
    [1, 2, 5, 10]

    >>> find_factors(11)
    [1, 11]

    >>> find_factors(111)
    [1, 3, 37, 111]

    >>> find_factors(321421)
    [1, 293, 1097, 321421]
    """

    results_1 = [1]
    i = 2
    while i ** 2 <= num:
        if num % i == 0:
            results_1.append(i)
        i += 1
    results_2 = [int(num / factor) for factor in results_1 if factor ** 2 != num]
    results_2.reverse()
    return results_1 + results_2



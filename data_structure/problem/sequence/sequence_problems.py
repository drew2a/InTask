import math

from data_structure.problem.array.array_problems import extract_digits


def create_3_5_10_array(n):
    five_div_flag = 0
    recalculate_flag = 0
    result_digit = 0
    digits = [0]
    for i in range(int(n / 3)):
        five_div_flag += 1
        result_digit += 3
        recalculate_flag += 1

        if five_div_flag == 5:
            five_div_flag = 0
            digits[0] += 3
            continue

        if recalculate_flag > 3:
            recalculate_flag = 1
            digits = list(extract_digits(result_digit))
        else:
            digits[0] += 3

        digits_sum = sum(digits)
        if digits_sum < 10:
            yield result_digit


def sieve_of_eratosthenes(n, sort=False):
    primes = dict([(i, True) for i in range(3, n + 1, 2)])

    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if not primes[i]:
            continue

        for d in range(i * i, n + 1, i):
            primes[d] = False

    yield 1
    yield 2
    for i in sorted(primes.keys()) if sort else primes.keys():
        if primes[i]:
            yield i

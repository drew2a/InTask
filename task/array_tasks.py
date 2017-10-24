from random import randrange


def _find_second(array, first, value):
    for a in array:
        if a + first == value:
            return a

    return None


def random_array(size, limit=10):
    for i in range(size):
        yield randrange(0, limit)


def find_pairs(array, value):
    result = []
    digits = dict()

    for i in array:
        if i > value:
            continue

        if i not in digits:
            digits[i] = 0
        elif i in digits:
            if i + i == value:
                result.append(tuple((i, i)))
                del digits[i]
            else:
                second = _find_second(digits.keys(), i, value)
                if second is not None:
                    result.append(tuple((i, second)))
                    del digits[second]

    return result


def array_left_rotation(a, k):
    n = len(a)
    start = k % n
    for i in range(start, n):
        yield a[i]

    for i in range(0, start):
        yield a[i]


def extract_digits(n):
    while n > 0:
        yield n % 10
        n = n // 10


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


def merge(array1, array2, condition):
    return list(filter(condition, array1)) + list(filter(condition, array2))

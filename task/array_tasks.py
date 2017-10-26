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


def split_array_by_sign(array):
    if len(array) == 0:
        return []

    current_array = []
    previous_number = array[0]

    for n in array:
        if n * previous_number < 0:
            yield current_array
            current_array = []

        current_array.append(n)

        if n != 0:
            previous_number = n

    if len(current_array) > 0:
        yield current_array


def max_sum_sub_array(given_array):
    sub_arrays = [(sum(a), a) for a in split_array_by_sign(given_array)]
    print('Draft subarrays: {}'.format(sub_arrays))

    if len(sub_arrays) == 1 and sub_arrays[0][0] <= 0:
        yield max(sub_arrays[0][1])
        return

    max_sum = sub_arrays[0][0]
    mi = 0
    mj = 1

    for i in range(0, len(sub_arrays)):
        for j in range(i + 1, len(sub_arrays) + 1):
            current_sum = sum(s[0] for s in sub_arrays[i:j])
            if current_sum > max_sum:
                max_sum = current_sum
                mi = i
                mj = j
    for sub_array in sub_arrays[mi:mj]:
        for item in sub_array[1]:
            yield item


def print_bars(bars, water):
    max_bar = max(bars)
    for h in range(max_bar, 0, -1):
        line = '|'
        for index in range(len(bars)):
            if bars[index] < h and water[index] < h:
                line += '  '
            elif water[index] >= h > bars[index]:
                line += '~~'
            else:
                line += 'oo'
            line += '|'

        print(line)
    line = ' '
    for i in range(len(bars)):
        line += '{:^3}'.format(i)
    print(line)


def find_water_count(array):
    if len(array) <= 2:
        return 0
    print('Given bars:')
    print_bars(array, array)
    water_array = list(array)
    total_water_count = 0
    extremes = find_extremes(array)

    print('\nExtremes: {}'.format(extremes))

    for extrem_index in range(len(extremes) - 1):
        first_extrem = extremes[extrem_index]
        second_extrem = extremes[extrem_index + 1]
        second_extrem_value = second_extrem[1]
        if second_extrem_value < water_array[second_extrem[0]]:
            continue

        increment = 1 if first_extrem[0] < second_extrem[0] else -1
        print('\nMove: {}->{}'.format(first_extrem[0], second_extrem[0]))
        for array_index in range(first_extrem[0] + increment, second_extrem[0], increment):
            if water_array[array_index] < second_extrem_value:
                total_water_count += second_extrem_value - water_array[array_index]
                water_array[array_index] = second_extrem_value

        print_bars(array, water_array)

    return total_water_count


def find_extremes(array):
    size = len(array)
    if size <= 2:
        return []

    extremes = []
    previous_value = 0
    for i in range(size - 1):
        current_value = array[i]
        next_value = array[i + 1]
        if (current_value > previous_value and next_value <= current_value) or \
                (current_value == previous_value and next_value < current_value):
            extremes.append((i, current_value))
        previous_value = current_value

    if array[size - 1] > array[size - 2]:
        extremes.append((size - 1, array[size - 1]))

    return sorted(extremes, key=lambda t: t[1], reverse=True)

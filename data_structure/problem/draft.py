import timeit
from functools import reduce
from random import randrange


def solution1(A):
    if A is None or len(A) == 0:
        return -1

    size = len(A)
    jump_count = 0
    i = 0
    while jump_count < size:
        jump_count += 1

        if A[i] == 0:
            return -1

        i = i + A[i]
        if i >= size or i < 0:
            return jump_count

    return -1


class ComplimentaryPairs:
    @staticmethod
    def solution(K, A):
        if A is None:
            return 0

        complement_dictionary = dict()
        total_sum = 0

        for i in range(len(A)):
            current_item = A[i]
            complement = K - current_item

            if current_item in complement_dictionary:
                total_sum += 2 * complement_dictionary[current_item]

            if current_item == complement:
                total_sum += 1

            if complement not in complement_dictionary:
                complement_dictionary[complement] = 1
            else:
                complement_dictionary[complement] += 1

        return total_sum

    @staticmethod
    def naiv_solution(k, a):
        s = 0
        if a is None:
            return 0

        for i in range(len(a)):
            for j in range(i, len(a)):
                if a[i] + a[j] == k:
                    if i != j:
                        s += 2
                    else:
                        s += 1

        return s

    @staticmethod
    def random_array(size):
        for i in range(size):
            yield randrange(0, size)

    @staticmethod
    def test_it():
        assert 1 == ComplimentaryPairs.solution(6, [3])
        assert 4 == ComplimentaryPairs.solution(6, [3, 3, 2])
        assert 7 == ComplimentaryPairs.solution(6, [1, 8, -3, 0, 1, 3, -2, 4, 5])
        assert 3 + 6 == ComplimentaryPairs.solution(10, [5, 5, 5])
        assert 3 + 6 + 4 == ComplimentaryPairs.solution(10, [5, 5, 5, 1, 9, -10, 20])
        assert 1 == ComplimentaryPairs.solution(0, [0])
        assert 7 == ComplimentaryPairs.solution(0, [0, -2, 2, 2, 2])
        assert 0 == ComplimentaryPairs.solution(0, None)
        assert 1 == ComplimentaryPairs.solution(-2147483648, [-2147483648, -2147483648 / 2])
        assert 0 == ComplimentaryPairs.solution(0, [-2147483648] * 100000)
        assert 16 == ComplimentaryPairs.solution(2147483648, [2147483648 / 2] * 4)
        assert 10000000000 == ComplimentaryPairs.solution(4, [2] * 100000)

        count = 100
        for i in range(count):
            k = randrange(-count, count)
            a = list(ComplimentaryPairs.random_array(count))
            assert ComplimentaryPairs.naiv_solution(k, a) == ComplimentaryPairs.solution(k, a)

        print('1000    : ',
              timeit.timeit('ComplimentaryPairs.solution(0, list(ComplimentaryPairs.random_array(1000)))', number=5, setup="from __main__ import ComplimentaryPairs"))
        print('1,5K    : ',
              timeit.timeit('ComplimentaryPairs.solution(0, list(ComplimentaryPairs.random_array(1500)))', number=5, setup="from __main__ import ComplimentaryPairs"))
        print('1,5K(n) : ',
              timeit.timeit('ComplimentaryPairs.naiv_solution(0, list(ComplimentaryPairs.random_array(1500)))', number=5, setup="from __main__ import ComplimentaryPairs"))
        print('20K     : ',
              timeit.timeit('ComplimentaryPairs.solution(0, list(ComplimentaryPairs.random_array(20000)))', number=5, setup="from __main__ import ComplimentaryPairs"))
        print('30K     : ',
              timeit.timeit('ComplimentaryPairs.solution(0, list(ComplimentaryPairs.random_array(30000)))', number=5, setup="from __main__ import ComplimentaryPairs"))
        print('40K     : ',
              timeit.timeit('ComplimentaryPairs.solution(0, list(ComplimentaryPairs.random_array(40000)))', number=5, setup="from __main__ import ComplimentaryPairs"))
        print('40K     : ', timeit.timeit('ComplimentaryPairs.solution(0, [2147483648]*40000)', number=5, setup="from __main__ import ComplimentaryPairs"))


class Fibonacci:
    def __init__(self):
        self.__mod = 1000000
        self.__first_who_have_six_digits = 26
        self.__period = 1500000
        self.__first_cheat_digit = self.__first_who_have_six_digits + self.__period

        self.__q_power = 1
        self.__q_martix = [[1, 1],
                           [1, 0]]

    @staticmethod
    def get_powers_of_2(digit):
        power = 1
        while power <= digit:
            if power & digit:
                yield power
            power <<= 1

    def __multiply_and_sum_by_modulo(self, a, b, c, d):
        return (a * b + c * d) % self.__mod

    def __multiply(self, m1, m2):
        return [
            [self.__multiply_and_sum_by_modulo(m1[0][0], m2[0][0], m1[0][1], m2[1][0]),
             self.__multiply_and_sum_by_modulo(m1[0][0], m2[0][1], m1[0][1], m2[1][1])],
            [self.__multiply_and_sum_by_modulo(m1[1][0], m2[0][0], m1[1][1], m2[1][0]),
             self.__multiply_and_sum_by_modulo(m1[1][0], m2[0][1], m1[1][1], m2[1][1])]]

    def __power_of_q(self, power):
        next_power = self.__q_power * 2

        while next_power <= power:
            self.__q_martix = self.__multiply(self.__q_martix, self.__q_martix)
            self.__q_power = next_power
            next_power *= 2

        return self.__q_martix

    def calculate(self, n):
        if n is None or n <= 0:
            return 0

        if n >= self.__first_cheat_digit:
            remainder = n % self.__period
            n = remainder if remainder > self.__first_cheat_digit else remainder + self.__period

        powers_of_2 = Fibonacci.get_powers_of_2(n)
        result_matrix = reduce(lambda x, y: self.__multiply(x, y),
                               map(lambda p: self.__power_of_q(p), powers_of_2))

        return result_matrix[0][1]

    @staticmethod
    def test_it():
        assert 0 == Fibonacci().calculate(-1)
        assert 0 == Fibonacci().calculate(None)
        assert 0 == Fibonacci().calculate(0)
        assert 1 == Fibonacci().calculate(1)
        assert 1 == Fibonacci().calculate(2)
        assert 2 == Fibonacci().calculate(3)
        assert 3 == Fibonacci().calculate(4)
        assert 5 == Fibonacci().calculate(5)
        assert 21 == Fibonacci().calculate(8)
        assert 46368 == Fibonacci().calculate(24)
        assert 75025 == Fibonacci().calculate(25)
        assert 121393 == Fibonacci().calculate(26)
        assert 196418 == Fibonacci().calculate(27)
        assert 930352 == Fibonacci().calculate(36)
        assert 546875 == Fibonacci().calculate(1000000)
        assert 121393 == Fibonacci().calculate(1500026)
        assert 453125 == Fibonacci().calculate(2000000)
        assert 937501 == Fibonacci().calculate(100000001)
        assert 484376 == Fibonacci().calculate(1000000002)

        print('100+1: ', timeit.timeit('Fibonacci().calculate(1000+1)', number=100, setup="from __main__ import Fibonacci"))
        print('1K+1: ', timeit.timeit('Fibonacci().calculate(1000+1)', number=100, setup="from __main__ import Fibonacci"))
        print('10K+1: ', timeit.timeit('Fibonacci().calculate(10000+1)', number=100, setup="from __main__ import Fibonacci"))
        print('100K+1: ', timeit.timeit('Fibonacci().calculate(100000+1)', number=100, setup="from __main__ import Fibonacci"))
        print('1M: ', timeit.timeit('Fibonacci().calculate(1000000)', number=100, setup="from __main__ import Fibonacci"))
        print('100M+1: ', timeit.timeit('Fibonacci().calculate(100000000+1)', number=100, setup="from __main__ import Fibonacci"))
        print('1G+2: ', timeit.timeit('Fibonacci().calculate(1000000*1000000+2)', number=100, setup="from __main__ import Fibonacci"))


def solution(N):
    return Fibonacci().calculate(N)


Fibonacci.test_it()

# print(solution(8))




# print(period(26))
# print(solution(0))
# print(solution(1))
# print(solution(8))

# for n in range(1000):
#     print(f(n))
# print(f(26))
# print(f(26+23))
# print(solution(36))
# print(solution(36 + 60))
# print(solution(61))
# print(solution(26))
# print(solution(85))
# print(f(85))
# print(solution(86))
# print(f(26))
# print(f(26 + 60))
# print(solution(27))
# print(solution(87))
# print(f(87))
# print(solution(2147483647))
# print(solution(8))

# print("start")
#
# print(better_solution(6, [3] * 100))
# print(better_solution(6, [2, 4] * 100))
# print(better_solution(6, [2, 4, 2] * 100))
# print(better_solution(6, [2, 4, 1, 5, 12, 3] * 100))

# print(solution(-2147483648, [-2147483648, -2147483648 / 2]))
# print(solution(-2147483648, []))
# print(solution(-2147483648, None))
# print(solution(-2147483648, [-2147483648] * 100000))

# print(solution([-1, 0]))
# print(solution([0, 0]))
# print(solution([1, 1]))
# print(solution([1, -1]))

# print(solution([]))
# print(solution(None))
# print(solution([-2147483648] * 100000))
# print(solution([2147483648]))

# []
# None
# [-2147483648] * 100000
# [0]
# [2147483648]
# [0, 1, -1]

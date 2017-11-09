import timeit
from functools import reduce


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
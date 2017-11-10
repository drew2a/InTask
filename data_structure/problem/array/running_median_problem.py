import random
from bisect import bisect_left


class RunningMediane:
    def __init__(self):
        self.__sorted = []

    def __str__(self):
        return str(self.__sorted)

    def add(self, value):
        self.__sorted.insert(bisect_left(self.__sorted, value), value)
        return self

    @staticmethod
    def scale(f):
        return int(f * 10) / 10

    def calculate(self):
        size = len(self.__sorted)
        if size == 0:
            return 0

        half = int(size / 2)
        if size % 2 != 0:
            return RunningMediane.scale(self.__sorted[half])
        return RunningMediane.scale((self.__sorted[half] + self.__sorted[half - 1]) / 2)

    @staticmethod
    def test_it():
        mediane = RunningMediane()

        for i in range(10):
            mediane.add(random.randint(0, 10))
        print(mediane)

        assert 1.0 == RunningMediane.scale(1)
        assert 1.5 == RunningMediane.scale(1.567)

        mediane = RunningMediane()
        assert 0 == mediane.calculate()
        assert 12 == mediane.add(12).calculate()
        assert 8.0 == mediane.add(4).calculate()
        assert 5.0 == mediane.add(5).calculate()
        assert 4.5 == mediane.add(3).calculate()
        assert 5.0 == mediane.add(8).calculate()
        assert 6.0 == mediane.add(7).calculate()

        mediane = RunningMediane()
        assert 1 == mediane.add(1).calculate()
        assert 1.5 == mediane.add(2).calculate()
        assert 2 == mediane.add(3).calculate()
        assert 2.5 == mediane.add(4).calculate()
        assert 3 == mediane.add(5).calculate()
        assert 3.5 == mediane.add(6).calculate()
        assert 4 == mediane.add(7).calculate()
        assert 4.5 == mediane.add(8).calculate()
        assert 5 == mediane.add(9).calculate()
        assert 5.5 == mediane.add(10).calculate()


RunningMediane.test_it()

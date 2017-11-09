import timeit
from random import randrange


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

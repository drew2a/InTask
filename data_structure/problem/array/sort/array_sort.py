import random
import timeit


def base_bubble_sort(a):
    for i in range(len(a)):
        for j in range(0, len(a) - i - 1):
            if a[j] < a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a


def optimised_bubble_sort(a):
    n = len(a)
    while n != 0:
        new_n = 0
        for i in range(1, n):
            if a[i - 1] < a[i]:
                a[i], a[i - 1] = a[i - 1], a[i]
                new_n = i
        n = new_n

    return a


def insertion_sort(a):
    for i in range(len(a)):
        j = i
        while j > 0 and a[j - 1] < a[j]:
            a[j], a[j - 1] = a[j - 1], a[j]
            j -= 1

    return a


def quick_sort_partition(a, lo, hi):
    pivot = a[lo]
    i = lo + 1
    j = hi
    while True:
        while i <= j and a[i] >= pivot:
            i += 1
        while i <= j and a[j] <= pivot:
            j -= 1
        if j < i:
            a[lo], a[j] = a[j], a[lo]
            return j
        a[i], a[j] = a[j], a[i]


def quick_sort(lo, hi, a):
    if lo < hi:
        p = quick_sort_partition(a, lo, hi)
        quick_sort(lo, p - 1, a)
        quick_sort(p + 1, hi, a)
    return a


_experiment_count = 5
_small_array_size = 10
_big_array_size = 1000

_small_array = [random.randrange(_small_array_size) for _ in range(_small_array_size)]
_big_array = [random.randrange(_big_array_size) for _ in range(_big_array_size)]
_line = '-' * 100
print('Given array: {}'.format(_small_array))
print(_line)
print('Base Bubble sort: {}'.format(base_bubble_sort(_small_array[:])))
print('Base Bubble sort: ', timeit.timeit('base_bubble_sort(list(_big_array))', number=_experiment_count, setup="from __main__ import base_bubble_sort,_big_array"))
print(_line)
print('Optimized Bubble sort: {}'.format(optimised_bubble_sort(_small_array[:])))
print('Optimized Bubble sort: ', timeit.timeit('optimised_bubble_sort(list(_big_array))', number=_experiment_count, setup="from __main__ import optimised_bubble_sort,_big_array"))
print(_line)
print('Insertion sort: {}'.format(insertion_sort(_small_array[:])))
print('Insertion sort: ', timeit.timeit('insertion_sort(list(_big_array))', number=_experiment_count, setup="from __main__ import insertion_sort,_big_array"))
print(_line)
print('Quick sort: {}'.format(quick_sort(0, len(_small_array) - 1, _small_array[:])))
print('Quick sort: ', timeit.timeit('quick_sort(0, len(_big_array)-1, list(_big_array))', number=_experiment_count, setup="from __main__ import quick_sort,_big_array"))
print(_line)

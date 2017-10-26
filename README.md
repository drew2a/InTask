# Summary
My implementation of a several programming tasks from interview.

All examples: ![main.py](main.py)

# Matrices
## Spiral/snail matrix
Example of how to create matrix like this: <br>
9 8 7 <br>
2 1 6 <br>
3 4 5 
```python
def create_snail_matrix(size):
```
<br>Source: ![matrix_tasks.py](task/matrix_tasks.py)

# Arrays

## Google problem with bars:
How many water given bars will collect?
```python
# array = [1, 2, 0, 1, 3, 1]
# Answer: 3
#
#|  |  |  |  |oo|  |
#|  |oo|~~|~~|oo|  |
#|oo|oo|~~|oo|oo|oo|
#  0  1  2  3  4  5 

def find_water_count(array):
```
<br>Source: ![array_tasks.py](task/array_tasks.py)

## Pairs
Find a pair of elements from an array whose sum equals a given number:
```python
# array = [8, 0, 6, 6, 9, 4, 1, 4, 9, 3, 9, 1, 0, 4, 2, 6, 5, 7, 5, 6]
# value = 10
# answer: [(4, 6), (9, 1), (5, 5), (6, 4)]
def find_pairs(array, value):
```
<br>Source: ![array_tasks.py](task/array_tasks.py)

## Left rotation
Example of a left rotation operation on an array: 
```python
# a = [1, 2, 3, 4, 5]
# k = 2
# answer: [3, 4, 5, 1, 2]
def array_left_rotation(a, k):
```
<br>Source: ![array_tasks.py](task/array_tasks.py)

## Sub array with max sum
How to find sub array with max sum: 
```python
# given array = [1, 2, -2, -3, 0, 0, 9, -1, 5, 2]
# answer: [9, -1, 5, 2]
def max_sum_sub_array(given_array):
```
<br>Source: ![array_tasks.py](task/array_tasks.py)

# Sequences
## Print numbers can be divided by 3 and can not be divided by 5...
Example how to find numbers can be divided by 3 and can not be divided by 5.
Sum of all digits in each number is less than 10.
```python
# n=40
# answer: [3, 6, 9, 12, 18, 21, 24, 27, 33, 36]
def create_3_5_10_array(n):
```
<br>Source: ![sequence_tasks.py](task/sequence_tasks.py)

## Find primes
Example how to find prime numbers with the sieve of eratosthenes:
```python
# n=50
# sort=True
# answer: [1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
def sieve_of_eratosthenes(n, sort=False):
```
<br>Source: ![sequence_tasks.py](task/sequence_tasks.py)


# Trees
## Binary search tree
Check is this a binary search tree:
```python
# root = 8(4(2(1(None, None), 3(None, None)), 6(None, None)), 13(10(None, None), 14(None, None)))
# answer: True
def check_binary_search_tree(root):
```
<br>Source: ![tree_tasks.py](task/tree_tasks.py)

# Strings
## Anagram
Check for anagrams (case sensitive)
```python
# s1 = one
# s2 = eon
# answer: True
def check(s1, s2):
```
<br>Source: ![string_tasks.py](task/string_tasks.py)

# sql
# group by with having clause
Select all departments with conditions:
1. All computers in a department have ram>=8
2. A department have only  MAC's
<br>Source: ![select.sql](database/task/select.sql)

## Screenshot
![screenshot](screenshot.jpg)
from data_structure.problem import array_problems
from data_structure.problem import string_problems
from data_structure.problem.matrix import matrix_problems
from data_structure.problem.sequence import sequence_problems
from data_structure.problem.tree import tree_problems

# snail/spiral matrix

_matrix_size = 5
_matrix = matrix_problems.create_snail_matrix(_matrix_size)

print("\n\nSpiral matrix({}):".format(_matrix_size))
matrix_problems.print_matrix(_matrix)

# tuples in array
_sum = 10
_list = list(array_problems.random_array(20))
_pairs = array_problems.find_pairs(_list, _sum)

print("\n\nArray: " + str(_list))
print("Pairs (with sum {}): {}".format(_sum, _pairs))

_list = [1, 2, 3, 4, 5]
print("\n\n{:<25}{}".format("Array:", _list))
print("{:<25}{}".format("Left rotated array (2):", list(array_problems.array_left_rotation(_list, 2))))

print("\n\nPrint numbers can be divided by 3 and can not be divided by 5. Sum of all digits in a number is less than 10:")
print(list(sequence_problems.create_3_5_10_array(40)))

print("\n\nSieve of eratosthenes:")
print(list(sequence_problems.sieve_of_eratosthenes(50)))

_list = [1, 2, -2, -3, 0, 0, 9, -1, 5, 2]
print('\n\nArray: {}'.format(_list))
print('Subarray with max sum: {}\n'.format(list(array_problems.max_sum_sub_array(_list))))

# anagram
_examples = [("one", "two"),
             ("one", "eon"),
             ("one", "one")]

print('\n\nIs anagram: ')
print('\n'.join('{}'.format((e[0], e[1], string_problems.check(e[0], e[1]))) for e in _examples))

print('\n\nFirst not recurring character(ABACDBCEAB): ', string_problems.find_first_not_recurring_character('ABACDBCEAB'))

# tree
_tree = tree_problems.create_sample_tree()
print('\n\nTree: ' + str(_tree))
print('Is binary search tree? ' + str(tree_problems.check_binary_search_tree(_tree)))
print('Lowest common ancestor of (16, 6) is ', tree_problems.get_lowest_common_ancestor(_tree, 16, 6))
print('Lowest common ancestor of (6, 1) is ', tree_problems.get_lowest_common_ancestor(_tree, 6, 1))

print('\n\n\n')
print('\nWater: {}\n\n--------------------------------------------\n\n'.format(array_problems.find_water_count([1, 2, 0, 1, 3, 1])))
print('\nWater: {}\n\n--------------------------------------------\n\n'.format(array_problems.find_water_count([0, 1, 2, 1, 2, 3, 4, 3, 4, 1, 1, 8, 1, 2, 4, 3, 5])))
print('\nWater: {}\n\n--------------------------------------------\n\n'.format(array_problems.find_water_count([5, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 4])))

from task import string_tasks, array_tasks, matrix_tasks, tree_tasks

# snail/spiral matrix
_matrix_size = 5
_matrix = matrix_tasks.create_snail_matrix(_matrix_size)

print("\n\nSpiral matrix({}):".format(_matrix_size))
matrix_tasks.print_matrix(_matrix)

# tuples in array
_sum = 10
_list = list(array_tasks.random_array(20))
_pairs = array_tasks.find_pairs(_list, _sum)

print("\n\nArray: " + str(_list))
print("Pairs (with sum {}): {}".format(_sum, _pairs))

_list = [1, 2, 3, 4, 5]
print("\n\n{:<25}{}".format("Array:", _list))
print("{:<25}{}".format("Left rotated array (2):", list(array_tasks.array_left_rotation(_list, 2))))

# anagram
_examples = [("one", "two"),
             ("one", "eon"),
             ("one", "one")]

print('\n\nIs anagram: ')
print('\n'.join('{}'.format((e[0], e[1], string_tasks.check(e[0], e[1]))) for e in _examples))

# tree
_tree = tree_tasks.create_sample_tree()
print('\n\nTree: ' + str(_tree))
print('Is binary search tree? ' + str(tree_tasks.check_binary_search_tree(_tree)))

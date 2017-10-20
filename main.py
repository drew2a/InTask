from task import string_tasks, array_tasks, matrix_tasks

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

# anagram
_examples = [("one", "two"),
             ("one", "eon"),
             ("one", "one")]

print('\n\nIs anagram: ')
print('\n'.join('{}'.format((e[0], e[1], string_tasks.check(e[0], e[1]))) for e in _examples))

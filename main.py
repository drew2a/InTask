import anagram
import snail
import tuples_in_array

# snail/spiral matrix
_matrix_size = 5
_matrix = snail.create_snail_matrix(_matrix_size)

print("\n\nSpiral matrix({}):".format(_matrix_size))
snail.print_matrix(_matrix)

# tuples in array
_sum = 10
_list = list(tuples_in_array.random_array(20))
_tuples = tuples_in_array.find_tuples(_list, _sum)

print("\n\nArray: " + str(_list))
print("Tuples (with sum {}): {}".format(_sum, _tuples))

# anagram
_examples = [("one", "two"),
             ("one", "eon"),
             ("one", "one")]

print('\n\nIs anagram: ')
print('\n'.join('{}'.format((e[0], e[1], anagram.check(e[0], e[1]))) for e in _examples))

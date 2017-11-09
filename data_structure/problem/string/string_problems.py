from collections import defaultdict


def check(s1, s2):
    if len(s1) != len(s2):
        return False

    s1_stamp = defaultdict(int)
    for ch in s1:
        s1_stamp[ch] += 1
    for ch in s2:
        s1_stamp[ch] -= 1

    return all(i == 0 for i in s1_stamp.values())


def find_first_not_recurring_character(s):
    if s is None:
        return ''

    chars = defaultdict(int)
    for char in s:
        chars[char] += 1
    for key in chars.keys():
        if chars[key] == 1:
            return key

    return ''


def number_needed(a, b):
    dictionary = defaultdict(int)
    for ch in a:
        dictionary[ch] += 1
    for ch in b:
        dictionary[ch] -= 1

    return sum(map(lambda item: abs(item), dictionary.values()))


def is_balanced(expression):
    stack = ['']
    pairs = {']': '[',
             ')': '(',
             '}': '{'}

    for bracket in expression:
        if bracket not in pairs:
            stack.append(bracket)
            continue

        if pairs[bracket] == stack[-1]:
            stack.pop()
        else:
            return False

    return len(stack) == 1

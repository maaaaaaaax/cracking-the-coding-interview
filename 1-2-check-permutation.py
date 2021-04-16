# 1.2 Check Permutation

# Given two strings, write a method to decide if one is a permutation of the other.


# Solution 1: Sort the strings, and compare equality.

def is_permutation_1(string_1, string_2):
    if len(string_1) != len(string_2):
        return False
    sorted_1 = ''.join(sorted(string_1))
    sorted_2 = ''.join(sorted(string_2))
    return sorted_1 == sorted_2

print(is_permutation_1('ate', 'tea')) # True
print(is_permutation_1('cat', 'dog')) # False


# Solution 2: Check whether the character counts of each string are equal

def is_permutation_2(string_1, string_2):
    if len(string_1) != len(string_2):
        return False
    seen = {}
    for c in string_1:
        if c in seen:
            seen[c] += 1
        else:
            seen[c] = 1
    for s in string_2:
        if s not in seen:
            return False
        else:
            seen[s] -= 1
            if seen[s] < 0:
                return False
    return True

print(is_permutation_2('ate', 'tea')) # True
print(is_permutation_2('cat', 'dog')) # False
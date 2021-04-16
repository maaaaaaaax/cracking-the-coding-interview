#  1.4 Palindrome Permutation

#  Given a string, write a function to check if it is a permutation of a palindrome. 
#  A palindrome is a word or phrase that is the same forwards and backwords. 
#  A permutation is a rearrangement of letters.
#  A palindrome does not need to be limited to just dictionary words.

def is_palindrome_permutation(string):

    # Let's assume that palindromes must be at least three characters long.
    length = len(string)
    if length <= 2:
        return False

    # Count the frequency of characters in a string.
    seen = {}
    for c in string:
        if c in seen:
            seen[c] += 1
        else:
            seen[c] = 1

    # If a palindrome has an even length, all characters must occur an even number of times.
    if length % 2 == 0:
        for char in seen:
            if seen[char] % 2 != 0:
                return False
        return True

    # If a palindrome is an odd length, one character must occur an odd number of times, 
    # while all other characters must occur an even number of times.
    if length % 2 == 1:
        odd_frequency_seen = False
        for char in seen:
            if seen[char] % 2 != 0:
                if odd_frequency_seen:
                    return False
                else:
                    odd_frequency_seen = True
        if not odd_frequency_seen:
            return False
        else:
            return True

print(is_palindrome_permutation('deed'))  # True
print(is_palindrome_permutation('civic'))  # True
print(is_palindrome_permutation('Max Wiederholt'))  # False
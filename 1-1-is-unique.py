# 1.1 Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?

# Use a set to keep track of which characters we've seen. O(1) runtime. O(N) space complexity.

def is_unique(string):
    seen = set()
    for char in string:
        if char in seen:
            return False
        else:
            seen.add(char)
    return True

print(is_unique('hello')) # False
print(is_unique('world')) # True
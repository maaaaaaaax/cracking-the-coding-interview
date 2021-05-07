#  1.9 String Rotation

#  Assume you have a method isSubstring which checks if one word is a substring of another. 
#  Given two strings, s1 and s2, write code to check if s2 is a rotation of s1 using only one call to isSubstring.
#  E.g., "waterbottle" is a rotation of "erbottlewat".

def is_string_rotation(s1, s2):
    if len(s1) != len(s2):
        return False
    s1_repeated = s1 + s1
    if s2 in s1_repeated:
        return True
    else:
        return False

print(is_string_rotation("waterbottle", "erbottlewat"))  # True
print(is_string_rotation("waterbottle", "erbottlewa"))  # False
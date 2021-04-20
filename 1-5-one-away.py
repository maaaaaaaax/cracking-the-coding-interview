# 1.5 One Away

# There are three types of edits that can be performed on strings: 
# insert a character, remove a character, or replace a character. 
# Given two strings, write a function to check if they are one edit (or zero edits) away.

def one_away(string_1, string_2):
    if string_1 == string_2:
        return True
    # Check if inserting a character creates equality
    if one_insert_away(string_1, string_2):
        return True
    # Check if removing a character creates equality
    if one_removal_away(string_1, string_2):
        return True   
    # Check if replaceing a character creates equality
    if one_replacement_away(string_1, string_2):
        return True                
    return False

def one_insert_away(string_1, string_2):
    if (len(string_1) + 1) != len(string_2):
        return False
    index_1 = 0
    index_2 = 0
    for i in range(len(string_1)):
        if string_1[index_1] != string_2[index_2]:
            index_2 += 1
            if index_2 - index_1 > 1:
                return False
        else:
            index_1 += 1
            index_2 += 1
    return True

def one_removal_away(string_1, string_2):
    if (len(string_1) - 1) != len(string_2):
        return False
    index_1 = 0
    index_2 = 0
    for i in range(len(string_2)):
        if string_1[index_1] != string_2[index_2]:
            index_1 += 1
            if index_1 - index_2 > 1:
                return False
        else:
            index_1 += 1
            index_2 += 1
    return True

def one_replacement_away(string_1, string_2):
    if len(string_1) != len(string_2):
        return False
    replaced = False
    for i in range(len(string_2)):
        if string_1[i] != string_2[i]:
            if replaced:
                return False
            replaced = True
    return True
    
print(one_away('hello', 'hello'))  # True
print(one_away('hell', 'hello'))  # True
print(one_away('hello', 'hell'))  # True
print(one_away('hello', 'heldo'))  # True
print(one_away('h', 'hello'))  # False
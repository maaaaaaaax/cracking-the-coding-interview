# 1.5 One Away

# There are three types of edits that can be performed on strings: insert a character, remove a character, or replace a character. Given two strings, write a function to check if they are one edit (or zero edits) away.

def one_away(string_1, string_2):
    if string_1 == string_2:
        return True
    # Check if inserting a character creates equality
    if one_insert_away(string_1, string_2):
        return True
    return False

def one_insert_away(string_1, string_2):
    # TO DO
    return False    

print(one_away('hello', 'hello'))
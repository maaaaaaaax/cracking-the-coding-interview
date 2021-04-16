#  1.3 URLify

#  Write a method that replaces all spaces in a string with '%20'. 
# You may assume that the string has sufficient space at the end to hold the additional characters, and that you are given the length of the string.

def urlify(string):
    stripped = string.strip()
    url = ''
    for c in stripped:
        if c == ' ':
            url += '%20'
        else:
            url += c
    return url

print(urlify("Mr John Smith    "))  #  Mr%20John%20Smith
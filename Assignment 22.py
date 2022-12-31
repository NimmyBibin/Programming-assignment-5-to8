"""
Question1
Create a function that takes three parameters where:
 x is the start of the range (inclusive).
 y is the end of the range (inclusive).
 n is the divisor to be checked against.
Return an ordered list with numbers in the range that are divisible by the third parameter n.
Return an empty list if there are no numbers that are divisible by n.
"""
def list_operation(x, y, n):
    divisor = []
    nonDiv = []
    for i in range(x, y + 1):
        if i % n == 0:
            divisor.append(i)
    return divisor
print(list_operation(1, 10, 3))
"""
Question2
Create a function that takes in two lists and returns True if the second list follows the first list
by one element, and False otherwise. In other words, determine if the second list is the first
list shifted to the right by 1.
"""
def simon_says(ls,ls2):
    if ls[0:len(ls)-1] == ls2[1:len(ls2)]:
        return True
    return False
print(simon_says([1, 2],[5, 1]))
print(simon_says([1, 2],[5, 5]))

"""
Question3
A group of friends have decided to start a secret society. The name will be the first letter of each of their names, sorted in alphabetical order.
Create a function that takes in a list of names and returns the name of the secret society.
"""
def society_name(lst):
    return ''.join([i[0] for i in sorted(lst)])
print(society_name(['Adam', 'Sarah', 'Malcolm']))

"""
Question4
An isogram is a word that has no duplicate letters. Create a function that takes a string and
returns either True or False depending on whether or not it's an 'isogram'.
Examples
is_isogram('Algorism') ➞ True
is_isogram('PasSword') ➞ False
# Not case sensitive.
is_isogram('Consecutive') ➞ False
"""

def is_isogram(s):
    for i in range(len(s)):
        if s.lower().count(s[i]) > 1:
            return False
    else:
        return True
print(is_isogram('Algorism'))
print(is_isogram('AmmA'))
"""
Question5
Create a function that takes a string and returns True or False, depending on whether the
characters are in order or not.
"""
def is_in_order(s):
    n = len(s)
    c = [s[i] for i in range(len(s))]
    c.sort()
    for i in range(n):
        if c[i] != s[i]:
            return False
    return True
print(is_in_order('abc'))

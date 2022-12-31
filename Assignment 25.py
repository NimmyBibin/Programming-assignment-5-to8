"""
Question1
Create a function that takes three integer arguments (a, b, c) and returns the amount of integers which are of equal value.

"""
def equal(a,b,c):
    num = 0
    if a == b and a == c :
        num = 3
    elif a == b or a == c :
        num = 2
    else:
        num = 0
    return num
print(equal(3, 4, 3))
Question2def dict_to_list(d):
    return list(d.items())
"""
Write a function that converts a dictionary into a list of keys-values tuples.
"""
def dict_to_list(d):
    return list(d.items())
print(dict_to_list({
    'D': 1,
    'B': 2,
    'C': 3
    }))
"""
Question3
Write a function that creates a dictionary with each (key, value) pair being the (lower case,
upper case) versions of a letter, respectively.
"""
def mapping(lst):
    return {v.lower():v.upper() for v in lst}
print(mapping(['p', 's']))
"""
Question4
Write a function, that replaces all vowels in a string with a specified vowel.
"""
def vow_replace(s,ch):
    vowel ='AEIOUaeiuo'
    s1 = []
    for i in range(len(s)):
        if s[i] in vowel:
            s1.append(ch)
        else:
            s1.append(s[i])

    return ''.join((s1))
print(vow_replace('apples and bananas', 'u'))


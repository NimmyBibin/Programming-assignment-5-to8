"""
Question1
Create a function that takes a string and returns a string in which each character is repeated once.
"""

def double(str):
    return ''.join([c+c for c in str])
print(double('string'))
"""
Question2
Create a function that reverses a boolean value and returns the string "boolean expected" if another variable type is given.

"""
def reverse(arg=None):
    return not arg if type(arg) == bool else "boolean expected"

print(reverse(True)) # False
print(reverse(False)) # True
print(reverse(0)) # "boolean expected"
print(reverse(None)) # "boolean expected"
"""
Question3
Create a function that returns the thickness (in meters) of a piece of paper after folding it n number of times. The paper starts off with a thickness of 0.5mm.

""""""


def num_layers(n):
    thickness = 0.5
    for  i in range(n):
        thickness *= 2

    return str(thickness / 1000) + 'm'  # for meters


print(num_layers(1))
print(num_layers(4))
print(num_layers(21))
"""
Question4
Create a function that takes a single string as argument and returns an ordered list containing the indices of all capital letters in the string.
"""
def index_of_caps(word):
    indices = []
    for i in range(len(word)):
        if word[i].isupper():
             indices.append(i)
    return indices

print(index_of_caps('BhaVYa'))
"""
Question5
Using list comprehensions, create a function that finds all even numbers from 1 to the given
number.
"""
def find_even_nums(n):
    even =[x for x in range(2,n+1) if x % 2 == 0]
    return even

n = int(input('Enter a number : '))
find_even_nums(n)




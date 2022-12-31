"""
Question1
Create a function that takes a list of strings and integers, and filters out the list so that it
returns a list of integers only.
"""
lst = [1, 2, 3, 'a', 'b', 4]
def filter_list(lst):
    intLst = []
    for i in lst:
        if type(i) == int:
            intLst.append(i)
    return intLst
print(filter_list([1, 2, 3, 'a', 'b', 4]))
"""
Question2
Given a list of numbers, create a function which returns the list but with each element's index in the list added to itself. This means you add 0 to the number at index 0, add 1 to the number at index 1, etc...
"""
def add_indexes(lst):
    ind = 0
    index = []
    for i in lst:
        index.append(lst.index(i,ind) + i)
        ind+=1
    return index
print(add_indexes([0, 0, 0, 0, 0]))
"""
Question3
Create a function that takes the height and radius of a cone as arguments and returns the
volume of the cone rounded to the nearest hundredth. See the resources tab for the formula.

"""
import math
pi = math.pi
# Function to calculate Volume of Cone
def cone_volume(r, h):
    return round((1 / 3) * pi * r * r * h)
radius = float(input("enter the radius of cone:"))
height = float(input("enter height of the cone: "))
print("Volume Of Cone : ", cone_volume(radius, height))
print(cone_volume(3, 2))
"""
Question4
This Triangular Number Sequence is generated from a pattern of dots that form a triangle.
The first 5 numbers of the sequence, or dots, are:
1, 3, 6, 10, 15
This means that the first triangle has just one dot, the second one has three dots, the third one
has 6 dots and so on.
Write a function that gives the number of dots with its corresponding triangle number of the
sequence.
"""
def triangle(n):
    return n*(n+1)*0.5

n = int(input('Enter the trinalge number :'))
print("The {}th triangle has {} dots ".format(n,int(triangle(n))))

#print(triangle(215))
"""
Question5
Create a function that takes a list of numbers between 1 and 10 (excluding one number) and
returns the missing number.
"""
def missing_num(lst):
    total = sum([x for x in range(11)])
    sum_Of_list = sum(lst)
    return total - sum_Of_list

print(missing_num([1, 2, 3, 4, 6, 7, 8, 9, 10]))


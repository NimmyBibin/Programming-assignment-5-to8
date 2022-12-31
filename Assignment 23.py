"""
Question 1
Create a function that takes a number as an argument and returns True or False depending
on whether the number is symmetrical or not. A number is symmetrical when it is the same as
its reverse.
"""
def is_symmetrical_num(n):
  return str(n) == str(n)[::-1]
print(is_symmetrical_num(121))
print(is_symmetrical_num(0))
print(is_symmetrical_num(122))
"""
Question 2
Given a string of numbers separated by a comma and space, return the product of the numbers.
"""
def multiply_nums(s):
    s = s.replace(' ', "")
    s = s.split(',')
    sum = 1
    for i in s:
        sum = sum * int(i)
    return sum

print(multiply_nums('2, 3'))
"""
Question 3
Create a function that squares every digit of a number.
"""
def square_digits(num):
    z = ''.join(str(int(i)**2) for i in str(num))
    return int(z)
print(square_digits(9119))

"""
Question 4
Create a function that sorts a list and removes all duplicate items from it.
"""
def setify(lst):
    return list(set(lst))
print(setify([1, 3, 3, 5, 5]))
"""
Question 5
Create a function that returns the mean of all digits.
"""


def mean(n):
    N = len(str(n))
    sum = mean = 0

    for digit in str(n):
        sum += int(digit)
    return int(sum / N)
print(mean(24))
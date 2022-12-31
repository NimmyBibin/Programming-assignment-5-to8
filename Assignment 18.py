"""
#Question1. Create a function that takes three arguments a, b, c and returns the sum of the numbers that are evenly divided by c from the range a, b inclusive.
l = [1, 2, 'aasf', '1', '123', 123]

def filter_list(l):
    new_list = []
    for x in l:
        if type(x) == int:
            new_list.append(x)
    return new_list

print(filter_list(l))

#Question 2:The "Reverser" takes a string as input and returns that string in reverse order, with the opposite case.
def reverse(str):
    str = str[::-1]
    return str.swapcase()


print(reverse('ReVeRsE'))

Q3,You can assign variables from lists like this:
lst = [1, 2, 3, 4, 5, 6]
first = lst[0]
middle = lst[1:-1]
last = lst[-1]

print(first) ➞ outputs 1
print(middle) ➞ outputs [2, 3, 4, 5]
print(last) ➞ outputs 6
With Python 3, you can assign variables from lists in a much more succinct way. Create variables first, middle and last from the given list using destructuring assignment (check the Resources tab for some examples), where:
first  ➞ 1

middle➞ [2, 3, 4, 5]

last➞ 6
Your task is to unpack the list writeyourcodehere into three variables, being first, middle, and last, with middle being everything in between the first and last element. Then print all three variables.

lst = [1, 2, 3, 4, 5, 6]
first ,*middle,last = lst
print(first)
print(last)
print(middle)

Question 4
Write a function that calculates the factorial of a number recursively.


def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

num = int(input('enter a number :'))
print("Factorial of", num, "is", factorial(num))

Question 5
Write a function that moves all elements of one type to the end of the list.
"""


def move_to_end(array, toMove):
    i = 0

    # Mark the right pointer
    j = len(array) - 1

    # Iterate untill left pointer
    # crosses the right pointer
    while (i < j):

        while (i < j and array[j] == toMove):
            # decrement right pointer
            j -= 1

        if (array[i] == toMove):
            # swap the two elements
            # in the array
            array[i], array[j] = array[j], array[i]

        # increment left pointer
        i += 1

    # return the result
    return array
arr = [7, 8, 9, 1, 2, 3, 4]
k = 9
ans = move_to_end(arr, k)
for i in range(len(arr)):
    print(ans[i] ,end= " ")
"""
arr = ['a', 'a', 'a', 'b']
k = 'a'
ans = move_to_end(arr, k)
for i in range(len(arr)):
    print(ans[i] ,end= " ")
"""
"""
Question 5
Write a function that moves all elements of one type to the end of the list.
"""
def move_to_end(lst,el):
    lst.append(lst.pop(lst.index(el)))
    return lst

print(move_to_end([1, 3, 2, 4, 4,], 1))
print(move_to_end([7, 8, 9, 1, 2, 3, 4], 9))
print(move_to_end(["a","a","a","b"], "a"))


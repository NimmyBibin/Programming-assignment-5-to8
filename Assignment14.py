""""
Question 1:

Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.


def divChecker(n):
    for i in range(n):
        if i % 7 == 0:
            value = True
        else:
            value = False
        print(i, value)

divChecker(20)

Question 2:
Write a program to compute the frequency of the words from the input. The output should output after sorting the key alphanumerically. 

Suppose the following input is supplied to the program:

New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.

Then, the output should be:

2:2

3.:1

3?:1

New:1

Python:5

Read:1

and:1

between:1

choosing:1

or:2

to:1
import operator

text_line = input("Type in: ")

freq_dict = {}

for i in text_line.split(' '):
    if i.isalpha():
        if i not in freq_dict:
            freq_dict[i] = 1
        elif i in freq_dict:
            freq_dict[i] = freq_dict[i] + 1
    else:
        pass

sorted_freq_dict = sorted(freq_dict.items(), key = operator.itemgetter(0))
print(sorted_freq_dict)

for i in sorted_freq_dict:
    print(i[0], i[1])

Question 3:
Define a class Person and its two child classes: Male and Female. All classes have a method "getGender" which can print "Male" for Male class and "Female" for Female class.


class Person(object):
    def __init__(self):
        self.gender ="unknown"

    def getGender(self):
        print(self.gender)

class Male(Person):
    def __init__(self):
        self.gender = "Male"

class Female(Person):
    def __init__(self):
        self.gender = "Female"

nimmy = Female()
aibel = Male()
nimmy.getGender()
aibel.getGender()

Question 4:
Please write a program to generate all sentences where subject is in ["I", "You"] and verb is in ["Play", "Love"] and the object is in ["Hockey","Football"].


subjects=["I", "You"]
verbs=["Play", "Love"]
objects=["Hockey","Football"]
for i in range(len(subjects)):
    for j in range(len(verbs)):
        for k in range(len(objects)):
            sentence = "%s %s %s." % (subjects[i], verbs[j], objects[k])
            print(sentence)

Question 5:
Please write a program to compress and decompress the string "hello world!helloworld!helloworld!hello world!".

import zlib
s = 'hello world!hello world!hello world!hello world!'
# In Python 3 zlib.compress() accepts only DataType <bytes>
y = bytes(s, 'utf-8')
x = zlib.compress(y)
print(x)
print(zlib.decompress(x))


Question 6:
Please write a binary search function which searches an item in a sorted list. The function should return the index of element to be searched in the list.
"""

def binary_search_Ascending(array, target):
    lower = 0
    upper = len(array)
    print('Array Length:',upper)
    while lower < upper:
        x = (lower + upper) // 2
        print('Middle Value:',x)
        value = array[x]
        if target == value:
            return x
        elif target > value:
            lower = x
        elif target < value:
            upper = x

Array = [1,5,8,10,12,13,55,66,73,78,82,85,88,99]
print('The Value Found at Index:',binary_search_Ascending(Array, 82))
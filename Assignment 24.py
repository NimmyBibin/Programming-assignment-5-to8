"""
Question1
Create a function that takes an integer and returns a list from 1 to the given number, where:
1. If the number can be divided evenly by 4, amplify it by 10 (i.e. return 10 times the
number).
2. If the number cannot be divided evenly by 4, simply return the number.
"""
def amplify(n):
    return [i*10 if i % 4 == 0 else i for i in range(1,n+1) ]
print(amplify(8))
"""
Question2
Create a function that takes a list of numbers and return the number that's unique.
"""
def unique(lst):
    s = list(set(lst))# give us unique value
    for i in s:
        if lst.count(i) == 1:
            return i
print(unique([3, 3, 3, 7, 3, 3]))
"""
Question3
Your task is to create a Circle constructor that creates a circle with a radius provided by an
argument. The circles constructed must have two getters getArea() (PIr^2) and
getPerimeter() (2PI*r) which give both respective areas and perimeter (circumference).

For help with this class, I have provided you with a Rectangle constructor which you can use
as a base example.

"""

class Circle():
    def __init__(self, r):
        self.radius = r

    def getArea(self):
        return round(self.radius ** 2 * 3.14)

    def getPerimeter(self):
        return round(2 * self.radius * 3.14)
circy = Circle(11)
print(circy.getArea())
print(circy.getPerimeter())
"""
Question4
Create a function that takes a list of strings and return a list, sorted from shortest to longest.
Examples
sort_by_length(['Google', 'Apple', 'Microsoft'])
➞ ['Apple', 'Google', 'Microsoft']
sort_by_length(['Leonardo', 'Michelangelo', 'Raphael', 'Donatello'])
➞ ['Raphael', 'Leonardo', 'Donatello', 'Michelangelo']
sort_by_length(['Turing', 'Einstein', 'Jung'])
➞ ['Jung', 'Turing', 'Einstein']
Notes
All test cases contain lists with strings of different lengths, so you won't have to deal with
multiple strings of the same length.
"""

def sort_by_length(lst):
    return sorted(lst, key = len)
print(sort_by_length(['Google', 'Apple', 'Microsoft']))
"""
Question5
Create a function that validates whether three given integers form a Pythagorean triplet. The
sum of the squares of the two smallest integers must equal the square of the largest number to
be validated.

"""

def is_triplet(a,b,c):
    lst = []
    lst.extend((a,b,c))
    lst = sorted(lst)

    if lst[0]**2 + lst[1]**2 == lst[2]**2:
        print('Triplets')
        return True
    else:
        print("not triplet")
        return False
print(is_triplet(3, 4, 5))
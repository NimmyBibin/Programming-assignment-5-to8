
"""
Question 1:
Please write a program using generator to print the numbers which can be divisible by 5 and 7 between 0 and n in comma separated form while n is input by console.
Example:
If the following n is given as input to the program:
100
Then, the output of the program should be:
0,35,70


def NumGenerator(n):
    for i in range(n+1):
        if i%5==0 and i%7==0:
            yield i
n=int(input("enter the value of n:"))
values = []
for i in NumGenerator(n):
    values.append(str(i))
print(",".join(values))


Question 2:
Please write a program using generator to print the even numbers between 0 and n in comma separated form while n is input by console.
Example:
If the following n is given as input to the program:
10
Then, the output of the program should be:
0,2,4,6,8,10

def EvenGenerator(n):
    i=0
    while i<=n:
        if i%2==0:
            yield i
        i+=1


n=int(input("enter the numberer n:"))

values = []
for i in EvenGenerator(n):
    values.append(str(i))

The Fibonacci Sequence is computed based on the following formula:
f(n)=0 if n=0
f(n)=1 if n=1
f(n)=f(n-1)+f(n-2) if n>1
Please write a program using list comprehension to print the Fibonacci Sequence in comma separated form with a given n input by console.
Example:
If the following n is given as input to the program:
7

Then, the output of the program should be:
0,1,1,2,3,5,8,13


def f(n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return f(n-1)+f(n-2)

n=int(input("enter the number n:"))
print(f(n))


Question 4:
Assuming that we have some email addresses in the "username@companyname.com" format, please write program to print the user name of a given email address. Both user names and company names are composed of letters only.
Example:
If the following email address is given as input to the program:
john@google.com
Then, the output of the program should be:
john


import re
emailAddress =input("enter the  email address:")

pat2 = "(\w+)@(\w+)\.(com)"
r2 = re.match(pat2,emailAddress)
print( r2.group(1))


Question 5:
Define a class named Shape and its subclass Square. The Square class has an init function which takes a length as argument. Both classes have a area function which can print the area of the shape where Shape's area is 0 by default.
"""
class Shape():
    def __init__(self):
        pass

    def area(self):
        return 0

class Square(Shape):
    def __init__(self,length = 0):
        Shape.__init__(self)
        self.length = length

    def area(self):
        return self.length*self.length

Asqr = Square(5)
print(Asqr.area())

print(Square().area())
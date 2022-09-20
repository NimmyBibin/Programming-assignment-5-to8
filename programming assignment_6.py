
# Write a Python Program to Display Fibonacci Sequence Using Recursion?
def recur_fibo(n):
    if n<=1:
        return n
    else:
        return (recur_fibo(n - 1) + recur_fibo(n - 2))

nterms=10
if nterms <= 0:
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(nterms):
       print(recur_fibo(i))


#2.	Write a Python Program to Find Factorial of Number Using Recursion?
# Factorial of a number using recursion

def recur_factorial(n):
   if n == 1:
       return n
   else:
       return n*recur_factorial(n-1)

num = 7

# check if the number is negative
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   print("The factorial of", num, "is", recur_factorial(num))

#3.	Write a Python Program to calculate your Body Mass Index?
height = float(input("Input your height in Feet: "))
weight = float(input("Input your weight in Kilogram: "))
print("Your body mass index is: ", round(weight / (height * height), 2))

#4.	Write a Python Program to calculate the natural logarithm of any number?
num=int(input("enter the number: "))
import math
log_num=math.log(num)
print("The natural log ofthe given number is:",log_num)

#Write a Python Program for cube sum of first n natural numbers?
def sumOfSeries(n):
   sum = 0
   for i in range(1, n+1):
      sum +=i*i*i
   return sum
# Driver Function
n = int(input("enter the number of terms: "))
print(sumOfSeries(n))

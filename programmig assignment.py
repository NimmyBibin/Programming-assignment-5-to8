"""
# Python Program to find the L.C.M. of two input number

def compute_lcm(x, y):

   # choose the greater number
   if x > y:
       greater = x
   else:
       greater = y

   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1

   return lcm

num1 = int(input("enter the number: "))
num2 = int(input("enter the second number: "))


print("The L.C.M. is", compute_lcm(num1, num2))

#Write a Python Program to Find HCF?
# Python program to find H.C.F of two numbers

# define a function
def compute_hcf(x, y):

# choose the smaller number
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller+1):
        if((x % i == 0) and (y % i == 0)):
            hcf = i
    return hcf

num1 = int(input("enter the number: "))
num2 = int(input("enter the number: "))

print("The H.C.F. is", compute_hcf(num1, num2))

#Write a Python Program to Convert Decimal to Binary, Octal and Hexadecimal?
num=int(input("enter the number: "))

print("The decimal value of", num, "is:")
print(bin(num), "in binary.")
print(oct(num), "in octal.")
print(hex(num), "in hexadecimal.")

#Write a Python Program To Find ASCII value of a character?
c = 'p'
print("The ASCII value of '" + c + "' is", ord(c))
"""
#Write a Python Program to Make a Simple Calculator with 4 basic mathematical operations?
# Program make a simple calculator

# This function adds two numbers
def add(x, y):
    return x + y


# This function subtracts two numbers
def subtract(x, y):
    return x - y


# This function multiplies two numbers
def multiply(x, y):
    return x * y


# This function divides two numbers
def divide(x, y):
    return x / y


print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    # take input from the user
    choice = input("Enter choice(1/2/3/4): ")

    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))

        # check if user wants another calculation
        # break the while loop if answer is no
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
            break

    else:
        print("Invalid Input")

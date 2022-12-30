'''
#1.	Write a Python program to check if the given number is a Disarium Number?
# ie check  whether the sum of its digits powered with their respective position is equal to the orginal number
def is_disariun(num):
    sum=0
    for i in range(len(str(num))):
        power=int(str(num)[i])**(i+1)
        sum+=power
    if sum==num:
     print("given number is a Disarium number: ",num)
    else:
        print("given number is not a Disarium number: ",num)
    return

is_disariun(120)
is_disariun(175)
#2.	Write a Python program to print all disarium numbers between 1 to 100?
list_Disarium = []
for i in range (1,100):

    sum=0
    for j in range(len(str(i))):
        power=int(str(i)[j])**(j+1)
        sum+=power
        if sum==i:
            list_Disarium.append(i)

        else:
            break
print("The list of Disarium numbers between 1 and 100 is: ",list_Disarium)
#3.	Write a Python program to check if the given number is Happy Number?

A happy number is defined by the following process:
Starting with any positive integer, 
replace the number by the sum of the squares of its digits, 
and repeat the process until the number equals 1 (where it will stay),
 or it loops endlessly in a cycle which does not include 1.
  Those numbers for which this process ends in 1 are happy numbers,
while those that do not end in 1 are unhappy numbers.


def is_Happy_num(n):
  past = set()
  while n != 1:
        n = sum(int(i)**2 for i in str(n))
        if n in past:
            return False
        past.add(n)
  return True
print(is_Happy_num(7))
print(is_Happy_num(932))
print(is_Happy_num(6))

#4.	Write a Python program to print all happy numbers between 1 and 100?
def happy_number(n):

  past = set()
  while n != 1:
        n = sum(int(i)**2 for i in str(n))
        if n in past:
            return False
        past.add(n)
  return True

print([x for x in range(100) if happy_number(x)])


#5.	Write a Python program to determine whether the given number is a Harshad Number?

a Harshad number in a given number base, is an integer that is divisible by the sum of its digits when written in that base.
Example: The number 18 is a Harshad number in base 10, because the sum of the digits 1 and 8 is 9 (1 + 8 = 9), and 18 is divisible by 9.
The number 19 is not a harshad number in base 10, because the sum of the digits 1 and 9 is 10 (1 + 9 = 10), and 19 is not divisible by 10.



def test(n):
    if (n > 0):
        a = 0
        b = n
        while b > 0:
            a = a + b % 10
            b = b // 10
        return not n % a


n = 666
print("Original number:", n)
print("Check the said number is a Harshad number or not!")
print(test(n))
n = 11
print("\nOriginal number:", n)
print("Check the said number is a Harshad number or not!")
print(test(n))
'''
#6.	Write a Python program to print all pronic numbers between 1 and 100?
#isPronicNumber() will determine whether a given number is a pronic number or not
def isPronicNumber(num):
    flag = False;

    for j in range(1, num + 1):
        # Checks for pronic number by multiplying consecutive numbers
        if ((j * (j + 1)) == num):
            flag = True;
            break;
    return flag;


print("Pronic numbers between 1 and 100: ");
for i in range(1, 101):
    if (isPronicNumber(i)):
        print(i),
        print(" ")









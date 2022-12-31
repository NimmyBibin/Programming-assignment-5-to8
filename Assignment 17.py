
#Question1. Create a function that takes three arguments a, b, c and returns the sum of the numbers that are evenly divided by c from the range a, b inclusive

def sumDivisibles(a, b, c):
    sum = 0
    for i in range(a, b + 1):
        if (i % c == 0):
            sum += i
    return sum
a = int(input('Enter a : '))
b = int(input('Enter b : '))
c = int(input('Enter c : '))
print(sumDivisibles(a, b, c))

#Create a function that returns True if a given inequality expression is correct andFalse otherwise.


def correct_signs ( txt ) :
    return eval ( txt )
print(correct_signs("3 > 7 < 11"))
print(correct_signs("13 > 44 > 33 > 1"))
print(correct_signs("1 < 2 < 6 < 9 > 3"))

#Question3.Create a function that replaces all the vowels in a string with a specified character.



def replace_vowels(str, s):
    vowels = 'AEIOUaeiou'
    for ele in vowels:
        str = str.replace(ele, s)
    return str


input_str = input("enter a string : ")
s = input("enter a vowel replacing special charachter : ")
print("\nGiven Sting:", input_str)
print("Given Specified Character:", s)
print("Afer replacing vowels with the specified character:", replace_vowels(input_str, s))

#Question4.Write a function that calculates the factorial of a number recursively.

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

num = int(input('enter a number :'))
print("Factorial of", num, "is", factorial(num))

#Question 5:Hamming distance is the number of characters that differ between two strings.



def hamming_distance(str1, str2):
    i = 0
    count = 0

    while (i < len(str1)):
        if (str1[i] != str2[i]):
            count += 1
        i += 1
    return count


# Driver code
str1 = "abcde"
str2 = "bcdef"

# function call
print(hamming_distance(str1, str2))


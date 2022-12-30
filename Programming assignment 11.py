#1.Write a Python program to find words which are greater than given length k?
def long_words(n, str):
    word_len = []
    txt = str.split(" ")
    for x in txt:
        if len(x) > n:
            word_len.append(x)
    return word_len
print(long_words(3, "python is a programming language"))
#2.	Write a Python program for removing i-th character from a string?
def remove_char(str, n):
    first_part = str[:n]
    last_part = str[n + 1:]
    return first_part + last_part


print(remove_char('Nimmy', 0))
print(remove_char('Nimmy', 3))
print(remove_char('NimmyJoy', 5))
#3.	Write a Python program to split and join a string?
def split_string(string):
    # Splitting based on space delimiter
    list_string = string.split(' ')
    return list_string

def join_string(list_string):
    # Joining based on '-' delimiter
    string = '-'.join(list_string)
    return string

string = 'Welcome to my home'
# Splitting a string
list_string = split_string(string)
print("After Splitting: ",list_string)

# Join list of strings into one
res_string = join_string(list_string)
print("After joining: ",res_string)
#4.	Write a Python to check if a given string is binary string or not?
def check(string):
    b = set(string)
    s = {'0', '1'}
    if s == b or b == {'0'} or b == {'1'}:
        print("Binary String")
    else:
        print("Non Binary String")


s1 = "00110101"
# function calling
check(s1)
s2 = "1010100200111"
check(s2)
#5.	Write a Python program to find uncommon words from two Strings?
def uncommon_words(s1, s2):
    count = {}
    for word in s1.split():
        count[word] = count.get(word, 0) + 1
    # words of string s2
    for word in s2.split():
        count[word] = count.get(word, 0) + 1
    # return required list of words
    return [word for word in count if count[word] == 1]


s1 = "This is a python  test program"
s2 = "This is python class"



# Print required answer
print(uncommon_words(s1, s2))
#6.	Write a Python to find all duplicate characters in string?
## initializing string
string = "tutorialspoint"
## initializing a list to append all the duplicate characters
duplicates = []
for char in string:
   ## checking whether the character have a duplicate or not
   if string.count(char) > 1:
   ## appending to the list if it's already not present
    if char not in duplicates:
       duplicates.append(char)
print(*duplicates)
#7.	Write a Python Program to check if a string contains any special character?
import re
def find(string):
    special_char = re.compile('[@_!$%^&*()<>?/\|}{~:]#')
    if special_char.search(string) == None:
        return "string is accepted"
    else:
        return "string not accpeted"
s = "Nimmy@12315"
#s="Hello15"
print(s)
print(find(s))



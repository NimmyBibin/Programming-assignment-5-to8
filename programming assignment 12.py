#1.	Write a Python program to Extract Unique values dictionary values?
dict1 = {'A': [1, 3, 5, 4],
         'B': [4, 6, 8, 10],
         'C': [6, 12, 4, 8],
         'D': [5, 7, 2]}

print("The original dictionary is : ", dict1)

# Using list comprehension, values() and sorted()
res = list(sorted({ele for val in dict1.values() for ele in val}))

# print result
print("The unique values list is : ", res)
#2.	Write a Python program to find the sum of all items in a dictionary?
def returnSum(Dict):
    list = []
    for i in Dict:
        list.append(Dict[i])
    final = sum(list)

    return final

dict = {'a': 100, 'b': 200, 'c': 300}
print("Sum :", returnSum(dict))
#3.	Write a Python program to Merging two Dictionaries?
# Python code to merge dict using update() method
def Merge(dict1, dict2):
    return (dict2.update(dict1))

dict1 = {'a': 10, 'b': 8}
dict2 = {'d': 6, 'c': 4}

# This return None
print(Merge(dict1, dict2))

# changes made in dict2
print(dict2)
#4.	Write a Python program to convert key-values list to flat dictionary?
test_dict = {'month': [1, 2, 3],
             'name': ['Jan', 'Feb', 'March']}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# Convert key-values list to flat dictionary
x = list(test_dict.values())
a = x[0]
b = x[1]
d = dict
for i in range(0, len(a)):

    d[a[i]] = b[i]
# printing result
print("Flattened dictionary : " + str(d))
#5.	Write a Python program to insertion at the beginning in OrderedDict?
from collections import OrderedDict

dic1 = OrderedDict([('A', '100'), ('B', '200'), ('C', '300')])
insrt = OrderedDict([("D", '400')])

final = OrderedDict(list(insrt.items()) + list(dic1.items()))

# print result
print("Resultant Dictionary :")
print(final)
#6.	Write a Python program to check order of character in string using OrderedDict()?
from collections import OrderedDict
def check_order(my_input, my_pattern):
   my_dict = OrderedDict.fromkeys(my_input)
   pattern_length = 0
   for key,value in my_dict.items():
      if (key == my_pattern[pattern_length]):
         pattern_length = pattern_length + 1

      if (pattern_length == (len(my_pattern))):
         return 'The order of pattern is correct'

   return 'The order of pattern is incorrect'

my_input = 'Nimmy'
input_pattern = 'Ni'
print("The string is ")
print(my_input)
print("The input pattern is ")
print(input_pattern)
print(check_order(my_input,input_pattern))
#7.	Write a Python program to sort Python Dictionaries by Key or Value?
color_dict = {'red':'#FF0000',
          'green':'#008000',
          'black':'#000000',
          'white':'#FFFFFF'}

for key in sorted(color_dict):
    print("%s: %s" % (key, color_dict[key]))
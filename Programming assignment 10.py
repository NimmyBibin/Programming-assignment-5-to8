
#1.	Write a Python program to find sum of elements in list?
numbers=[1,2,3,45,4,6]
sum=0
for i in  numbers:
    sum+=i
print("the sum is: ",sum)

    # OR
l= []
ele=0
total=0
n = int(input("Enter number of elements : "))
for i in range(0, n):
    print("Enter elements:")
    ele = int(input())
    l.append(ele)
print(l)
for ele in range(0, n):
    total = total + l[ele]
print("Sum of all elements in the list: ", total)

#2.	Write a Python program to  Multiply all numbers in the list?
def multiply(numbers):
    total = 1
    for x in numbers:
        total *= x
    return total
print(multiply((8, 2, 3, -1, 7)))

#3.	Write a Python program to find smallest number in a list?
def smallest_num_in_list( list ):
    min = list[ 0 ]
    for a in list:
        if a < min:
            min = a
    return min
print(smallest_num_in_list([1, 2, -8, 0]))

#4.	Write a Python program to find largest number in a list?
def largest_num_in_list( list ):
    min = list[ 0 ]
    for a in list:
        if a > min:
            max = a
    return max
print(largest_num_in_list([1, 2, -8, 0]))

#5.	Write a Python program to find second largest number in a list?
def second_largest(numbers):
  if (len(numbers)<2):
    return
  if ((len(numbers)==2)  and (numbers[0] == numbers[1]) ):
    return
  dup_items = set()
  uniq_items = []
  for x in numbers:
    if x not in dup_items:
      uniq_items.append(x)
      dup_items.add(x)
  uniq_items.sort()
  return  uniq_items[-2]
print(second_largest([1,2,3,4,4]))
print(second_largest([1, 1, 1, 0, 0, 0, 2, -2, -2]))


#6.	Write a Python program to find N largest elements from a list?
# function
def N_max_elements(list, N):
    result_list = []

    for i in range(0, N):
        maximum = 0

        for j in range(len(list)):
            if list[j] > maximum:
                maximum = list[j]

        list.remove(maximum)
        result_list.append(maximum)

    return result_list


# test
list1 = [2, 6, 41, 85, 0, 3, 7, 6, 10]
N = 2

print(N, "max elements in ", list1)

# Calling and printing the function
print(N_max_elements(list1, N))

#7.	Write a Python program to print even numbers in a list?

# list of numbers
list1 = [10, 21, 4, 45, 66, 93]

# iterating each number in list
for num in list1:

    # checking condition
    if num % 2 == 0:
        print(num, end=" ")

#8.	Write a Python program to print odd numbers in a List?
list1 = [11,23,45,23,64,22,11,24]
# iteration
for num in list1:
   # check
   if num % 2 != 0:
      print(num, end = " ")

#9.	Write a Python program to Remove empty List from List?

# Initializing list
test_list = [5, 6, [], 3, [], [], 9]

# printing original list
print("The original list is : " + str(test_list))

# Remove empty List from List
# using list comprehension
res = [ele for ele in test_list if ele != []]

# printing result
print("List after empty list removal : " + str(res))


#10.Write a Python program to Cloning or Copying a list?
original_list = [10, 22, 44, 23, 4]
new_list = list(original_list)
print(original_list)
print(new_list)

#11.Write a Python program to Count occurrences of an element in a list?
def list_count_4(nums):
  count = 0
  for num in nums:
    if num == 4:
      count = count + 1

  return count

print(list_count_4([1, 4, 6, 7, 4]))
print(list_count_4([1, 4, 6, 4, 7, 4]))



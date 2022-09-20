

#1.	Write a Python Program to find sum of array?
a=[1,2,3,4,5,6,7,8,9]
sum=0
for i in a:
    sum=sum+i
print(sum)

#2.	Write a Python Program to find largest element in an array?
arr=[12,11,21,32,23,13]
arr.sort()
print(arr[-1])
#method 2

arr1=[12,11,21,32,23,13]
n=len(arr)
max_num=arr1[0]
for i in range(n):
    if arr1[i]>max_num:
        max_num=arr1[i]
print("The largest num is: ",max_num)
#Write a Python Program for array rotation?
#Intialize array
arr = [1, 2, 3, 4, 5]
#n determine the number of times an array should be rotated
n = 1

#Displays original array
print("Original array: ")
for i in range(0, len(arr)):
    print(arr[i])

#Rotate the given array by n times toward left
for i in range(0, n):
    #Stores the first element of the array
    first = arr[0]
    for j in range(0, len(arr)-1):
        #Shift element of array by one
        arr[j] = arr[j+1]

    #First element of array will be added to the end
    arr[len(arr)-1] = first

print()

#Displays resulting array after rotation
print("Array after left rotation: ");
for i in range(0, len(arr)):
    print(arr[i])
"""
#4.	Write a Python Program to Split the array and add the first part to the end?
#Step 1- Define a function SplitArray() which will split the array and add the first part to the end

#Step 2- Run a loop from the starting index to the index where the array has to be split
#Step 3- Inside the loop, store the first element of the array in a variable x

#Step 4- Run a loop inside the first loop from starting to the ending index and shift the elements to the left side
#Step 5- When all the elements are shifted keep the first element at the last index

#Step 6- Repeat the process for all elements which are in the first part of the array
"""
def splitarr(arr,n,k):
    for i in (0,k):
        x=arr[0]
        for j in range(0, n - 1):
            arr[j] = arr[j + 1]
            arr[n - 1] = x
"""
Step 7- Define another function to print the array

Step 8- Specify the array and the position from where the array has to split

Step 9- Call the function and pass the array and the position

Step 10- Print the resultant array
"""
arr = [15, 40, 15, 16, 50]
n = len(arr)
position =3
splitarr(arr, n, position)
for i in range(0, n):
	print(arr[i], end = ' ')

#5.	Write a Python Program to check if given array is Monotonic?
def isMonotonic(A):
   return (all(A[i] <= A[i + 1] for i in range(len(A) - 1)) or
      all(A[i] >= A[i + 1] for i in range(len(A) - 1)))

A = [1,2,3,4,7,8]
print(isMonotonic(A))








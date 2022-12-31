"""
Question1
Write a function that takes a list and a number as arguments. Add the number to the end of the list, then remove the first element of the list. The function should then return the updated list.

"""
lst = [5, 6, 7, 8, 9]
def next_in_line(lst,num):
    if len(lst) > 0:
        lst.append(num)
        return lst[1:]
    else:
        print("No list has been selected")
print(next_in_line([5, 6, 7, 8, 9], 1))

"""
Question2
Create the function that takes a list of dictionaries and returns the sum of people's budgets.
Examples
get_budgets([
{ 'name': 'John', 'age': 21, 'budget': 23000 },
{ 'name': 'Steve', 'age': 32, 'budget': 40000 },
{ 'name': 'Martin', 'age': 16, 'budget': 2700 }
]) ➞ 65700
get_budgets([
{ 'name': 'John', 'age': 21, 'budget': 29000 },
{ 'name': 'Steve', 'age': 32, 'budget': 32000 },
{ 'name': 'Martin', 'age': 16, 'budget': 1600 }
]) ➞ 62600
"""

def get_budgets(listDict):
    sum = 0
    for dc in listDict:
        for k,v in dc.items():
            if k == 'budget':
                sum = sum + v
    return sum
print(get_budgets([
{ 'name': 'John', 'age': 21, 'budget': 23000 },
{ 'name': 'Steve', 'age': 32, 'budget': 40000 },
{ 'name': 'Martin', 'age': 16, 'budget': 2700 }
]))
"""
Question3
Create a function that takes a string and returns a string with its letters in alphabetical order.
"""
def alphabet_soup(str):
    return ''.join(sorted(str))
print(alphabet_soup('hello'))
"""
Question4
Suppose that you invest $10,000 for 10 years at an interest rate of 6% compounded monthly.
What will be the value of your investment at the end of the 10 year period?
Create a function that accepts the principal p, the term in years t, the interest rate r, and the
number of compounding periods per year n. The function returns the value at the end of term
rounded to the nearest cent.
"""
def compound_interest(amt, years, intrest, compPeriod):
    future_value = amt *(1 + (intrest/compPeriod)) ** (years * compPeriod)
    return round(future_value,2)
print(compound_interest(100, 1, 0.05, 1))

"""
Question5
Write a function that takes a list of elements and returns only the integers.
"""
def return_only_integer(lst):
    intLst = []
    for i in lst:
        if type(i) == int:
            intLst.append(i)
    return intLst   
print(return_only_integer([9, 2, 'space', 'car', 'lion', 16]))
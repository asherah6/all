# MERGE SORT: 
# COMPARE & MERGE, COMPARE & MERGE ...

# https://www.w3schools.com/python/python_dsa_mergesort.asp

def merge_sort(lst):
    # [1,5,6,2,8,7,9]
    if len(lst) <= 1:
        return lst
    # 7
    # 3.5
    # 3
    mid = len(lst)//2
    # mid is to split into 2 list half/half
    # we dont need the location we just need half
    # left = lst[0:mid]
    # right = lst[mid:len(lst)]
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])
   
    res = []
    i = 0
    j = 0
 
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            res.append(left[i])  
            i += 1
        else:
            res.append(right[j])
            j += 1
    res.extend(left[i:])
    res.extend(right[j:])
    return res
 

#  TASK 1:
# Write a program that allows a user to calculate the quotient (division of one number by another) of two numbers. 
# The program accepts two values from the keyboard and returns the result of the operation to the screen. 
# Handle the exception that occurs during division by zero and print the error message.

a = int(input("Number 1:"))
b = int(input("Number 2:"))


if b > 0:
    c = a/b
    print(c)
else:
    print("Error: You cant divide by 0!")

# TASK 2:
# Implement the first task through a function. 
# The function must accept two parameters and display the result of division on the screen. 
# Create two versions of the function implementation:
# The first version does not handle the exception inside the function. 
# All handling is on the outside;
# The second version handles the exception inside the function.

# V1:

def my_func(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("You can't divide by zero")
# V2:
try:
    print(my_func(1, 0))
except ZeroDivisionError:
    print("You can't divide")


# MOJE:
# V1:

a = int(input("Number 1:"))
b = int(input("Number 2:"))

if b > 0:
    c = a/b
    print(c)
else:
    print("Error: You cant divide by 0!")


# TASK 3:
# Write a program that accepts a string and tries to convert it to a number.
# Handle the exception that occurs when the conversion fails, and print an error message.

def convert(some_string: str):
    try:
        converted = int(some_string)
        print(converted)
    except ValueError:
        print("Cannot convert a string to an integer ")
 
 
convert("5")
 
convert("hello")



# TASK 4:
# Implement the third task through a function. The function should accept a string and display the result of the conversion on the screen. 
# Create two versions of the function implementation:
# The first version does not handle the exception inside the function. 
# All handling is on the outside;
# The second version handles the exception inside the function.

def convert(some_string: str):
    data = int(some_string)
    return data
 
string = input("string :")
try:
    x = convert(string)
    print(x)
except ValueError:
    print("you can not convert alphabet to an integer value")


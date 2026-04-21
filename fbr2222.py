# HIGH ORDER FUNCTIONs:
# Funkcja która zawiera funkcję jako parametr i zwraca również funkcję.

def add_data(x, y):
    return x+ y
 
def substract_data(x, y):
    return abs(x -y)
 
def multiply_data(x, y):
    return x * y
 
def divide_data(x, y):
    if x > y:
        return x / y
    else:
        return y /x
   
 
def calculator(func, x, y):
    return func(x, y)
 
x = calculator(add_data, 2,3)
y = calculator(substract_data, 2,3)
z = calculator(multiply_data, 2,3)
G = calculator(divide_data, 2,3)
 
print(x)
print(y)
print(z)
print(G)


# V2:

def make_square(n):
    return n **2
 
 
def do_something(func,n):
    return func(n)
 
x = do_something(make_square, 3)
print(x)


# V3:

def greet(func):
    return func("Hello")
 
def uppercase(text):
    return text.upper()
 
print(greet(uppercase))


# V4:
# higher order function returing a function:

def fun(n):
    return lambda x: x * n
 
# creating mutiliplier functions
double = fun(2)
triple = fun(3)
 
print(double(5))  
print(triple(5))


# TASK 1:

# To solve this task, be sure to use the mechanism of higher order functions. 
# Create a function that checks the passed number to be even or odd. 
# A user determines what to check for (evenness or oddness).

# first_fun fun(n) n%2 ==0
# second_fun fun(n) n%2 !=0
 
 
# highrorder(choice, func, n):
# return func(choice, n)
 
 
def is_even(n):
    return n % 2 == 0
 
def is_odd(n):
    return n % 2 != 0
 
def check_data(func, n):
        return func(n)
 
choice = input("choice :")
value = int(input("value :"))
 
if choice == "even":
    print(check_data(is_even, value))
else:
    print(check_data(is_odd, value))


# TASK 2:
# To solve this task, be sure to use the mechanism of higher order functions. 

def square(n):
    return n **2
 
def cube(n):
    return n **3
 
def higher_order(func, n):
    return func(n)
 
choice = input("choice :")
value = int(input("value :"))
 
 
if choice == "square":
    print(higher_order(square, value))
elif choice == "cube":
    print(higher_order(cube, value))
else:
    pass
 
#  TASK 3:
# SUM + MULTIPLE
# To solve this task, be sure to use the mechanism of higher order functions.

def func_sum(a ,b):
    return a + b
def func_multiply(a, b):
    return a * b

def higher_order(func, a, b):
    return func(a, b)

choice = input("enter your choice: ")

if choice == "sum":
    print(higher_order(func_sum,2,3))
elif choice == "multiply":
    print(higher_order(func_multiply,2,3))
else:
    pass

# TASK 4:

# Create a function to display the current time. The function takes no parameters. 
# Without using decorator syntax, decorate the function with another function. 
# Potential data output to the screen:

# import datetime
 
 
# now = datetime.datetime.now()
# print(now.strftime("%H:%M"))

import datetime
 
def func_time(func):
    print("*" * 5)
    print(func())
    print("*" * 5)
 
def display_time():
    now = datetime.datetime.now()
    return now.strftime("%H:%M")
 
func_time(display_time)

# TASK 5:

# Write a recursive function that takes 
# a list of 100 random integers and finds the position at which a sequence 
# of 10 numbers begins, and their sum must be the smallest.

list_of_int = [random.randint(1, 100) for i in range(1, 101)]
print(list_of_int)
 
def smallest_sum(list_of_int):
    first_index = 0
    small_sum = float("inf")
 
    for i in range(first_index, len(list_of_int) -9):
        current_list = list_of_int[i : i +10]
        current_sum = sum(current_list)
 
        if current_sum < small_sum:
            small_sum = current_sum
            first_index = i
       
    return small_sum, first_index
 
print(smallest_sum(list_of_int))
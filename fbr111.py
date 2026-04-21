# FUNCTIONS

# FUNKCJA DEF:
# multiplying
# substracting
# divide


def multiply(a,b):
    return a * b

def divide(a,b):
    return a/b

def substracting(a,b):
    return a - b


print(multiply(1,3))
print(divide(4,2))
print(substracting(5,2))


# V2:
def add_data(x, y):
    return (
        f"the subtraction is {abs(x - y)}\n"
        f"the multiplication is {abs(x * y)}\n"
        f"the division is {abs(x / y)}"
    )
 
x = add_data(3, 4)
print(x)


# kalkulator:

def calculator(x, y):
    user_input = (input("method :")).lower()
    if user_input == 'add':
        return x + y
    elif user_input == 'substract':
        return abs(x-y)
    elif user_input == "multiply":
        return x *y
    elif user_input == "divide":
        return x/y
   
    # DiVide
 
x = calculator(2,3)
print(x)


# Write a function that takes two numbers as a parameter
#  and displays all odd numbers in between.
# if number % 2 != 0
# 2, 8
# 3,5,7

def display_odd(x, y):
    data = []
    for i in range(x,  y+1):
        if i % 2 != 0:
            data.append(i)
    return data
 
x = display_odd(2, 8)
print(x)


# Write a function that prints a horizontal or vertical line made out of some symbol. 
# The function takes the following as a parameter: the line's length, direction, symbol.

def print_symbol(length,direction,symbol):
    for _ in range(length):
        if direction == "horizontal":
            print(symbol, end="")
        else:
            print(symbol)
 
 
# print_symbol(5, "horizontal", "#")
print_symbol(5, "vertical", "#")


# Write a function that returns the greatest of four numbers. Numbers are passed as parameters.

# v1:

def max_num(a, b, c, d):
    return max(a, b, c, d)

print(max_num(1, 4, 7, 3))

# v2:

def greatest(a,b,c,d):
    data = [a,b,c,d]
    great = data[0]
    for i in data:
        if i > great:
            great = i
    return great
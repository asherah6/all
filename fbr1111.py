#  LAMBDA FUN.:

def square_data(x):
    return x**2
x = square_data(2)
print(x)
 
x = lambda x: x**2
print(x(2))

# V2:

def add_data(x, y):
    return x + y
 
print(add_data(2,4))
 
a = lambda x, y : x+y
print(a(2,4))
      
#   V3:

user_name = lambda first, last: f"name :{first} surname: {last}"
 
print(user_name("izan", "tzafer"))

# GENERATOR FUN.:

import random
 
for i in range(1, 10):
    new_data = random.randint(1,10)
    print(new_data)
 
data = range(1, 10)
for i in data:
    print(i)

# V2:

def first_generator(x, y):
    for i in range(x, y+1):
        if i % 2 == 0:
            yield i
 
 
data = first_generator(2, 20)
 
for i in data:
    print(i)

# TASK 1:
# Create a function that returns all odd numbers in a range.
# The function takes the beginning and the end of the range as parameters.
# Use the generator mechanism within the function.
 
 
def generate_odd_numbers(start, end):
    for i in range(start, end + 1):
        if i % 2 != 0:
            yield i
 
data = generate_odd_numbers(2, 20)
for i in data:
    print(i)

# TASK 2:
# Create a function that returns all values
# from a list that are in a range specified by a user.
# The function takes the list,
#  the beginning and the end of the range as parameters.
#  Use the generator mechanism within the function.

def data_generator(lst, start, end):
    for i in range(start, end + 1):
        if i in lst:
            yield i
 
lst = [2,5,3,1,10, 15, 16, 19,6,4, 8]
start = 5
end = 9
 
data = data_generator(lst, start, end)
 
for i in data:
    print(i)

# TASK3:
# Create a function that returns all prime numbers in a range. 
# The function takes the beginning and end of the range as parameters. 
# Use the generator mechanism inside the function.

def check_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
 
# 2,3,4,5,6,7,8,9,..16
# 17
 
def generate_prime(m):
    for j in range(2, m+1):
        if check_prime(j):
            yield j
 
data = generate_prime(100)
 
for k in data:
    print(k)

def my_function1(*username):
#   print("Username:", username)
  print("Additional details:")
  for i in username:
    print(i)
 
# my_function1("a","b","c")

data = {
  "name": "john",
  "age": 12
}

def my_function(username, **details):
  print("Username:", username)
  print("Additional details:")
  for key, value in details.items():
    print(" ", key + ":", value)
 
my_function("emil123", age = 25, city = "Oslo", hobby = "coding", fruit = "mango")

# TASK 1:
# Write a function that returns the greatest of four numbers. Numbers are passed as parameters.

def biggest_number(a,b,c,d):
    greatest = a
    if b > greatest:
        greatest = b
    if c > greatest:
        greatest = c
    if d > greatest:
        greatest = d
 
    return greatest
 
print(biggest_number(5,3,8,23))


# TASK 2:
# Write a function that returns the sum of numbers in a specified range. 
# The start and end points of the range are passed as parameters.

def sum_of_number(start, end):
    total = 0
    for i in range(start, end +1):
        total += i
    return total
 
x = sum_of_number(2, 5)
print(x)
 
#  TASK 3:
# Write a function that checks if a number is prime.
#  The number is passed as a parameter.
# If the number is prime, return true, otherwise false.
 
# 2,3,5,7,11
 
def is_prime(n):
    if n < 2:
        return False
   
    for i in range(2, n):
        if n % i == 0:
            return False
   
    return True
 
# 5 %
x = is_prime(5)
print(x)
 
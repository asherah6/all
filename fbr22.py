#  Write a recursive function to find the power of a numer.
#  moje:
def power_number(num, power):
    return num ** power

x = power_number(2, 3)
print(x)

# v1:
# num
# power
# 2**3
# 2*2*2 = 8
# 2**0
def power_of_number(num, power):
    if power == 0:
        return 1
    else:
        return num * power_of_number(num, power-1)
 
x = power_of_number(2, 3)
print(x)

# Write a recursive function to find the power of a number.
 
# num
# power
# 2**3
# 2*2*2 = 8
# 2**0
 
def power_of_number(num, power):
    if power == 0:
        return 1
    else:
        return num * power_of_number(num, power-1)
            # 2 * power_of_number(2,2)
            # 2 * 2 * power_of_number(2, 1)
            # 2 * 2 * 2 * power_of_number(2, 0)
            # 2 * 2 * 2 * 1
           
print(power_of_number(2, 3))

# TASK 2:
# Write a recursive function that calculates the sum of all numbers in the range from a to b. 
# The user types in a and b. 
# Illustrate how the function works with an example.

# v1:
def add_all_nums(a,b):
    if a > b:
        return 0
    else:
        return a + add_all_nums(a +1, b)
 
x = add_all_nums(2, 5)
print(x)

# v2:
def add_all_nums(a,b):
    if a == b:
        return b
    else:
        return b + add_all_nums(a, b-1)
 
x = add_all_nums(2, 5)
print(x)

# v3:

def add_all_nums(a,b):
    if a == b:
        return a
    else:
        return a + add_all_nums(a +1, b)
 
x = add_all_nums(2, 5)
print(x)
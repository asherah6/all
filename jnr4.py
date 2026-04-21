# TUPLE
 
# CRUD
# CREATE
 
data = ()
data1 = ("A", "B", "C")
data2 = ("DATA",)
# its a syntax for tuple where python checks rest of data types
data3 = True, False, "a", 123
 
# READ
# print(data1[0])
# for i in data1:
#     print(i)
 
# if "B" in data1:
#      print("yes")
 
# print(data1[:2])
 
# UPDATE  is not supported by tuple
 
# DELETE
 
# print(data1)
# del data1
# print(data1)
 
data = tuple(i for i in range(10))
# data = (i for i in range(10))
# data = [i for i in range(10)]
# print(data)
# print(type(data))


# random:
import random
 
# data = ["olexander", "altay", "oscar", "kacper", "adriana", "abraham"]
 
# student = random.choice(data)
# print(student)
 
data = []
 
 
for i in range(10):
    number = random.randint(1, 20)
    data.append(data)
 
print(data)

# TASK 1:

# Calculate the following in a list filled with random numbers:


# Sum of negative numbers;

import random

data = []
 
negeative_numbers = []
 
for i in range(10):
    num = random.randint(-10, 10)
    data.append(num)
 
for i in data:
    if i < 0:
        negeative_numbers.append(i)
 
print(data)
print(negeative_numbers)
 
print(f"sum of negetive :  {sum(negeative_numbers)}")


# Sum of even numbers;

# v1:
import random

data = []
even_numbers = []
 
 
for i in range(10):
    num = random.randint(-10, 10)
    data.append(num)
 
for j in data:
    if j % 2 == 0:
        even_numbers.append(j)

print(data)
print(f"even numbers {even_numbers}")
print(f"even numbers {sum(even_numbers)}")


# v2:

import random

even_numbers = []
counter = 0
 
 
for i in range(10):
    num = random.randint(-10, 10)
    data.append(num)
 
for j in data:
    if j % 2 == 0:
        even_numbers.append(j)
        counter += j
 
 
print(data)
print(f"even numbers {even_numbers}")
print(f"even numbers {sum(even_numbers)}")
print(f"even numbers {counter}")


# Sum of odd numbers;

import random

data = []
odd_numbers = []
 
for i in range(10):
    num = random.randint(-10, 10)
    data.append(num)
 
for j in data:
    if j % 2 != 0:
        odd_numbers.append(j)
 
print(data)
print(f"odd numbers {odd_numbers}")
print(f"odd numbers {sum(odd_numbers)}")

# Product of elements with indices divisible by 3;

import random
                                                                                                                                                                                                                                                                                                                                                                                    
data = []
numbers = []
product = 1
 
for i in range(10):
    num = random.randint(-10, 10)
    data.append(num)
 
for j in data:
    if j > 0 :
        if j % 3 == 0:                                                                                                  
            numbers.append(j)
            product *= j
 
print(data)
print(f"odd numbers {numbers}")
print(f"product {product}")


# Product of elements between the smallest and the largest element;

data = []
 
smallest = 0
 
for i in range(10):
    num = random.randint(-10, 10)
    data.append(num)
 
for j in data:
    if j < smallest:
        smallest = j
 
 
print(data)
print(smallest)


# The sum of the elements between the first and the last positive elements.

total = 0
new_data = []
for i in data:
    if i > 0 :
        new_data.append(i)
       
print(new_data)
new_data.sort()
print(new_data)
 
for j in range(1, len(new_data)-1):
    total+= new_data[j]
 
print(total)


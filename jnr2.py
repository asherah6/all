fruits = ["mango", "banana","orange", "orange", "apple", "strawberry"]
# print(fruits)
# print(type(fruits))
 
# CRUD
# CREATE
 
fruits = set(fruits)
fruits.add("cherry")
# print(fruits)
 
#READ
# for i in fruits:
#     print(i)
 
# if "cherry" in fruits:
#     print("yes")
 
# DELETE
# print(fruits)
# fruits.remove("cherry")
# fruits.remove("cherry")
# print(fruits)
 
# fruits.discard("cherry")
# print(fruits)
# fruits.pop()
# print(fruits)
# fruits.pop()
# print(fruits)
 
# UPDATE
vegetable = {"cabbage", "tomato", "onion", "chilli"}
 
fruits.update(vegetable)  
print(fruits)

#  te same elementy: 

num1 = {1,2,3}
num2 = {3, 4, 5}
 
data = num1.intersection(num2)
print(data)


# TASK 1

# The user inputs a fruit from the keyboard. 
# Display the number of times this fruit occurs as an element.

user_input = (input("Provide the list of fruits:"))

fruits = ["apple", "banana", "orange", "banana", "grape", "banana", "apple"]

counter = 0
for i in fruits:
    if user_input == i:
        counter += 1
 
counter = fruits.count(user_input)
 
print(f"{user_input} occurs {counter} times in fruits")

# TASK 2:

# Improve Task 1 by adding the possibility to calculate how many times this fruit occurs as a part of an element. 
# Here, for example, "banana, apple, banana, mango, mango, strawberry, banana".
# The word "banana" occurs three times.

fruits = ['banana', 'apple', 'bananamango', 'mango', 'strawberry-banana']
 
user_input = input("fruit :")

for i in fruits:
    if user_input in i:
    print("Yes")


# TASK 3:

# You have a tuple containing names of car manufacturers
# (a name may occur from 0 to N times).
#  The user inputs a manufacturer and a replacement word.
#  Replace all elements in the tuple with the replacement word.
#  The match must be complete.
 
data = ("kia", "ford", "toyota", "bmw", "hyundai","kia","kia","kia")
 
name = input("name :")
replacement = input("replacement :")
 
 
data = list(data)
 
for i in range(len(data)):
    if data[i] == name:
        data[i] = replacement
   
 
data = tuple(data)
# print(data)
# print(type(data))

# TASK 4:

# You have a tuple of integers.
# Display statistics on the number of digits in tuple elements.
# For instance:
# One digit — 3 elements;
# Two digits — 4 elements;
# Three digits — 5 elements.
 
data = (1, 2, 3,34,45, 56,234,345,345, 8,34343)
data = list(data)
 
histogram = {}
 
for i in data:
    num = len(str(i))
    if num in histogram:
        histogram[num] += 1
    else:
        histogram[num] = 1
 
print(histogram)
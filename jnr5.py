# dictionary
 
# CRUD
 
# CREATE
 
 
data = {"name": "john", "surname": "doe", "age": 30, "is_admin": True}
print(data)
# data = {0: "john", 1:"Doe"}
# data = dict(name="john", last_name = "Doe", age=30, is_admin=True)
data["has_password"]= True
 
# READ
# print(data["name"])
# print(data["age"])
 
# for i in data:
#     print(f"key is : {i} value is : {data[i]}")


data = {
    "name": "john",
    "meta" : {1 : "apple", 2:"mango"},
    "age": 45
}
 
print(data["meta"][2])
 
 
# UPDATE
 
# print(data)
# data["name"] = "johnny"
# print(data)
 
# for i in data:
#     if data[i] == "john":
#         data[i] = "johnny"
 
# print(data)
 
# DELETE
 
# data.clear()
# data.pop("name")
# del data["age"]
# del data
# print(data.pop("lastname", "not found"))
# print(data)
# data.popitem()
# print(data)
# data.popitem()
# print(data)
 
# removing multiple items
 
# remove = ["has_password", "age"]
 
# for i in remove:
#     data.pop(i, "not found")
 
# print(data)
 
keys = data.keys()
values = data.values()
print(keys)
print(values)
 
for i in values:
    print(i)


# HOMEWORK V5:

# There is a list of integers filled with random numbers.
#  Do the following based on this data:
import random

data = []
for i in range(10):
    num = random.randint(-20, 20)
    data.append(num)
 
print(data)
 
 
# Create a list of integers containing only even numbers;

even_number = []
for j in data:
    if j % 2 == 0:
        even_number.append(j)
print(even_number)
 
 
# Create a list of integers containing only odd numbers;
 
odd_number = []
for j in data:
    if j % 2 != 0:
        odd_number.append(j)
print(odd_number)

# Create a list of integers containing only negative numbers;
 
negetive = []
for i in data:
    if i < 0:
        negetive.append(i)
 
print(negetive)

# Create a list of integers containing only positive numbers.
 
positive = []
for i in data:
    if i > 0:
        positive.append(i)
 
print(positive)
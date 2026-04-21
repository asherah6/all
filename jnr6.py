data = {
    "name": "john",
    "meta" : {'1': "apple", '2':"mango"},
    "age": 45
}
 
# if "meta" in data:
#     print("yes")
 
for i in data:
    # print(i)
    # print(data[i])
    if i == "meta":
        for j in data[i]:
            if "mango"in data[i][j]:
                print("mango is there")
            # print(data[i][j])


# variable = {key:expression for (key, value) in iterable}
 
data = {x:x for x in range(20)}
data = {x:x**2 for x in range(20)}
data = {x:x**2 for x in range(20) if x % 2 == 0}
# print(data)
 
 
new_data = {1:"banana", 2:"apple", 3:"kiwi", 4:"strawberry"}
 
print(new_data.keys())
print(new_data.values())
 
fruit = {value:key for  key,value  in new_data.items()}
print(fruit)
 

 # set
 
# CRUD
# CREATE
 
myset = {1,2,3}
# print(type(myset))
# print(myset)
 
myset= set(['1', '2', '2'])
# print(type(myset))
# print(myset)
 
# READ
# print(myset)
# for i in myset:
#     print(i)
 
# UPDATE
myset.update((1,2,3,4))
# print(myset)
 
myset.add("apple")
print(myset)
 
 
# DELETE
 
myset.remove("2")
# print(myset)
myset.pop()
# print(myset)
myset.discard("1")
print(myset)
 
# myset.clear()
# print(myset)
 
# comprehension
 
data = {i for i in range(20)}
print(data)


# You have a set containing country names. Provide the following features:

countries = set(["Spain", "USA", "Poland", "France"])

# Add a country;

countries.add("India")
print(countries)

# Delete a country;

countries.discard("USA")
print(countries)

# Search for a country by entered characters;

country = input("Enter your country: ")

# Check whether the country exists inside the set.

if country in countries:
    print(country)
    print("Country is in the set")
else:
    print("There is no country of origin")

# TASK 2:

# You have two sets containing city names.
# Create a third set containing names present in both sets.
 
 
cities1 = {"Ciudad de Mexico", "Acapulco", "Monterrey", "Guadalajara", "Cancun"}
cities2 = {"Estado de Mexico", "Yucatan", "Monterrey", "Guadalajara", "Cancun"}
 
cities3 = cities1.intersection(cities2)
 
 
cities3 = set()
 
for i in cities1:
    if i in cities2:
        cities3.add(i)
 
 
print(cities3)


# TASK 3:
# You have two sets containing city names.
# Create a third set containing names present in the first set but not in the second.
 
cities1 = {"Ciudad de Mexico", "Acapulco", "Monterrey", "Guadalajara", "Cancun"}
cities2 = {"Estado de Mexico", "Yucatan", "Monterrey", "Guadalajara", "Cancun"}

#  V1:
city3 = cities1 - cities2
print(city3)

# V2:
city3 = set()
 
for i in cities1:
    if i not in cities2:
        city3.add(i)
 
print(city3)


# TASK 4:

# You have two sets containing city names. Create a third set containing names unique to each set
 
cities1 = {"Ciudad de Mexico", "Acapulco", "Monterrey", "Guadalajara", "Cancun"}
cities2 = {"Estado de Mexico", "Yucatan", "Monterrey", "Guadalajara", "Cancun"}

# V1:
city3 = cities1 + cities2
print(city3)

# V2:
city3 = cities1.add(cities2)
print(city3)


# HOMEWORK:

# A dictionary contains a set of pairs: 
# Country name -> Capital. Provide the possibility to add, delete, search, and replace them
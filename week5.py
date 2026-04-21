#The user inputs a fruit from the keyboard. 
# Display the number of times this fruit occurs as an element.
 

fruits = ["blueberry", "banana", "apple"]
user_input = input("Please choose a fruit: ")
count_fruits = 0 

for i in fruits:     
    if user_input == i:         

count_fruits += 1 
print(count_fruits)


# 10
# alphabets
# how many numbers
# how many symbols
 
import random
 
mylist = ["apple", "banana", "cherry"]
random.shuffle(mylist)
 
print(mylist)


# -------------------------------------------

import random
# 10
# alphabets
# howmany numbers
# how many symbols
 
password = []
 
alphabet = int(input("howmany alphabet you wwant : "))
numbers = int(input("howmany numbers you wwant : "))
symbol = int(input("howmany symbols you wwant : "))
 
 
alp = ['a','b','c','d','e','f','g','h','i',"j"]
num = [1,2,3,4,5,6,7,8,9,0]
sym = ["@", "#", "%", "&"]
 
for i in range(alphabet):
    password.append(random.choice(alp))
for j in range(numbers):
    password.append(random.choice(str(num)))
for k in range(symbol):
    password.append(random.choice(sym))
random.shuffle(password)
password =  "".join(password)
print(password)
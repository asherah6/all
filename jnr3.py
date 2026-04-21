# LIST:
 
# CREATE
fruits = ["apple", "banana"]
fruits.append("kiwi")
fruits.insert(0, "orange")
# print(fruits)
# print(fruits)
 
# READ
# print(fruits[0])
# for i in fruits:
#     print(i)
 
# UPDATE
# print(fruits)
fruits[3] = "pineapple"
 
# print(fruits.index("pineapple"))
# print(fruits)
 
# DELETE
# print(fruits)
# fruits.remove("pineapple")
# print(fruits)
# fruits.pop()
# print(fruits)
 
# del fruits[0]
# print(fruits)
 
 
# short statement for checking data which returns boolean
# print("apple" in fruits)
 
 
# data = [expression for i in iterable condition]
 
text = "ford is a very good car"
 
data = [i for i in range(20) if i % 2 == 0]
print(data)
 
# data = []
# for i in range(20):
#     if i % 2 == 0:
#         data.append(i)
# print(data)

# rozdzielenie wyrazów:
text = "ford is a very good car"
data = text.split()
print(data)


# TASK 1:
# There is some text. Implement the following features:
# Change the text so that each sentence starts with a capital letter;


text = "lorem ipsum is simply dummy text of the printing and typesetting industry."
text1 = "lorem Ipsum has been the industry's standard dummy text ever since the 1500s"
text2 = "lorem Ipsum has been the industry's standard dummy text ever since the 1500s"
 
data = [text, text1, text2]
 
for i in data:
    print(i.capitalize())

data = text.title()  # -> inny sposób


# Count how many times numbers appear in the text;
text = "lorem ipsum is simply/ ? dummy , .text 2 3of 2the 7printing !!!!and typesetting industry. 1500"
data = [i for i in text if i.isdigit()]
print(len(data))

# 2 sposób:
# counter = 0
# for i in data:
#     if i.isdigit():
#         counter += 1
# print(counter)

# Count how many times punctuation marks appear in the text;

text = "lorem ipsum is simply/ ? dummy , .text 2 3of 2the 7printing !!!!and typesetting industry. 1500"
counter = 0
punctuate = [",",".","/","?"]

for i in text:
    if i in punctuate:
        counter +=1
print(counter)

# Count the number of exclamation marks in the text.
text = "lorem ipsum is simply/ ? dummy , .text 2 3of 2the 7printing !!!!and typesetting industry. 1500"
counter = 0

for i in text:
    if i == "!":
        counter +=1
print(counter)



# Task 1
# There is some text. Implement the following features:
# Change the text so that each sentence starts with a capital letter;
# Count how many times numbers appear in the text;
# Count how many times punctuation marks appear in the text;
# Count the number of exclamation marks in the text.

# PUNKT 1:
# text = "lorem ipsum is simply/ ? dummy , .text 2 3of 2the 7printing !!!!and typesetting industry. 1500"
# # text1 = "lorem Ipsum has been the industry's standard dummy text ever since the 1500s"
# # text2 = "lorem Ipsum has been the industry's standard dummy text ever since the 1500s"
 
 
# # data = [text, text1, text2]
# data = text.title() 

# # for i in data:
# #     print(i.capitalize())

 
# # PUNKT 2:
# counter = 0
# # data = [i for i in data if i.isdigit()]
# # print(len(data))
# # for i in data:
# #     if i.isdigit():
# #         counter += 1
# # print(counter)
 
# # PUNKT 3:

# punctuate = [",",".","/","?"]
# # for i in data:
# #     if i in punctuate:
# #         counter +=1
# # print(counter)
 
# # PUNKT 4:
# for i in data:
#     if i == "!":
#         counter +=1
# print(counter)


# TASK 2:

# The user types in a list of integers and a number.
# Count how many times this number appears in the list. Print the result.
 
data = [1,2,3,4,4,4,4,4,4,4,5,6,7,5,5,5,5,5,5,5,58,9]
 
user_input = input("digit :")
 
count = 0
for i in data:
    if str(i) == user_input:
        count +=1
 
print(count)

# TASK 3:

# The user types in a list of integers. 
# Calculate the sum and average of these elements. 
# Print the result.

data = [1,2,3,4,56,7,8,9]
 
result = sum(data)
length = len(data)
avarage = result/length
print(result)
print(avarage)

# v2:

data = [1,2,3,4,5,5,5,5,5,5,5,5]
count = 0
count = 0
while True:
    user_input = input("Number :")
    if user_input in ["quit", "exit"]:
        print("list done")
        break
 
    data.append(int(user_input))

# v3?
search_num = int(input("search :"))
# count = data.count(search_num)
 
for i in data:
    if i == search_num:
        count += 1
print(count)
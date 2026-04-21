FRUIT = "banana" # global
 
def fruit_names():
    fruit = "mango" # enclosing
 
    def vegetable_name():
        veg = "cabbage" # local
       
        print(f"{fruit} is enclosing")
        print(f"{veg} is a local ")
   
    def greet():
        greet_me = "bonjour"
        print("helo there")
        print(f"{fruit} i am a enclosing variable")
 
    # print(f"{FRUIT} is a global variable")
   
    greet()
    vegetable_name()
 
    return f"{fruit} is a local variable"
 
x = fruit_names()
print(x)
 
# v2:
def say_hello():
    return "hello there"
 
greet = say_hello()
# print(greet)
 
def greet_user(name):
    return f"{greet} {name}"
 
print(greet_user("john"))


# TASK 7:

# Write a function that checks if a six-digit number is lucky. The number is passed as a parameter. 
# If the number is lucky, return true, otherwise false.
# A lucky six-digit number is a number with the sum of its first three digits being equal to the sum of its last three digits. 
# For example, 123420 is a lucky number because 1+2+3 = 4+2+0, and 723422 is not because 7+2+3 != 4+2+2.

num = input("please provide 6 digit number :")
 
def lucky_number(num):
    # first check 6 digits
    if len(str(num)) == 6:  
        # create 2 list
        first_three = num[:3]
        last_three = num[3:]
 
        first = []
        last = []
        for i in first_three:
            first.append(int(i))
        for j in last_three:
            last.append(int(j))
        if sum(first) == sum(last):
            return True
    return False




# v2 (BETTER):
x = lucky_number(num)
print(x)

def lucky_numr(num):
    num = str(num)          
 
    first_three = int(num[0]) + int(num[1]) + int(num[2])
    last_three = int(num[3]) + int(num[4]) + int(num[5])
 
    return first_three == last_three
print(lucky_number(723422))


# TASK 1:
# Write a function that calculates the sum of elements from a list of integers. The list is passed as a parameter.

# def sum_of_elements(lst):
#     return sum(lst)
 
 
def sum_of_element(lst):
    total = 0
    for i in lst:
        total +=i
    return total
 
x = sum_of_element([1,2,3,4,5,6])
print(x)

# TASK 2:
# Write a function to find the maximum in the list of integers. The list is passed as a parameter.


def max_of_elements(lst):
    maximum = lst[0]
 
    for i in lst:
        if i > maximum:
            maximum = i
 
    return maximum
 
 
x = max_of_elements([1, 2, 3, 4, 5, 6])
print(x)


# TASK 3:
# Write a function that determines the number of even, odd, positive, negative elements in the list of integers. 
# The list is passed as a parameter.


# V1 (CHAT):
def count_numbers(lista):  
    even = 0  
    odd = 0  
    positive = 0  
    negative = 0  
  
    for number in lista:  
        # Sprawdzamy parzyste/nieparzyste  
        if number % 2 == 0:  
            even += 1  
        else:  
            odd += 1  
  
        # Sprawdzamy dodatnie/ujemne  
        if number > 0:  
            positive += 1  
        elif number < 0:  
            negative += 1  
  
    print("Even:", even)  
    print("Odd:", odd)  
    print("Positive:", positive)  
    print("Negative:", negative)  
  
  
# Przykładowe wywołanie:  
count_numbers([1, -2, 3, -4, 5, 0, 8, -7])


# V2 (CHAT):

def count_numbers(lista):  
    even = 0  
    odd = 0  
    positive = 0  
    negative = 0  
      
    for number in lista:  
        if number % 2 == 0:  
            even += 1  
        else:  
            odd += 1  
          
        if number > 0:  
            positive += 1  
        elif number < 0:  
            negative += 1  
      
    return even, odd, positive, negative  
  
  
# Przykładowe wywołanie:  
e, o, p, n = count_numbers([1, -2, 3, -4, 5, 0, 8, -7])  
print("Even:", e)  
print("Odd:", o)  
print("Positive:", p)  
print("Negative:", n)


# V3 (Puskar):
def determine_number(lst):
    positive = 0
    negetive = 0
    even = 0
    odd = 0
    for i in lst:
        if i > 0:
            positive +=1
        elif i < 0:
            negetive += 1
    for j in lst:
        if j %2 ==0:
            even += 1
        else:
            odd += 1
    return f" even : {even} odd : {odd} positive : {positive} negetive : {negetive}"
 
x = determine_number([1,2,3,4,-2,-5,-8])
print(x)
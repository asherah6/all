# The user types in a number.
# Check if it is even or odd.
# If the number is even, print the number and the text "Even number."
# If the number is odd, print the number and the text "Odd number."


user_input = int(input("Number:"))

if user_input % 2 == 0 :
    print("Even Number")
else:
    print("odd number")

 
# The user types in a number.
# Check if it is a multiple of 7.
# If it is, print the number and the text "Your number is a multiple of 7."
# If it is not, print the number and the text "Your number is not a multiple of 7."

user_input = int(input("Number:"))

if user_input % 7 == 0 :
    print("Your number is a multiple of 7.")
else:
    print("Your number is not a multiple of 7.")

user_input1 = int(input("Number 1:"))
user_input2 = int(input("Number 2:"))

if user_input1 % 9 == 0:

    print("Maximum")
else:
    print("Not maxiumum")

num1 = int(input("User types the first number:"))
num2 = int(input("User types the second number:"))
 
if num1> num2:
    print(f"The maximum number is: {num1}")
elif num2> num1:
    print(f"the maximum number is: {num2}")
else:
    print("both numbers are equal")

# The user types in two numbers.
first_number = int(input("First Number :"))
second_number = int(input("Second Number :"))
 
# # Find the maximum of two numbers and print it.
 
if first_number > second_number:
    print(f"{first_number} is Greater than {second_number}")
elif first_number < second_number:
    print(f"{second_number} is Greater than {first_number}")
else:
    print("both numbers are equal")

# #The user types in two numbers. Find the minimum of two numbers and print it
# first_number = int(input("First Number :"))
# second_number = int(input("Second Number :"))
 
# # Find the maximum of two numbers and print it.
 
if first_number > second_number:
    print(f"{second_number} is smaller than {first_number}")
elif first_number < second_number:
    print(f"{first_number} is smaller than {second_number}")
else:
    print("both numbers are equal")

# #The user types in two numbers.# Based on the user's choice,

first_number = int(input("First Number :"))
second_number = int(input("Second Number :"))

# print the result of the sum,
print(f"sum :{first_number + second_number}")

# result = first_number + second_number
#     print(result)

# difference, product of these numbers or
result2 = first_number - second_number
print(result2)

# their arithmetic mean.
result3 = (first_number + second_number)/2
print(result3)


# The user types in two numbers.
 
first_number = int(input("First Number "))
second_number = int(input("Second Number "))
# Based on the user's choice,
# print the result of the sum,
sum = first_number + second_number
print(f"sum of {first_number} and {second_number} is {sum}")
 
# # difference,
 
print(f"difference : {abs(first_number - second_number)}")
 
if first_number < second_number:
    first_number, second_number = second_number, first_number
    print(f" difference is :{first_number - second_number}")
 
else:
    print(f" difference is :{first_number - second_number}")
 
 
# product of these numbers or
product = first_number * second_number
print(f"product of {first_number} and {second_number} is {product}")
# their arithmetic mean.
 
mean = (first_number + second_number)/2
print(f"the mean of {first_number} and {second_number} is {mean}")
 
 
 
 

 
a = 10
b = 15
print(f"a :{a}")
print(f"b :{b}")
a, b = b, a
 
print(f"a :{a}")
print(f"b :{b}")
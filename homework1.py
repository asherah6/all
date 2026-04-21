#TASK 1:

# The user types in three numbers.
 
first_number = int(input("First Number "))
second_number = int(input("Second Number "))
third_number = int(input("Third Number "))
# Based on the user's choice,

# print the result of the sum,
sum = first_number + second_number + third_number
print(f"sum of {first_number} and {second_number} and {third_number} is {sum}")
 
# product of these numbers
product = first_number * second_number * third_number
print(f"product of {first_number} and {second_number} and {third_number} is {product}")



#TASK 2:

# The user types in three numbers. Based on the user's choice, 
first_number = int(input("First Number "))
second_number = int(input("Second Number "))
third_number = int(input("Third Number "))


# the program prints a maximum of three, 

maximum = max(first_number, second_number, third_number)
print(maximum)

# a minimum of three, 

minimum = min(first_number, second_number, third_number)
print(minimum)

# or arithmetic mean of three numbers.

arithmetic_mean = (first_number + second_number + third_number)/3
print(arithmetic_mean)


#TASK 3:

#The user types in the number of meters. Based on the user's choice,

user_type = int(input("Numbers_of_meters "))

#the program converts meters to miles, inches, or yards.

miles = (user_type / 1609.344)
print(miles)

#inches:
inches = (user_type* 39.3701)
print(inches)

#yards:
yards = (user_type* 1.09361)
print(yards)


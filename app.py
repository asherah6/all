print("hello Adrianna")
print()
print("hello Adrianna")
print("hello \n Adrianna")
print("hello Adrianna" + "how are You?")
print("hello Adrianna" , "how are You?")
print("hello Adrianna" + "how are You?" , "187638" + " true")

# - linijka zostanie pominięta
# variable no with numbers, bloomlop and float
# - \n - enter lub \t -> tab
# "Anyone who
#   stops
#     learning is old,
#        whether at twenty or eighty
#                       Henry Ford"

print("Nothing \nwill work \nunles you do")
print('"Anyone who \n    stops \n      learning is old, \n        whether at twenty or eighty \n                        Henry Ford"')
print("""A# "Anyone who
   stops
     learning is old,
        whether at twenty or eighty
                      Henry Ford""")


x= 2
y= 5
z= x + y

print(x + y)
print(y - x)
print(y / x)
print(y * x)
print(z)

print(f"sum :{x+ y}")
# print("sum :", x+y)

x= 50

print(x * 0.1)


# The user types in two numbers.
# The first number is a value, and the second is a percentage to be calculated.
# Let's say we typed in 50 and 10. The displayed number should be 10% of 50. Result: 5.
 
 
x = int(input(f"first Number :"))
y = int(input(f"second Number :"))
 
result = (x * y)/100
 
print(result)

name = input("name : ")
print(f"Name is {name}")

# Write a program that calculates the area of a rectangle.
# The user types in the width and height of the rectangle.
 
height  =  float(input( "Height :"))
width  =  int(input( "Width :"))
 
result = height * width
print(result)
 
x= "5"
y= 10
# z= x + y
h= x * y

# print(x + y)
# print(y - x)
# print(y / x)
# print(y * x)

print(h)


year = int(input("year :"))
 
# leap year is a year when february has 29 days
 
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("Year", year, "is leap")
else:
    print(False)


# The user types in a two-digit number. For example,
# 26. Display the value of the first and second digit on different lines. In our case,
# it will be as follows:
# 2
# 6
 
user_input  = input("number :")
print(f"{user_input[0]}\n{user_input[1]}")


# The user types in Celsius temperature.
# Convert it to Fahrenheit and display the result on the screen.
 
# fahrenheiht = (celcius  * 1.8)+32

# user_input = float(input("Celcius :"))
# print(((user_input) * 1.8) + 32)

celcius = float(input("calcius :"))
 
fahrenheiht = (celcius  * 1.8) + 32
 
print(fahrenheiht)
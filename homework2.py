
# # Task 1
# # The user types in a number from 1 to 7 that represents a day of the week. 


# day = int(input("Enter a number from 1 to 7: "))

# # Print its name. For example, if the number is 1, then you should display "Monday"; if 2, display "Tuesday," etc.

# if day == 1:
#     print("Monday")
# elif day == 2:
#     print("Tuesday")
# elif day == 3:
#     print("Wednesday")
# elif day == 4:
#     print("Thursday")
# elif day == 5:
#     print("Friday")
# elif day == 6:
#     print("Saturday")
# elif day == 7:
#     print("Sunday")
   
# else:
#     print("Enter a number from 1 to 7")


# Task 2
# The user types in a number from 1 to 12 that represents a month. 

# month = int(input("Enter a number from 1 to 12: "))

# # Print its name. For example, if the number is 1, display "January"; if 2, display "February," etc.

# if month == 1:
#     print("January")
# elif month == 2:
#     print("February")
# elif month == 3:
#     print("March")
# elif month == 4:
#     print("April")
# elif month == 5:
#     print("May")
# elif month == 6:
#     print("June")
# elif month == 7:
#     print("July")
# elif month == 8:
#     print("August")
# elif month == 9:
#     print("September")
# elif month == 10:
#     print("October")
# elif month == 11:
#     print("November")
# elif month == 12:
#     print("December")
   
# else:
#     print("Enter a number from 1 to 12")



# Task 3
# The user types in a number. 
# If the number is greater than 0, 
# print "Your number is positive"; if it is less than zero, 
# print "Your number is negative"; if it is equal to 0, print "Your number is equal to zero."


# user_input = int(input("Number:"))

# if user_input > 0:
#     print("Your number is positive")
# elif user_input == 0:
#     print("Your number is equal to zero")
# else:
#     print("Your number is negative")


# Task 4
# The user types in two numbers. Determine if these numbers are equal. If they are not, print them in ascending order.

user_input1  = int(input("1 number :"))
user_input2  = int(input("2 number :"))

if range(user_input1) == range(user_input2):
    print("Numbers are equal.")
elif user_input2 > user_input1:
    print(user_input1, user_input2)
elif user_input1 > user_input2:
    print(user_input2, user_input1)

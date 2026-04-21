# The user types in a six-digit number. Write a program that determines if this number is lucky. 
# (A lucky number is a six-digit number with the sum of its first three digits being equal to the sum of its last three digits.)
# For example, 123321 is a lucky number because 1+2+3 = 3+2+1.
# But 378423 is not a lucky number because 3+7+8 != 4+2+3.
# If the user typed in a non-six-digit number, display an error message.
 
numbers = input("please provide six digit number :")
first_three = numbers[:2]
last_three = numbers[2:]

#v1
 
# if int(first_three[0]) + int(first_three[1]) + int(first_three[2]) == int(last_three[0]) + int(last_three[1]) + int(last_three[2]):
#     print("lucky")
# else:
#     print("unlucky")

#v2

if len(numbers) < 6 or len(numbers) > 6:
    print("please provide exact 6 digit number")
 
else:
    first_three = numbers[:2]
    last_three = numbers[2:]
 
    first_section = 0
    second_section = 0
 
    for i in first_three:
        first_section += int(i)
    for j in last_three:
        second_section += int(j)
 
    if first_section == second_section:
        print("lucky number")
    else:
        print("unlucky")

# The user types in a six-digit number. Swap the first and the sixth digits, as well as the second and the fifth.
# For instance, 723895 should become 593827.
# If the user typed in a non-six-digit number, display an error message.
 
number = "123456"
a = ""
 
for i in range(len(number)):
    if i == 0:
        a += number[5]
    elif i == 1:
        a += number[4]
    elif i == 5:
        a += number[0]
    elif i == 4:
        a += number[1]
    else:
        a += number[i]
print(a)

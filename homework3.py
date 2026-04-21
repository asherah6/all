# TASK 1:

# The user types in two numbers. 

a = int(input("Number 1:"))
b = int(input("Number 2:"))

sum_even = 0
count_even = 0

sum_odd = 0
count_odd = 0

sum_9 = 0
count_9 = 0

# Find the sum of all even, odd numbers and multiples of 9 in the specified range, 

start = min(a, b)
end = max(a, b)

for x in range(start, end + 1):
    if x % 2 == 0:
        sum_even += x
        count_even += 1
    else:
        sum_odd += x
        count_odd += 1

    if x % 9 == 0:
        sum_9 += x
        count_9 += 1

# as well as arithmetic mean of each group.

avg_even = sum_even / count_even if count_even != 0 else 0
avg_odd = sum_odd / count_odd if count_odd != 0 else 0
avg_9 = sum_9 / count_9 if count_9 != 0 else 0

print("Parzyste: suma =", sum_even, "średnia =", avg_even)
print("Nieparzyste: suma =", sum_odd, "średnia =", avg_odd)
print("Wielokrotności 9: suma =", sum_9, "średnia =", avg_9)


#TASK 2:
# The user types in the length of a line and a symbol to fill the line. 
# Print a vertical line made out of the typed in symbol of the specified length.

length = int(input("Podaj długość linii: "))  
symbol = input("Podaj symbol: ")  
  
for i in range(length):  
    print(symbol)


# TASK 3:

# The user types in numbers. If the number is greater than 0, print "Your number is positive"; 
# if it is less than zero, print "Your number is negative"; if it is equal to 0, print "Your number is equal to zero.
# " When the user types in 7, the program stops and prints "Good bye!"

number = int(input("Provide the number: "))

while number != 7:

    if number > 0:
        print("Your number is positive")
    elif number < 0:  
        print("Your number is negative")
    else:
        print("Your number is equal to zero")

    number = int(input("Provide number again: "))
 
print("Good bye!")

# TASK 4:

# The user types in numbers. 
# The program must calculate their sum and find the maximum and minimum. 
# When the user types in 7, the program stops and prints "Good bye!".

number = int(input("Provie the number: "))

if number == 7:
    print("Good bye!")
else:
    suma = number
    maximum = number
    minimum = number

    while number != 7:
    
        suma += number
        if number > maximum:
            maximum = number
        if number < minimum:
            minimum = number
     
        number = int(input("Provide another number: "))

    print("Suma:", suma)
    print("Maksimum:", maximum)
    print("Minimum:", minimum)
    print("Good bye!")
# TASK 1:
# Write a function that prints formatted text given below:
# "Don't compare yourself with anyone in this world...
#  if you do so, you are insulting yourself."
#                                           Bill Gates

def print_quote():
    print("\"Don't compare yourself with anyone in this world...")
    print(" if you do so, you are insulting yourself.\"")
    print("                                          Bill Gates")
  
print_quote()



# TASK 2:
# Write a function that takes two numbers as a parameter and displays all even numbers in between.

def even_numbers(a, b):
    for number in range(a, b + 1):
        if number % 2 == 0:
            print(number)

even_numbers(1, 20)

# v2:

def even_numbers_list(a, b):
    result = []
    for number in range(a, b + 1):
        if number % 2 == 0:
            result.append(number)
    return result

print(even_numbers_list(1, 20))



# TASK 3:
# Write a function that prints an empty or solid square made out of some symbol. 
# The function takes the following as parameters: the length of the side of the square, a symbol, and a boolean variable:

    # if it is True, the square is solid;
    # if False, the square is empty.

def draw_square(side, symbol, is_solid):
    for i in range(side):
        if is_solid or i == 0 or i == side - 1:
            print(symbol * side)
        else:
            print(symbol + " " * (side - 2) + symbol)

print("Solid square:")
draw_square(5, "*", True)

print("\nEmpty square:")
draw_square(5, "*", False)



# TASK 4:
# Write a function that returns the smallest of five numbers. 
# Numbers are passed as parameters.

def smallest_of_five(a, b, c, d, e):
    return min(a, b, c, d, e)

print(smallest_of_five(10, 3, 7, 1, 9))

# V2 - manual:

def smallest_of_five(a, b, c, d, e):
    smallest = a
    if b < smallest:
        smallest = b
    if c < smallest:
        smallest = c
    if d < smallest:
        smallest = d
    if e < smallest:
        smallest = e
    return smallest

print(smallest_of_five(10, 3, 7, 1, 9))



# TASK 5:
# Write a function that returns the product of numbers in a specified range. 
# The start and end points of the range are passed as parameters. 
# If the order of these points is incorrect (e.g., 5 is the end, and 25 is the start), swap them.

def product_in_range(start, end):

    if start > end:
        start, end = end, start

    result = 1

    for number in range(start, end + 1):
        result *= number
    return result

print(product_in_range(2, 5))



# TASK 6:
# Write a function that counts how many digits a number has. 
# The number is passed as a parameter. 
# Return the received number of digits from the function. 
# For example, if the passed number is 3456, it has 4 digits.

def count_digits(number):
    if number == 0:
        return 1

    count = 0
    number = abs(number)

    while number > 0:
        number //= 10
        count += 1

    return count

print(count_digits(3456))

# V2:

def count_digits(number):
    return len(str(abs(number)))

print(count_digits(3456))



# TASK 7:
# Write a function that checks if a number is a palindrome. 
# The number is passed as a parameter. If the number is a palindrome, return true, otherwise false.
# A palindrome is a number which reads the same backward as forward. 
# For instance, 123321 is a palindrome, 546645 is a palindrome, but 421987 is not.

def is_palindrome(number):
    number = abs(number)
    
    original = number
    reversed_num = 0

    while number > 0:
        reversed_num = reversed_num * 10 + number % 10
        number //= 10
    
    return original == reversed_num

print(is_palindrome(12321))

# v2:

def is_palindrome(number):
    text = str(abs(number))
    return text == text[::-1]

print(is_palindrome(12321))

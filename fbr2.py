# recursion is a method where function calls itself
# recursion stands for re occurance (repeating itself)
# everytime function will call itself the problem will get smaller
 
 
def get_number(n):
    if n == 0:
        print("break")
    else:
        print(n)
        get_number(n-1)
       
 
# get_number(10)

#  v2:

n =5
while n >= 0:
    print(n)
    n -= 1
 
 
 
def get_number(n):
    if n == 0:
        print("break")
    else:
        print(n)
        get_number(n -1)
 
# get_number(5)

#  V3:

n =5
total = 0
while n >= 1:
    print(n)
    total += n
    n -= 1
 
print(total)
 
def total(n):
    if n == 1:
        return 1
    else:
        return n + total(n -1)
    
# EXAMPLE:

data = "p u s h k a r"
 
def reverse_string(str):
    return str[::-1]
print(reverse_string(data))
 
def reverse_it(str):
    if len(str) == 1:
        return str
    else:
        return reverse_it(str[1:]) + str[0]
 
x = reverse_it(data)
print(x)


# exmpl 2:
# sum of the list:

data = [1,2,3,4,5,6]
data = []
 
def sum_of_list(lst):
    if lst == []:
        return 0
    else:
        return lst[0] + sum_of_list(lst[1:])
 
x = sum_of_list(data)
print(x)
 

# exmple 3:
# multiplication:

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
 
x = factorial(5)
print(x)


# fibbonacci
# 0,1,1,2,3,5,8,13,21...
 
def fibbonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fibbonacci(n -1) + fibbonacci(n - 2)
  
data  = []
for i in range(8):
    z = fibbonacci(i)
    data.append(z)
    print(data)
      
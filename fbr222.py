# LEGB :

DATA = 500 # global
 
def outer():
    data= 50 #enclosing
 
    def inner():
        my_data = 5 #local
        print(data)
        print(my_data)
        print(DATA)
 
    inner()
    print(data)
    # print(my_data)
    print(DATA)
 
 
# print(data)
outer()

# recursion

# 0 7
# 0+1+2+3+4+5+6+7
n =5
total = 0
for i in range(1, n+1):
    total += i
# print(total)
 
def add_num(n):
    if n == 0:
        return 0
    else:
       return n + add_num(n-1)
 
print(add_num(5))


# define a function that takes n, power as parameter
# use recursion

def p(n,power):
    if power == 0:
        return 1
    else:
       return n * p(n,power-1)
       
print(p(4,7))

# v2 while:
n = 3
power = 3
total = 1
while power > 0:
    total *= n
    power -=1
 
print(total)

# v3 for:
n = 4
power = 2
 
total = 1
for i in range(1, power+1):
    total *= n
 
print(total)


# v4:
def make_power(n, power):
    if power == 0:
        return 1
    else:
        return n * make_power(n, power-1)
            #  4 * make_power(4, 2)
            #  4 * make_power(4, 1)
            #  4 * 1
   
# 4 * 4
# 4 * 4 * 4
 
x = make_power(4, 3)
print(x)
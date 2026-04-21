# BUBBLE SORT:

data = [14,3,2,5,8,-2,0]
 
def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(n -1):        
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j +1], lst[j]
    return lst
 
x = bubble_sort(data)
print(x)

# DECORATOR:

def starmaker(func):
    def wrapper():
        print(5 * "*")
        func()
        print(5 * "*")
    return wrapper
 
@starmaker
def say_hello():
    print("hello")
 
say_hello()


from datetime import datetime
 
def starmaker(func):
    def wrapper():
        print(5 * "*")
        print(func())
        print(5 * "*")
       
    return wrapper
 
@starmaker
def say_hello():
    now = datetime.now()
    return now.strftime("%H:%m")
   
 
print(say_hello())
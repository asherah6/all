# OOP: Magic, private, dunder methods (public, private, ):

class Human:
    
    __data = "123456"
 
    def __human_info(self):
        return "human are awesome"
    
    def get_info(self):
        return "nothing"
    
human = Human()


# podjówna podłoga __ -> oznacza private:

# v2:

import random
 
class Country:
    _id = f"34251{random.randint(1, 5)}"
 
    def _data(self):
        _id = 2341
        return _id
 
    def __init__(self, country_name):
        self.country_name = country_name
 
    def __str__(self):
        return f"country : {self.country_name}"
    
    def __len__(self):
        return 20000
 
 
country = Country("poland")
print(country._id)
print(country._data())
 

# v3:

class WalletFunctor:
    def __init__(self, startCoins = 100):
        self.__startCoins = startCoins
    
    def __call__(self, coins = 0):
        return self.__startCoins+coins
    
    
wallet = WalletFunctor()
print(wallet(50))

# TASK 1:

# create student classs
# student have access to 4 classes computer science math english
# create different id for each class
# use random
# use private method
# use __str__ method to show string representation

import random
 
class Student:
    def __init__(self):
        self.__id = random.randint(1, 1000)

    def computer(self):
        return f"{self.__id + 11}11"
 
    def science(self):
        return f"{self.__id}22"
 
    def math(self):
        return f"{self.__id}33"
 
    def english(self):
        return f"{self.__id}44"

    def __str__(self):
        return f"student's Computer id: {self.computer()} math id: {self.math()}"

student = Student()

print(student)
print(student.computer())
print(student.science())
print(student.math())
print(student.english())


# TASK 2:

class Data1:
    def say_hello(self):
        return f"hello from data 1"
    
class Data2:
    def say_hello(self):
        return f"hello from data 2"
    
class Data3:
    def say_hello(self):
        return f"hello from data 3"
    
class Data4(Data1,Data2,Data3):
    def __str__(self):
        return f"{Data1.say_hello()} {Data2.say_hello()} {Data3.say_hello()}"
    
 
data = Data4()
print(data)
print(data.say_hello())
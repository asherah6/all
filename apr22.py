# OOP, CLASS METHOD:

class Person:
    def __init__(self, name):
        self.name = name
   
    @classmethod
    def showdata(cls, data):
        name = data.split("-")
        name = data
        return cls(name)
   
person = Person.showdata("john-45")
person1 = Person("johnny-45")
# print(type(person.name))
# print(person1.name)
print(person.name)

# V2:

class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
 
    @classmethod
    def getinfo(cls,name, age, gender):
        age = age + 20
        return cls(name, age, gender)
 
    def showinfo(self):
        return f"{self.name} age: {self.age} gender : {self.gender}"
 
person = Person.getinfo("john", 45, "male")
print(person.age)
 
person1 = Person("john", 45, "male")
print(person1.showinfo())
print(person.showinfo())

#  TASK 1:

# Implement a class Human. Class fields should store the following: 
# full name, date of birth, contact number, city, country, home address. 
# Implement class methods for data input and output, 
# provide access to individual fields through class methods.

from datetime import datetime
 
class Human:
    def __init__(self, name, date_of_birth, city, country):
        self.name = name
        self.date_of_birth = date_of_birth #yyyy/mm/dd
        self.city = city
        self.country = country
 
 
    def showinfo(self):
        return f"name : {self.name} age : {self.date_of_birth} city : {self.city} country : {self.country} "
 
    @classmethod
    def info_data(cls, name, date_of_birth, city, country):
        # date_object = datetime.strptime(date_string, "%d %B, %Y")
        dob = datetime.strptime(date_of_birth, "%Y/%m/%d")
        today = datetime.now()
        age= today.year - dob.year
        return cls(name, age, city, country )
 
 
human = Human("john", "1990/07/23", "warsaw", "poland")
print(human.showinfo())
human1 = Human.info_data("john", "1990/07/23", "warsaw", "poland")
print(human1.showinfo())
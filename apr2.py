# OOP:

# EXMPL:

class Passport:
    def __init__(self, name, nationality, passport_number):
        self.name = name
        self.nationality = nationality
        self.passport_number = passport_number
 
    def show_info(self):
        return (f"Name: {self.name}, "
                f"Nationality: {self.nationality}, "
                f"Passport Number: {self.passport_number}")
    
# EXP 2:

class Student:
    def __init__(self, name, age):
        self.name= name
        self.age = age
        self.subjects = []
 
    def add_subject(self, subject):
        self.subjects.append(subject)
       
 
student = Student("john", 45)
student.add_subject("math")
student.add_subject("english")
student.add_subject("science")
student.add_subject("geography")
for subject in student.subjects:
    print(f"{student.name} has subjects :{subject}")

# EMP 3:

class Student:
    def __init__(self, name, age):
        self.name= name
        self.age = age
        self.subjects = []
 
    def get_info(self):
        return f"name is {self.name} age is : {self.age}"
   
 
class Teacher(Student):
    def __init__(self, name, age):
        self.name = name
        self.age = age
 
    # def get_info(self):
    #     return "teacher is fantastic"
       
 
student = Student("john", 45)
teacher = Teacher("johnny", 55)
 
print(student.get_info())
print(teacher.get_info())


# EMP 4:

class Calculator:
    def __init__(self, x, y):
        self.x = x
        self.y = y
 
    def add(self):
        return self.x + self.y
   
class AdvanceCalculator(Calculator):
    def __init__(self, x , y):
        self.x = x
        self.y = y
 
    def add(self):
        return super().add() + self.x * self.y
   
 
calculator = Calculator(2,3)
ad_calculator = AdvanceCalculator(2,3)
 
print(calculator.add())
print(ad_calculator.add())


# TASK 1:

# Implement a class Human. Class fields should store the following:
#  full name,  contact number,
# city, country
#  Implement class methods for data input and output,
#  provide access to individual fields through class methods.
 
# Supplement the Human class with a constructor,
# as well as the required overloaded methods.
 
 
class Human:
    def __init__(self, name, number, city, country):
        self.name = name
        self.number = number
        self.city = city
        self.country  = country
 
    def get_info(self):
        return f"name : {self.name} \nnumber :{self.number} \ncity : {self.city} \ncountry : {self.country}"
   
    def __str__(self):
        return f"name : {self.name} \nnumber :{self.number} \ncity : {self.city} \ncountry : {self.country}"
 
 
class Person(Human):
    def __init__(self, name, number, city, country):
        self.name = name
        self.number = number
        self.city = city
        self.country  = country
 
    def get_info(self):
        return f"name {self.name}"
 
human = Human("john", "123456", "warsaw", "poland")
 
print(human.get_info())


# TASK 2:

# Create a class Human that will contain info about a human.
# Use inheritance to create a Builder class (contains info about a builder), 
# a Sailor class (contains info about a sailor), 
# a Pilot class (contains info about a pilot).
# Each class must have the required methods.
# OVERLOADING

class Human:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height
   
    def running(self):
        return f"{self.name} runs"
 
    def get_info(self):
        return f"name : {self.name} \nage :{self.age} \nheight : {self.height}"

human = Human("john", "123456", "warsaw", "poland")

class Builder(Human):
    def __init__(self, name, age, height):
        super().__init__(name, age, height)
   
    def builds(self):
        return f"{self.name} builds very good building"

def get_info(self):
        return f"Builder_name : {self.name} \nage :{self.age} \nheight : {self.height}"

builder = Builder("john", 45, 175)

class Sailor(Human):
    def __init__(self, name, age, height):
        super().__init__(name, age, height)
    
    def sailing(self):
        return f"{self.name} sailing on the sea once in a month"
    
    def get_info(self):
        return f"Sailor_name : {self.name} \nage :{self.age} \nheight : {self.height}"

sailor = Sailor("Jan", 55, 185)


class Pilot(Human):
    def __init__(self, name, age, height):
        super().__init__(name, age, height)

    def piloting(self):
        return f"{self.name} pilot the plane yesterday"
    
    def get_info(self):
        return f"Pilot_name : {self.name} \nage :{self.age} \nheight : {self.height}"

pilot = Pilot("Cris", 35, 180)

# print(builder.builds())
# print(builder.running())
# print(sailor.sailing())
# print(pilot.piloting())
print(human.get_info())
print(builder.get_info())
print(sailor.get_info())
print(pilot.get_info())


# TASK 3:

# Create a base class Animal and derived classes Tiger, Crocodile, Kangaroo. 
# Use a constructor to set the name of each animal and its characteristics. 
# Create the required methods and fields for each class.

class Animal:
    def __init__(self, species, sex, weight):
        self.species = species
        self.sex = sex
        self.weight = weight
    
    def get_info(self):
        return f"species : {self.species} \nsex : {self.sex} \nweight : {self.weight}"

class Tiger(Animal):
    def __init__(self, species, sex, weight):
        self.species = species
        self.sex = sex
        self.weight = weight

def get_info(self):
        return f"species : {self.species} \nsex : {self.sex} \nweight : {self.weight}"

tiger = Tiger("Tiger", "Female", 100) 

class Crocodile(Animal):
    def __init__(self, species, sex, weight):
        self.species = species
        self.sex = sex
        self.weight = weight

    def get_info(self):
        return f"species : {self.species} \nsex : {self.sex} \nweight : {self.weight}"

crocodile = Crocodile("Crocodile", "Male", 100) 

class Kangaroo(Animal):
    def __init__(self, species, sex, weight):
        self.species = species
        self.sex = sex
        self.weight = weight

    def get_info(self):
        return f"species : {self.species} \nsex : {self.sex} \nweight : {self.weight}"

kangaroo = Kangaroo("Kangaroo", "Male", 80) 

print(tiger.get_info())
print(crocodile.get_info())
print(kangaroo.get_info())

# OOP - objects

# EXMPL:

class Person:
    def __init__(self, firstName, lastName, age):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age
 
    def getInfo(self):
        return f"Person first name -  {self.firstName}; last name - {self.lastName}; age - {self.age}."
 
class Employee(Person):
    def __init__(self, firstName, lastName, age, jobTitle, salary, seniority):
        super().__init__(firstName, lastName, age)
        self.jobTitle = jobTitle
        self.salary = salary
        self.seniority = seniority
   
    def getInfo(self):        
        return  super().getInfo() + f"\njobTitle - {self.jobTitle}; salary - {self.salary}; seniority - {self.seniority}."
 
 
 
# employee1 = Employee("Kate", "Smith", 20, "HR", 2500, 7)
 
# print(employee1.getHi("Hello"))
# print(employee1.getInfo())
 
 
person = Person("John", "Doe", "22")
# print(person.getInfo())
employee = Employee("John", "Doe", "22","manager", 5000, 8)
# print(employee.firstName)
print(employee.getInfo())


# TASK 1:

# Create a class Human that will contain info about a human.
# Use inheritance to create a Builder class (contains info about a builder),
# a Sailor class (contains info about a sailor),
# a Pilot class (contains info about a pilot).
# Each class must have the required methods.
 
class Human:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height
   
    def running(self):
        return f"{self.name} runs"
 
 
class Builder(Human):
    def __init__(self, name, age, height):
        super().__init__(name, age, height)
   
    def builds(self):
        return f"{self.name} builds very good building"
 
builder = Builder("john", 45, 175)

class Sailor(Human):
    def __init__(self, name, age, height):
        super().__init__(name, age, height)
    
    def sailing(self):
        return f"{self.name} sailing on the sea once in a month"

sailor = Sailor("Jan", 55, 185)

class Pilot(Human):
    def __init__(self, name, age, height):
        super().__init__(name, age, height)

    def piloting(self):
        return f"{self.name} pilot the plane yesterday"

pilot = Pilot("Cris", 35, 180)

print(builder.builds())
print(builder.running())
print(sailor.sailing())
print(pilot.piloting())


# TASK 2:

# Create a class Passport that will contain passport information about a citizen of a given country.
# Use inheritance to create a ForeignPassport class derived from Passport.
# Recall that a foreign passport has not only passport information but also data on visas and the number of the foreign passport.
# Each class must have the required methods.

# class Passport:
#     def __init__(self, citizen_country, given_country):
#         self.citizen_country = citizen_country
#         self.given_country = given_country



# class ForeignPassport(Passport):



class Passport:
    def __init__(self, name, nationality, passport_number):
        self.name = name
        self.nationality = nationality
        self.passport_number = passport_number
 
    def show_info(self):
        return (f"Name: {self.name}, "
                f"Nationality: {self.nationality}, "
                f"Passport Number: {self.passport_number}")

 
class ForeignPassport(Passport):
    def __init__(self, name, nationality, passport_number, foreign_passport_number):
        super().__init__(name, nationality, passport_number)
        self.foreign_passport_number = foreign_passport_number
        self.visas = []  # list of visas
 
    def add_visa(self, country):
        self.visas.append(country)
 
    def show_visas(self):
        if not self.visas:
            return f"{self.name} has no visas"
        return f"Visas for {self.name}: {', '.join(self.visas)}"
 
    def show_foreign_info(self):
        base = self.show_info()
        return (f"{base}, Foreign Passport Number: {self.foreign_passport_number}")

fp = ForeignPassport("Karol", "Polish", "PL123456", "FP987654")
 
fp.add_visa("USA")
fp.add_visa("Japan")
 
print(fp.show_foreign_info())
print(fp.show_visas())




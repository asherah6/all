# OOP static methods:

# TASK 1:
# Add a static method to the Human class that when called returns the number of created Human class objects.

class Human:
    counter = 0
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        Human.counter += 1  #pointer to the class object
 
    def show_info(self):
        return f"{self.name} is {self.age} years old"
   
    @staticmethod
    def show_data():
        return Human.counter
 
   
 
human = Human("john", 54, "male")
human1 = Human("johnny", 45, "male")
human2 = Human("johnny", 45, "male")
human3 = Human("johnny", 45, "male")
human4 = Human("johnny", 45, "male")
human5 = Human("johnny", 45, "male")
 
print(human1.show_data())

# TASK 2:
# Create a class to calculate the area of geometric shapes. 
# The class should provide functionality for calculating the area of a triangle using various formulas, 
# the area of a rectangle, the area of a square, the area of a rhombus. 
# Class methods for calculating the area should be implemented with static methods. 
# The class should also count the number of calculations and return that value using a static method.

class Geometry:
    counter = 0
    def __init__(self, radius, length, width, side):
        self.radius = radius
        self.length = length
        self.width = width
        self.side = side
        Geometry.counter += 1
 
    def area_of_rectangle(self):
        return f"area of rectangle is : {self.length * self.width}"
   
    def area_of_square(self):
        return f"area of square is : {self.side**2}"
   
    def area_of_circle(self):
        return f"area of circle is : {3.14* self.radius **2}"
   
    @staticmethod
    def check_counter():
        return Geometry.counter
   
 
rectangle = Geometry(10,5,6,8)
square     = Geometry(10,5,6,8)
circle = Geometry(10,5,6,8)
 
print(rectangle.check_counter())


# TASK 3:

# Create a class to find the largest and the smallest of four arguments,
# the average,
# and the factorial.
# Implement this functionality as static methods.

class Mathematics:
 
    @staticmethod
    def find_the_largest(a,b,c,d):
        return f"Largest: {max(a,b,c,d)}"
 
    @staticmethod
    def find_the_smallest(a,b,c,d):
        return f"Smallest: {min(a,b,c,d)}"
 
    @staticmethod
    def factorial(a):
        counter = 1
        if a < 1:
            return 1
        for i in range(2, a +1):
            counter *= i
        return counter
 
    @staticmethod
    def average(a,b,c,d):
        return f"Average: {(a + b + c + d) / 4}"
 
 
print(Mathematics.find_the_largest(1,2,3,4))
print(Mathematics.find_the_smallest(1,2,3,4))
print(Mathematics.factorial(5))
print(Mathematics.average(1,2,3,4))
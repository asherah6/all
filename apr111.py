# OOP - SUPER METHOD / MRO = multiple inherence method:

# v1:
class myBook:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
       
    def showBookInfo(self):
        print("Title: {}".format(self.title))
        print("Author: {}".format(self.author))
        print("Pages: {}".format(self.pages))
 
class myFile:
    def __init__(self, fileSize, src):
        self.fileSize = fileSize
        self.src = src    
       
    def showFileProps(self):
        print("File size: {}".format(self.fileSize))
        print("File source: {}".format(self.src))
 
class myEBook(myBook,myFile):
    def __init__(self, title, author, pages,fileSize, src):
        super().__init__(title, author, pages)
        myFile.__init__(self,fileSize, src)
 
   
 
eBook1 = myEBook("Python Crash Course", "Eric Matthes", 624,1024, "www.mumbojumbo.com")
print(eBook1.showBookInfo())
print(eBook1.showFileProps())


# TASK 1:

# Use multiple inheritance to develop a class Car. 
# There should also be these classes: Wheels, Engine, Doors, etc.

class Car:
    def __init__(self, model):
        self.model = model

class Wheels:
    def __init__(self, size):
        self.size = size
        
class Engine:
    def __init__(self, power):
        self.power = power
        
class Doors:
    def __init__(self, amount):
        self.amount = amount
    
class Info(Car, Wheels, Engine, Doors):
    def __init__(self, model, size, power, amount):
        super().__init__(model)
        Wheels.__init__(self, size)
        Engine.__init__(self, power)
        Doors.__init__(self, amount)

    def show_info(self):
        print("Model: {}".format(self.model))
        print("Wheels_size: {}".format(self.size))
        print("Power: {}".format(self.power))
        print("Doors_amount: {}".format(self.amount))

info = Info("Audi", "20'", "200KM", 5)
# print(info.show_info())
info.show_info()


# v2:

class myBook:
    def __init__(self, title, author, pages, **kwargs):
        self.title = title
        self.author = author
        self.pages = pages
        super().__init__(**kwargs)
    def showInfo(self):
        print("Title: {}".format(self.title))
        print("Author: {}".format(self.author))
        print("Pages: {}".format(self.pages))
 
class myFile:
    def __init__(self, fileSize, src, **kwargs):
        self.fileSize = fileSize
        self.src = src
        super().__init__(**kwargs)
    def showData(self):
        print("File size: {}".format(self.fileSize))
        print("File source: {}".format(self.src))
 
class myEBook(myBook,myFile):
    def __init__(self, title, author, pages, fileSize, src, name):
        self.name = name
        super().__init__(title=title,author=author,pages=pages,fileSize=fileSize,src=src)
 
eBook1 = myEBook("Python Crash Course", "Eric Matthes", 624, 1024, "https://www.amazon.co.uk/dp/1593276036/?tag=adnruk-21", "john doe")
# eBook1.showData()
# eBook1.showInfo()
print(eBook1.name)

# TASK 3:

# Create a base class Pet and derived classes Dog, Cat, Parrot, Hamster. 
# Use a constructor to set the name of each animal and its characteristics. 
# Implement the following methods for each class:
# Sound — makes the sound of an animal (type in the console);
# Show — shows the name of an animal;
# Type — shows the name of its subspecies.


class Pet:
    def __init__(self, name, characteristics):
        self.name = name
        self.characteristics = characteristics
 
class Dog(Pet):
    def __init__(self, name, characteristics):
        super().__init__(name, characteristics)
   
    def sound(self):
        return "woof woof"
   
    def show(self):
        return self.name
   
    def type(self):
        return self.characteristics
   
class Cat(Pet):
    def __init__(self, name, characteristics):
        super().__init__(name, characteristics)
   
    def sound(self):
        return "meao meao"
   
    def show(self):
        return self.name
   
    def type(self):
        return self.characteristics

class Parrot(Pet):
    def __init__(self, name, characteristics):
        super().__init__(name, characteristics)
   
    def sound(self):
        return "Hello"
   
    def show(self):
        return self.name
   
    def type(self):
        return self.characteristics

class Hamster(Pet):
    def __init__(self, name, characteristics):
        super().__init__(name, characteristics)
   
    def sound(self):
        return "Pipi"
   
    def show(self):
        return self.name
   
    def type(self):
        return self.characteristics
    

dog = Dog("Tommy", "German chepard")
cat = Cat("Kitty", "Persian")
parrot = Parrot("Jack", "Kakadu")
hamster = Hamster("Misia", "Domowy")

print(dog.show())
print(dog.type())
print(dog.sound())
 
print(cat.show())
print(cat.type())
print(cat.sound())

print(parrot.show())
print(parrot.type())
print(parrot.sound())

print(hamster.show())
print(hamster.type())
print(hamster.sound())
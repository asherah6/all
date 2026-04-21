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
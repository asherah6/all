# MRO revision + GitHub:

class A:
    def __str__(self):
        return "i am class A"
 
    def info(self):
        return "computer science"
 
class B(A):
    pass
 
class C(B, A):
       def __str__(self):
        return "i am class C"
 
class D(C):
    pass
 
d = D()
print(d.info())
# print(str(d))
print(D.mro())


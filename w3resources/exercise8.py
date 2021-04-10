#8. Write a Python program to create two empty classes, Student and Marks. Now create some instances and check 
#whether they are instances of the said classes or not. Also, check whether the said classes are subclasses of the built-in object class or not

class Student:
    pass
class Marks:
    pass

S = Student()
M = Marks()
print(type(S))
print("The object {} is an instance of the class {}?".format("S",Student.__name__),isinstance(S,Student))
print(type(M))
print("The object {} is an instance of the class {}?".format("M",Student.__name__),isinstance(M,Student))
print("The object {} is an instance of the class {}?".format("M",Marks.__name__),isinstance(M,Marks))


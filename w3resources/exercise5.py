#5. Define a Python function student(). Using function attributes display the names of all arguments.
#Solving by defining a class
class Student:
    def __init__(self,student,ids,gpa):
        self.student = student
        self.ids = ids
        self.gpa = gpa
    
    def __str__(self):
        return "The student ID is {}\nThe student name is {}\nThe GPA is {}".format(self.ids,self.student,self.gpa)

M = Student("Mauricio",39,5.0)
print(M)
print("================================================")


#Solving by defining a function
def student(name,id,gpa):
    return "The student ID is {}\nThe student name is {}\nThe GPA is {}".format(id,name,gpa)
D = student("Diogo",28,3.5)
print(D)
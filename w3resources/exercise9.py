#9. Write a Python class named Student with two attributes student_name, marks. 
#Modify the attribute values of the said class and print the original and modified values of the said attributes.
class Student:
    def __init__(self,student_name="Mauricio",marks="A+"):
        self.student_name = student_name
        self.marks=marks
    def __str__(self):
        return "The student name is {} and the marks are {}".format(self.student_name,self.marks)

M = Student()
print(M)
setattr(Student,"student_name","Diogo")
setattr(Student,"marks","A-")
print("The student name is {} and the marks are {}".format(getattr(Student,"student_name"),getattr(Student,"marks")))

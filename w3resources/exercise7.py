#7. Write a simple Python class named Student and display its type. 
#Also, display the __dict__ attribute keys and the value of the __module__ attribute of the Student class.
class Student:
    def __init__(self,student_name,student_class,student_gpa):
        self.student_name = student_name
        self.student_class = student_class
        self.student_gpa = student_gpa

print("The Student class type is {}".format(type(Student)))
print(Student.__dict__)
print(Student.__module__)

#10. Write a Python class named Student with two attributes student_id, student_name. 
# Add a new attribute student_class and display the entire attribute and their values of the said class. 
# Now remove the student_name attribute and display the entire attribute with values

class Student:
    def __init__(self,student_id,student_name):
        self.student_id = student_id
        self.student_name = student_name

setattr(Student,"student_name","John Doe")
print("The student name is {}".format(getattr(Student,"student_name")))
delattr(Student,"student_name")


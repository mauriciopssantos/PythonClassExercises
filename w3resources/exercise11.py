#11. Write a Python class named Student with two attributes student_id, student_name. Add a new attribute student_class. 
# Create a function to display the entire attribute and their values in Student class

class Student:

    student_id = 29
    student_name = "Mauricio"
    
    def __init__(self):
        pass    
        

    def display(self):
        for att, value in Student.__dict__.items():
            if not att.startswith("_"):
                print(att,"==",value)

setattr(Student,"student_class","Arts")
M = Student()
M.display()

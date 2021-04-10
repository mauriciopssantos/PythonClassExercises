#12. Write a Python class named Student with two instances student1, student2 and assign given values to the said instances attributes. 
# Print all the attributes of student1, student2 instances with their values in the given format

class Student:
    student_id = 29
    student_name = "Mauricio"

student1 = Student()
student2 = Student()
student2.student_name = "Diogo"
print(student1.student_name)
print(student2.student_name)

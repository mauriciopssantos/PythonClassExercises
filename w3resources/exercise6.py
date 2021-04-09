#Write a Python function student_data() which will print the id of a student (student_id). 
#If the user passes an argument student_name or student_class the function will print the student name and class
#Solving the problem defining a function
def student_data(student_id,**data):
    print("The student ID is {}".format(student_id))
    if "student_name" in data:
        print("The student name is {}".format(data["student_name"]))
    if "student_name" in data and "student_class" in data:
        print("The student class is {}".format(data["student_class"]))
student_data(19,student_name="Mauricio")



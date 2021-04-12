#9. Write a Python class which has two methods get_String and print_String. 
# get_String accept a string from the user and print_String print the string in upper case.

class StringTransform:
    def get_String(self):
        self.strr = input("Entre a string: ")
        return self.strr

    def print_String(self):
        print(self.strr.upper())

a = StringTransform()
a.get_String()
a.print_String()
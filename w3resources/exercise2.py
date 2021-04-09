#Write a Python program to create a class and display the namespace of the said class
class NameGenerator:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __call__(self):
        print("My name is {}, and I'm {} years old".format(self.name,self.age))

M = NameGenerator("Mauricio","23")
M()

for attributes in NameGenerator.__dict__:
    print(attributes)
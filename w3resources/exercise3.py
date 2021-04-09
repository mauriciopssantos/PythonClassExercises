#Write a Python program to create an instance of a specified class and display the namespace of the said instance
class NumChange:
    def __init__(self,number):
        self.number = number
    
    def setToZero(self):
        self.number = 0
    
    def setToOne(self):
        self.number = 1
    
    def displayNum(self):
        print("Your number is",self.number)

n = NumChange(4)
n.displayNum()
n.setToZero()
n.displayNum()
n.setToOne()
n.displayNum()
print(n.__dict__)
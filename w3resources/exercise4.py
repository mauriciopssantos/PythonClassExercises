#4. 'builtins' module provides direct access to all 'built-in' identifiers of Python.
#Write a python program which import the abs() function using the builtins module, 
#display the documentation of abs() function and find the absolute value of -155
from builtins import abs
class calculateAbs:
    def __init__(self,num):
        self.num = num
    

    def __str__(self):
        return "The absolute value of {} is {}".format(self.num,abs(self.num))

print(help(abs))
n = calculateAbs(-155)
print(n)

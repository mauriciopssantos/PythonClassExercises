#12. Write a Python program to get the class name of an instance in Python:
class getInst:
    def __str__(self):
        return type(self).__name__

x = getInst
print(x)
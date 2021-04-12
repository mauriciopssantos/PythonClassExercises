#1. Write a Python class to convert an integer to a roman numeral
class RomanNumeral:
    def __init__(self,n=0):
        self.n=n
    
    def checker(self):
        if isinstance(self.n, int):
            return self.n
        else:
            raise Exception("This is not a number")
    
    def convert(self):
        pass

    
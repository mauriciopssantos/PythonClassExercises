
#Write a Python class to implement pow(x, n).
class expo:
    def __init__(self,n):
        self.n = n
    
    def expon(self,x):
        self.n = self.n**x
        print(self.n)
q = expo(5)
q.expon(3)


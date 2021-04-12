import numpy as np
#11. Write a Python class named Circle constructed by a radius and two methods which will compute the area and the perimeter of a circle#

class Circle:
   
    def __init__(self,r):
        self.r = r

    def areaCircle(self):
        self.area = np.pi * (self.r**2)
        return self.area

    def perimeterCircle(self):
        self.perimeter = 2*np.pi*self.r
        return self.perimeter
    

c = Circle(5)
c.areaCircle()
c.perimeterCircle()
print("The radius of your circle is {}\nThe area of your circle is {}\nThe perimeter of your circle is {}".format(c.r,c.area,c.perimeter))
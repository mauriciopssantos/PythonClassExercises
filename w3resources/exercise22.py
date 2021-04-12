#10. Write a Python class named Rectangle constructed by a length and width and a method which will compute the area of a rectangle.
class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width

    def computeArea(self):
        self.area = self.length*self.width
        print("The area of your rectangle is {}".format(self.area))

rec = Rectangle(5,10)
rec.computeArea()

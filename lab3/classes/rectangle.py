from shape import Shape

class Rectangle(Shape):
    def __init__(self,length,width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
    

rec = Rectangle(10,2)
print(rec.area())



        
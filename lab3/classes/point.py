class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def show(self):
        print(self.x,self.y)
    
    def move(self,x1,y1):
        self.prevX = self.x
        self.prevY = self.y
        self.x = x1
        self.y = y1
        
     
    def dist(self):
        return (abs(self.prevX - self.x),abs(self.prevY - self.y))
    
point = Point(1,2)

point.show()

point.move(4,5)

point.show()

print(point.dist())

        
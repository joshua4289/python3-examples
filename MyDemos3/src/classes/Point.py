class Point:
    """this is the docs for Point"""
    count = 0
    @staticmethod
    def getCount(): 
        return Point.count
    
    def __init__(self, x0, y0, name):
        Point.count += 1
        self.x = x0
        self.y = y0
        self.name = name
    def moveBy(self, dx = 1, dy = 1):
        self.x += dx
        self.y = self.y + dy
    def display(self):
        print "Point {0} is at [{1},{2}]".format(self.name, self.x, self.y)
print Point.getCount()
p1 = Point(100, 200, 'point-p1')
p2 = Point(200, 205, 'point-p2')
p3 = Point(300, 210, 'point-p3')
print Point.getCount()
p1.moveBy(1, 1)
p2.moveBy(1, 1)
p3.moveBy(1, 1)
p1.display()
p2.display()
p3.display()
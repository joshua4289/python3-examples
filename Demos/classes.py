class Point:
    '''doc string'''
    count = 0
    @staticmethod
    def getCount():
        return Point.count
    # CTOR
    def __init__(self, x0, y0, name):
        Point.count += 1
        self.x = x0
        self.y = y0
        self.name = name
    def __del__(self):
        Point.count -= 1
    def moveBy(self, dx, dy):
        self.x = self.x + dx
        self.y = self.y + dy
    def display(self):
        print "Point: {2} is at {0},{1}".format(self.x, self.y, self.name)
# create objects


print Point.getCount()
p1 = Point(100, 200, "Point-p1")
p2 = Point(110, 300, "Point-p2")
p3 = Point(150, 400, "Point-p3")
print Point.getCount()
p1.moveBy(1, 1)
p2.moveBy(1, 1)
p3.moveBy(1, 1)
p1.display()
p2.display()
p3.display()
1
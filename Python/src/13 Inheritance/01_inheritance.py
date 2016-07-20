############################################################
#
#    Inheritance
#
############################################################


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def whereAmI(self):
        print("Point({}) is at {},{}".format(id(self), self.x, self.y))

    def moveBy(self, dx, dy):
        self.x += dx
        self.y += dy

class ColoredPoint(Point):
    def __init__(self, x, y, color):
        Point.__init__(self, x, y)
        self.color = color
        
    def changeColor(self, newColor):
        self.color = newColor
    
    def display(self):
        self.whereAmI()
        print(" ... and color is %s" % self.color)
        

def WhereAreYou(p):
    p.whereAmI()

p = Point(5,8)
cp = ColoredPoint(15,25,"Blue")
print( cp.__dict__ )
p.whereAmI()
cp.whereAmI()
cp.display()

cp.changeColor("Cyan")
cp.moveBy(5,15)
cp.Display()

WhereAreYou(p)
WhereAreYou(cp)

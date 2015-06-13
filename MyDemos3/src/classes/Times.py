class Time:
    def __init__(self, hrs = 0, min = 0):
        self.hrs = hrs
        self.min = min
    def display(self):
        print "{0} hrs, {1} min".format(self.hrs, self.min)
    def addOneHour(self): 
        self.hrs += 1
    def addOneMinute(self): 
        self.min += 1
        if self.min == 60:
            self.min = 0
            self.addOneHour()
    def __add__(self, rhs):
        result = Time()
        if isinstance(rhs, Time):
            result.min = self.min + rhs.min
            result.hrs = self.hrs + rhs.hrs
        else:
            result.min = self.min + rhs

        if result.min >= 60:
            result.min -= 60
            result.hrs += 1
            
        return result
#     if isinstance(a, dict):
#     do_something()
t1 = Time(6, 40)
t2 = Time(3, 25)
t1.addOneHour()
t2.addOneMinute()
t1.display()
t2.display()
t = t1 + t2
t.display()

t += t2
t.__iadd__(t2)




a = [ [10,20],[30,40] ] # mutable
b = a[:]
print id(a)
a.append(99)
print id(a)
print id(b)
print id(a[0])
print id(b[0])
print id(a[0][1])
print id(20)



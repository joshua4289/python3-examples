import copy

x = [ [10, 20], [30, 40] ]
y = tuple(x)        # cast => shallow copy
z = copy.copy(x)

print x
print y
print z
print id(x), id(y), id(z)
print id(x[0]), id(y[0]), id(z[0])
print id(x[1]), id(y[1]), id(z[1])
 


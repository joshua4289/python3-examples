
x = range(10, 30)
y = x[:]    # shallow copy
z = list(x) # shallow copy
import copy
w1 = copy.copy(x) # shallow copy
w2 = copy.deepcopy(x)   # deep copy
print id(x)
print id(z)
print id(w1)
print id(w2)

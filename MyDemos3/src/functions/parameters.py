def f(a, b = 10, c = 100):
    print a + b + c
    
    
f(2, 4, 6)
f(2, 4)
f(2)
f(2, c = 77)
f(c = 44, b = 33, a = 22)
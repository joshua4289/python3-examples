############################################################
#
#    decorators
#
############################################################



class MyClass(object):
    def __init__(self, color):
        self.color = color

    def foo(self, fn):
        def enhance(x, fn=fn):
            print "foo: ", self.color, x
            return fn(x)
        return enhance

    def bar(self, fn):
        def enhance(x, fn=fn):
            print "bar: ", self.color, x
            return fn(x)
        return enhance
        
x = MyClass("red")
y = MyClass("blue")


@x.bar
def square(n):
    return n * n
 
@y.bar
def cube(n):
    return n * n * n
 
@y.foo
def quad(n):
    return n * n * n * n

@x.bar
@y.foo
def ff(fn): return fn


# curried and decorator versions
print x.bar(square)(4)
print square(5)

# curried and decorator versions
print x.bar(y.foo(ff))(4)
print ff(4)

print cube(6)
print quad(7)

1
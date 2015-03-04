# This example defines a class factory that defines an attribute y
# and a constructor and allocator.
# The class factory can be used to create other classes; the factory
# can add attributes to the dictionary of the newly created class

# Note: all class factories inherit from the base class factory: type

# utility to show relevant parts of dictionaries
def displayUserDefinedPartsOfDictionary(dct):
    for key, value in dct.iteritems():
        if not key.startswith("__"):
            print "\t", key, value
    print




class MyClassFactory(type):
    y = 100
    def __init__(cls, name, bases, dct):
        print "Creating class %s using CustomMetaclass" % name
        print "with dictionary: "
        displayUserDefinedPartsOfDictionary(dct)
        bases = (object,)
        super(MyClassFactory, cls).__init__(name, bases, dct)
        
    def __new__(cls, name, bases, dct):
        print "Allocating memory for class", name
        dct['y'] = MyClassFactory.y              # attribute created
        dct['f'] = lambda self: self.x + self.y; # method created
        # use the class factory type to allocate
        return type.__new__(cls, name, bases, dct)

# New classes use the class factory 'type', unless the __metaclass__
# attribute is defined to select a different class factory
 
class BaseClass(object):
    __metaclass__ = MyClassFactory
    x = 44
    # this class will get 'x', 'y' and 'f' defined by the class factory
    
# this uses the class factory of its superclass
class SubClass(BaseClass):
    def h(self):
        print self.x
        
base1 = BaseClass()
base2 = BaseClass()
print "Base class: ", BaseClass.__bases__
base1.a = 100
base1.b = 200
base2.c = 300
print "\nBase dictionaries:"
print "=================="
displayUserDefinedPartsOfDictionary(BaseClass.__dict__)
displayUserDefinedPartsOfDictionary(base1.__dict__)
displayUserDefinedPartsOfDictionary(base2.__dict__)

sub = SubClass()
print "\nDerived dictionaries:"
print "====================="
displayUserDefinedPartsOfDictionary(SubClass.__dict__)
displayUserDefinedPartsOfDictionary(sub.__dict__)

# call methods on sub
sub.h()
print sub.f()

1

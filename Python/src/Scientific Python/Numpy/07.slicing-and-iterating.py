############################################################
#
#    slicing and iterating
#
############################################################

from numpy import *
# from scisoftpy import *


# one dimensional arrays
a = arange(20); print a
print a[7:14]
print a[2:14:3]
print a[::]
print

# multi-dimensional arrays
a = arange(24).reshape(4,3,2); print a
print a[0:2,0:2,0:2]

# iterate (works on first dimension)
print "iteration"
for eachRow in a:
    print eachRow
    
# flatten array (not a function) to iterate over every element
for element in a.flat:
    print element,

# Fortran arrays     -> first dimension varies fastest
# C arrays (default) -> last dimension varies fastest 
a = arange(24).reshape( (4,3,2), order="F" ) # create Fortran array
print a


1

from functools import reduce
############################################################
#
#    reduce
#
############################################################

numbers = list(range(1, 11))
sum = reduce(lambda x, y: x + y, numbers)
print(sum)



1

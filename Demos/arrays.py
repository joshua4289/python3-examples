mytuple = ( 5, 7, 11, 13, 17 )
mylist = mytuple
mylist2 = list(mylist)

mylist[3] = 99

print mytuple, id(mytuple)
print mylist, id(mylist)
print mylist2, id(mylist2)



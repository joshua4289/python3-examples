x,y,z = 1,2,3



salary = {
          'john' : 23000,
          'susan': 47000,
          'jim'  : 33000,
          'zoe'  : 44000,
          'pedro': 41500
          }


# extract keys into a list
mylist = salary.keys()

# sort the list using mylist.sort()
mylist.sort()

# loop from the sorted list, picking up each key value pair
for key in mylist:
    print key, salary[key]
salary = { 'Jim' : 50000,
           'Bob' : 44000,
           'Sue' : 27000,
           'Zoe' : 66000,
           'Ali' : 44000
          }

# use salary.keys() to get list of keys
theKeys = salary.keys()

# use sort() to sort the list
theKeys.sort()

# loop through sorted list printing key, value pairs
for key in theKeys:
    print key, salary[key]



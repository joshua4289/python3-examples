salary = {
           'John' : 52000,
           'Sue'  : 48000,
           'Dave' : 38000,
           'Zoe'  : 60000,
           'Ali'  : 55000
         }

salary['Sean'] = 47000  # create new key, value pair
salary['Sean'] = 48000  # update
salary['Dave'] = None
# del salary['Zoe']
salary.pop('Zoe')


sortedKeys = salary.keys()
sortedKeys.sort()
print len(sortedKeys)

for key in sortedKeys:
    print key, salary[key]


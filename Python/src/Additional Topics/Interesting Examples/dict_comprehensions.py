department = 'Silly Walk'
z = {x: x**2 for x in (2, 4, 6)}
print z

department = 'Silly Walk'
print {x: department.count(x) for x in department}
# {'a': 1, ' ': 1, 'i': 1, 'k': 1, 'l': 3, 'S': 1, 'W': 1, 'y': 1}

print {x for x in department}

import unicodedata

# create a string from unicode code points
u = chr(233) + chr(0x0bf2) + chr(3972) + chr(6000) + chr(13231) + chr(0xf29)
print(u)


for i, c in enumerate(u):
#     print(i, '%04x' % ord(c), unicodedata.category(c), end=" ")
#     print(unicodedata.name(c))
    print("{}: {:04x} {:4s} {}".format(i, 
                                 ord(c), 
                                 unicodedata.category(c),
                                 unicodedata.name(c)))
# some unicode characters represent numbers (in this case, characters 1 and 5)
# Get numeric value of second character
print("{}".format(unicodedata.numeric(u[1])))
print("{}".format(unicodedata.numeric(u[5])))

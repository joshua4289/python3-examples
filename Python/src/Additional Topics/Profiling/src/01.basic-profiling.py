import sys, myprogram, cProfile
sys.path.append("src")


def f():
    count = 0
    for i in xrange(200):
        count = count + i

# profile using cProfile
cProfile.run('myprogram.foo()')


import sys, os, pstats, profilestats

sys.path.append("src")
import myprogram


if not os.path.exists('stats'): os.mkdir('stats')
os.chdir('stats')

# this decorator profiles individual functions and creates two files in stats directory: 
#    cachegrind.out.profilestats (in KCachegrind-compatible fotrmat)
#    profilestats.prof (in cProfile format)
@profilestats.profile
def profileIt():
    myprogram.foo()

def reportUsingStats():
    stats = pstats.Stats('profilestats.prof')
    stats.strip_dirs()
    stats.sort_stats('cumulative')
    stats.print_stats()


def reportUsingKCachegrind():
    # need to install KCacheGrind program (not a Python module and only runs on Unix)
    pass

profileIt()
reportUsingStats()
reportUsingKCachegrind()


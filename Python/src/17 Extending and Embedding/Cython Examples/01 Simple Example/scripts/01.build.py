import subprocess, os, sys
sys.path.append('../..')
import set_paths

os.chdir("../src")
subprocess.call("python setup.py build_ext --inplace".split())

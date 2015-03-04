import subprocess,os,sys, requests
from distutils.sysconfig import get_python_lib

def setPath():
    # Changing the PATH to locate setuptools
    if sys.platform == 'darwin': offset = "/../../../bin:"
    if sys.platform == 'win32':  offset = "/../../Scripts;"
    if sys.platform == 'linux2': offset = "/../../../bin:"

    setuptoolsPath = get_python_lib() + offset
    os.environ["PATH"] = setuptoolsPath + os.environ["PATH"]



setPath()
cmd = "pip uninstall mymodule"


# this has to be in a pipe
# because pip will ask a series of questions
proc = subprocess.Popen(cmd.split(),
                        stdin=subprocess.PIPE,
                        stdout=subprocess.PIPE,
                        )
# answer Yes to all pip questions
stdout_text = proc.communicate('y')[0]
print stdout_text

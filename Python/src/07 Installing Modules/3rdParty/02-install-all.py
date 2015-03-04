# Use this script to setup packages
#
# Choose the installer below with a command such as:
#
#    installer = "pip install"          # to install
#    installer = "pip uninstall"        # to uninstall
#    installer = "pip install --upgrade # to upgrade

# N.B. if you are installing behind a proxy you will have to set 
#    HTTP_PROXY=http://user:password@yourproxy.com:port
#
# Alternatively use a local repository:
#    install -f http://localhost/repo foo

import subprocess,os,sys
from distutils.sysconfig import get_python_lib

def setPath():
    # Changing the PATH to locate setuptools
    if sys.platform == 'darwin': offset = "/../../../bin:"
    if sys.platform == 'win32':  offset = "/../../Scripts;"
    if sys.platform == 'linux2': offset = "/../../../bin:"

    setuptoolsPath = get_python_lib() + offset
    os.environ["PATH"] = setuptoolsPath + os.environ["PATH"]

def setProxy(url):
    """example call:
          setProxy("http://wwwcache.rl.ac.uk:8080")
    """
    os.environ["HTTP_PROXY"] = url
    
def install(cmd):
    cmd = (installer + " " + cmd)
    print "****", cmd
    subprocess.call(cmd.split())
    
setPath()
installer = "pip install"
install("beautifulSoup")
install("bottle")
install("chameleon")
install("cherrypy")
install("cx_oracle")
install("django")
install("html5lib")
install("flask")
install("mako")
install("markupsafe") 
install("mechanize")
install("mock")
install("multiprocessing")
install("nose")
install("numpy")
install("paramiko")
install("pip")
install("pil")
install("pisa")
install("profilestats")
install("pypdf2")
install("pypng")
install("pyprof2html")
install("pyramid")
install("pyramid_chameleon")
install("pyramid_mako")
install("pysnmp")
install("pytest")
install("pyx")
install("reportlab")
install("requests")
install("scipy")
install("scrapy")
install("scons")
install("selenium")
install("speech")
install("sqlalchemy")
install("virtualenv")
install("webob")
install("web.py")
install("xlrd")     # excel
install("xlwt")     # excel
install("yolk")

# use pip and yolk to see what is installed
subprocess.call("pip freeze".split())
subprocess.call("yolk -l".split())

1




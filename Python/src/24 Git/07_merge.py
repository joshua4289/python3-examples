import os

os.chdir('myrepo')

os.system('ls')
os.system('git merge mybranch')
os.system('ls')
os.system('git push -u origin master')
import os

os.chdir('myrepo')
raw_input("When you have created the remote repo ('myrepo'), hit return")
repo = "myrepo"
username = "seddon-software"
password = raw_input("Enter password: ")
cmd = "git remote add origin https://{0}:{1}@github.com/{0}/{2}.git".format(username, password, repo)
os.system(cmd)
os.system('git remote -v')
os.system('git push -u origin master')


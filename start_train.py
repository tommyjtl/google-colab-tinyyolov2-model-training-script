import glob, random, os, time, subprocess

os.chdir("./conf/")
output = subprocess.check_output("bash start-train.sh", shell=True)
print(output)
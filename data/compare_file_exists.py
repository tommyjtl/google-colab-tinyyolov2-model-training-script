import glob, os
import os.path
from os import path

direcotry_name = input("Please enter the name of the directory you want to compare: \n") 

current_path = os.getcwd()
directory_path = direcotry_name
extension_name = "txt"
print(current_path)
os.chdir(directory_path)

count = 0

for file in glob.glob("*." + str(extension_name)):
	count = count + 1
	f_extns = file.split(".")
	check_if = path.exists(f_extns[0]+".jpg")
	if ( check_if == False ):
		print(f_extns[0] + ",\t\t" + str(check_if))
		os.remove(file)

print("\nThis folder has " + str(count) + " images in total")
os.chdir(current_path)
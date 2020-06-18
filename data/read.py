import glob, os
import os.path
from os import path

current_path = os.getcwd()
directory_path = "tree"
extension_name = "jpg"
print(current_path)
os.chdir(directory_path)

count = 0

for file in glob.glob("*." + str(extension_name)):
	count = count + 1
	f_extns = file.split(".")
	check_if = path.exists(f_extns[0]+".txt")
	if ( check_if == False ):
		print(f_extns[0] + ",\t\t" + str(check_if))
		os.remove(file)

print("\n" + str(count))

'''
for file in glob.glob("*." + str(extension_name)):
	fin = open(file, 'r') 
	fin_lines = fin.readlines() 
	fin_lines_count = len(fin_lines)
	print(str(fin_lines_count)+" lines in total.")
	fin_list = []
	count = 0

	for line in fin_lines: 
		read_string = str(line)
		fin_list.append(read_string)

	for c in range(0,fin_lines_count,1):
		read_string = str(fin_list[c])
		fin_list[c] = read_string.replace("0", "2", 1)

	print(fin_list)
	fout = open(file, 'w')
	fout.writelines((fin_list))
	fout.close()
	fin.close()
'''
os.chdir(current_path)
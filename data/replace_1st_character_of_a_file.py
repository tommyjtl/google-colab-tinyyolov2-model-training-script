import glob, os

direcotry_name = input("Please enter the name of the directory you want to replace: \n") 

current_path = os.getcwd()
print(current_path)
directory_path = "turnright"
extension_name = "txt"
index_placed_before = "0"
index_placed_after = "2"

os.chdir(directory_path)

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
		fin_list[c] = read_string.replace(index_placed_before, index_placed_after, 1)

	print(fin_list)
	fout = open(file, 'w')
	fout.writelines((fin_list))
	fout.close()
	fin.close()

os.chdir(current_path)
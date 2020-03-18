import glob, random, os, time

def getListOfFiles(dirName):
	# create a list of file and sub directories 
	# names in the given directory 
	listOfFile = os.listdir(dirName)
	allFiles = list()
	# Iterate over all the entries
	for entry in listOfFile:
	    # Create full path
	    fullPath = os.path.join(dirName, entry)
	    # If entry is a directory then get the list of files in this directory 
	    if os.path.isdir(fullPath):
	        allFiles = allFiles + getListOfFiles(fullPath)
	    else:
	        allFiles.append(fullPath)
	            
	return allFiles

def main():

	dirName = os.getcwd()
	# Get the list of all files in directory tree at given path
	listOfFiles = getListOfFiles(dirName)

	f = open("train.txt", "w")

	# Print the files
	#for elem in listOfFiles:
	#    print(elem)

	# Get the list of all files in directory tree at given path
	listOfFiles = list()
	for (dirpath, dirnames, filenames) in os.walk(dirName):
	    listOfFiles += [os.path.join(dirpath, file) for file in filenames]
        
	for elem in listOfFiles:
		if (elem[-3] == "j"):
			# print(elem)
			with open("train.txt", "a") as myfile:
				myfile.write(elem+"\n")

def convert_test():
	num_lines = sum(1 for line in open('train.txt'))
	# print(num_lines)

	f=open('train.txt')
	lines=f.readlines()

	cont_line = random.sample(range(num_lines), int(num_lines/2))
	# print(cont_line)

	for i in range(0,int(num_lines/2),1):
		content = lines[cont_line[i]]
		# print(content)
		content = content.strip('\n')
		with open("test.txt", "a") as myfile:
			myfile.write(content)
		
	f.close()
        
if __name__ == '__main__':
    main()
    time.sleep(1)
    convert_test()
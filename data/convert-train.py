import glob, os

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
	for elem in listOfFiles:
	    print(elem)

	# Get the list of all files in directory tree at given path
	listOfFiles = list()
	for (dirpath, dirnames, filenames) in os.walk(dirName):
	    listOfFiles += [os.path.join(dirpath, file) for file in filenames]
        
	for elem in listOfFiles:
		if (elem[-3] == "j"):
			print(elem)
			with open("train.txt", "a") as myfile:
				myfile.write(elem+"\n")
        
if __name__ == '__main__':
    main()

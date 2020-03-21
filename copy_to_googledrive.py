from shutil import copyfile

project_name = input("Please enter the name of your project inside Google Drive: \n")
# google_drive_path = "/home/ubuntu/projects/"
google_drive_path = "/content/gdrive/My Drive/"
# google_drive_path = "/Users/tommyjtl/Documents/CocoRobo/"

try:
	copyfile("./convert/"+ project_name +".kmodel", google_drive_path + project_name +".kmodel")
except IOError as e:
	print("Something went wrong:\n")
	print(str(e))
finally:
	print("Done copying the model file to your Google Drive! No go check it!")
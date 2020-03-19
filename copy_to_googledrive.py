from shutil import copyfile

project_name = input("Please enter the name of your project in side Google Drive: \n")
# google_drive_path = "/home/ubuntu/projects/"
google_drive_path = "/content/gdrive/My\\ Drive/"
# google_drive_path = "/Users/tommyjtl/Documents/CocoRobo/"

copyfile("./convert/"+ project_name +".kmodel", google_drive_path + project_name +".kmodel")

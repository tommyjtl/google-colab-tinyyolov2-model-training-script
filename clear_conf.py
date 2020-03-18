import glob, random, os, time, shutil

names_file_name = ""
file_exist_state = False

def delete_conf():
	try:
		os.chdir("./conf/")
		os.system("rm start-train.sh")
		os.system("rm ./*.cfg")
		os.system("rm ./*.data")
		os.system("rm ./*.names")
	except IOError as e:
		print(str(e))
	finally:
		os.chdir("../")

def delete_data():
	try:
		os.chdir("./data/")
		os.remove("test.txt")
		os.remove("train.txt")
		names_file_name = ""
		for names_file in glob.glob("*.names"):
			names_file_name = names_file
			print(names_file_name)
			os.remove(names_file_name)
		data_file_list = os.listdir("./")
		data_file_list.remove("generate_train-test.py")
		try:
			data_file_list.remove(".DS_Store")
		except BaseException as e:
			if str(e) == "list.remove(x): x not in list":
				print("Not macOS system, pass")
			pass
		for i in range(len(data_file_list)): 
			print("Deleting " + data_file_list[i] + "...")
			shutil.rmtree(data_file_list[i])
	except IOError as e:
		print(str(e))
	finally:
		os.chdir("../")

try:
	os.chdir("./conf/")
	for names_file in glob.glob("*.data"):
		names_file_name = names_file
		# print(names_file_name)
	if names_file_name == "":
		print("conf files don't exist") 
		file_exist_state = False
	elif names_file_name != "":
		print("conf files is not empty") 
		file_exist_state = True
except IOError as e:
	print(str(e))
finally:
	os.chdir("../")

if file_exist_state == False:
	print("conf doesn't exist")
elif file_exist_state == True:
	check_if_continue = input("conf exists, are you sure to delete them? (y/n): ")
	if check_if_continue == "y":
		print("deleting all...\n")
		delete_conf()
		delete_data()
	elif check_if_continue == "n":
		print("does nothing, exiting now.")
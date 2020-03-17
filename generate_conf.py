import glob, random, os, time

conf_directory_name = "conf"
google_drive_path = "/home/ubuntu/projects/"

google_drive_project_path = input("Please enter the dataset directory path you put on Google Drive: \n") 
classes_count = input("Please enter the number of classes you would like to train: \n")
project_name = input("Please enter the name of your project: \n")
current_directory_path = os.getcwd()

def generate_cfg():
	print("1. Total classes is " + classes_count + ", " + project_name + ".cfg generated to conf directory")
	f = open(conf_directory_name+ "/" + project_name + ".cfg", "w")
	cfg_content = ["[net]\n", "Training\n", "batch=64\n", "subdivisions=16\n", "width=224\n", "height=224\n", "channels=3\n", "momentum=0.9\n", "decay=0.0005\n", "angle=0\n", "saturation = 1.5\n", "exposure = 1.5\n", "hue=.1\n\n", "learning_rate=0.001\n", "burn_in=1000\n", "max_batches=" + str(int(float(classes_count))*2000) +"\n", "policy=steps\n", "steps=" + str(int(float(classes_count))*0.8) + "," + str(int(float(classes_count))*0.9) + "\n", "scales=.1,.1\n\n", "[convolutional]\n", "batch_normalize=1\n", "filters=16\n", "size=3\n", "stride=1\n", "pad=1\n", "activation=leaky\n\n", "[maxpool]\n", "size=2\n", "stride=2\n\n", "[convolutional]\n", "batch_normalize=1\n", "filters=32\n", "size=3\n", "stride=1\n", "pad=1\n", "activation=leaky\n\n", "[maxpool]\n", "size=2\n", "stride=2\n\n", "[convolutional]\n", "batch_normalize=1\n", "filters=64\n", "size=3\n", "stride=1\n", "pad=1\n", "activation=leaky\n\n", "[maxpool]\n", "size=2\n", "stride=2\n\n", "[convolutional]\n", "batch_normalize=1\n", "filters=128\n", "size=3\n", "stride=1\n", "pad=1\n", "activation=leaky\n\n", "[maxpool]\n", "size=2\n", "stride=2\n\n", "[convolutional]\n", "batch_normalize=1\n", "filters=256\n", "size=3\n", "stride=1\n", "pad=1\n", "activation=leaky\n\n", "[maxpool]\n", "size=2\n", "stride=2\n\n", "[convolutional]\n", "batch_normalize=1\n", "filters=512\n", "size=3\n", "stride=1\n", "pad=1\n", "activation=leaky\n\n", "[convolutional]\n", "size=1\n", "stride=1\n", "pad=1\n", "filters=" + str((int(float(classes_count)) + 5) * 5) + "\n", "activation=linear\n\n", "[region]\n", "anchors = 0.57273, 0.677385, 1.87446, 2.06253, 3.33843, 5.47434, 7.88282, 3.52778, 9.77052, 9.16828\n", "bias_match=1\n", "classes=" + str(int(float(classes_count))) + "\n", "coords=4\n", "num=5\n", "softmax=1\n", "jitter=.2\n", "rescore=0\n\n", "object_scale=5\n", "noobject_scale=1\n", "class_scale=1\n", "coord_scale=1\n\n", "absolute=1\n", "thresh = .6\n", "random=1"]
	f.writelines(cfg_content)
	f.close()

def generate_data():
	print("2. " + project_name + ".data generated to conf directory\n")
	f = open(conf_directory_name+ "/" + project_name + ".data", "w")
	data_content = [
		"classes="+ str(int(float(classes_count))) +"\n",
		"train  = "+current_directory_path+"/data/train.txt\n",
		"valid  = "+current_directory_path+"/data/test.txt\n",
		"names = trash.names\n",
		"backup = "+current_directory_path+"/backup\n"
	]
	f.writelines(data_content)
	f.close()

def generate_names():
	os.chdir(google_drive_path + google_drive_project_path)
	names_file_name = ""
	for names_file in glob.glob("*.names"):
		names_file_name = names_file
		print(names_file_name)
	f = open(names_file_name,"r+")
	read_original_names = f.readlines()
	print(read_original_names)
	f.close()
	os.chdir(current_directory_path)
	f2 = open(conf_directory_name+ "/" + project_name + ".names", "w")
	f2.writelines(read_original_names)
	f.close()

def generate_training_bash():
	f = open(conf_directory_name+ "/" +  "start-train.sh", "w")
	bash_content = ["../tools/darkflow-colab/darknet detector train "+ project_name +".data "+project_name+".cfg darknet19_448.conv.23\n"]
	f.writelines(bash_content)
	f.close()


if __name__ == '__main__':
	# shenzhen_trash_classification_sign_dataset
	
	os.system("cp -a "+ google_drive_path +google_drive_project_path + "/. data/")
	generate_cfg()
	generate_data()
	generate_names()
	generate_training_bash()
	os.chdir("./data/")
	exec(open("generate_train-test.py").read())
	os.chdir(current_directory_path)
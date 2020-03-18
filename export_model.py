import glob, random, os, time, shutil

project_name = input("Please enter the name of your project: \n")

current_directory_path = os.getcwd()

def clear_darflow_label():
	try:
		os.remove("./tools/darkflow-colab/labels.txt")
	except IOError as e:
		print(str(e))
	finally:
		print("Deleteing labels.txt from previous darkflow conversion.")

def copy_raw_to_darkflow():
	try:
		os.mkdir("./convert/to-be-exported")
	except IOError as e:
		print(str(e))

	try:
		os.system("cp ./conf/" + project_name + ".names ./tools/darkflow-colab/labels.txt")
		os.system("cp ./conf/" + project_name + ".cfg ./convert/to-be-exported/")
		os.system("cp ./backup/" + project_name + "_last.weights ./convert/to-be-exported/")
		os.system("cp ./convert/to-be-exported/" + project_name + ".cfg ./tools/darkflow-colab/cfg/" + project_name + ".cfg")
		os.system("cp ./convert/to-be-exported/" + project_name + "_last.weights ./tools/darkflow-colab/bin/" + project_name + ".weights")
	except IOError as e:
		print(str(e))
	finally:
		print("Done copying files to darkflow directory.")

def run_darkflow_convertion():
	os.chdir("./tools/darkflow-colab/")

	try:
		os.system("./flow --model cfg/" + project_name + ".cfg --load bin/" + project_name + ".weights --savepb")
	except IOError as e:
		print(str(e))
	finally:
		print("Done converted model to tensorflow type.")

	os.chdir(current_directory_path)

def generate_test_images_for_conversion():
	try:
		os.mkdir("./tools/tflite2kmodel-colab/images/" + project_name)
		print("Exporting testing images from training dataset.")
		time.sleep(0.5)
		os.chdir("./data/")
		num_lines = sum(1 for line in open('train.txt'))
		f=open('train.txt')
		lines=f.readlines()
		cont_line = random.sample(range(num_lines), int(num_lines/4))
		for i in range(0,int(num_lines/4),1):
			content = lines[cont_line[i]]
			content = content.strip('\n')
			os.system("cp " + content + " ../tools/tflite2kmodel-colab/images/" + project_name + "")
			# print(content)
		f.close()
		os.chdir(current_directory_path)
	except IOError as e:
		print(str(e))

def prepare_ncc_package():
	os.chdir("./tools/tflite2kmodel-colab/")
	os.system("wget https://cocoroboai.s3-ap-southeast-1.amazonaws.com/ncc.zip")
	os.system("unzip ncc.zip")


if __name__ == '__main__':
	generate_test_images_for_conversion()
	clear_darflow_label()
	copy_raw_to_darkflow()
	run_darkflow_convertion()
	prepare_ncc_package()
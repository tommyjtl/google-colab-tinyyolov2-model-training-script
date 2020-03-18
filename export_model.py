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

if __name__ == '__main__':
	clear_darflow_label()
	copy_raw_to_darkflow()
	run_darkflow_convertion()
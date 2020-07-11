'''
import os

os.system("git submodule update --init")
os.system("cd ./tools/darknet-colab/ && make && cd ../../")
os.system("cd ./tools/darkflow-colab/ && python3 setup.py build_ext --inplace && cd ../../")
'''

import subprocess, shlex, os, signal

try:
	print("(Step 1 of 3) Getting all the tools we need... (Darknet, Darkflow, Conversion tool)")

	command = "git submodule update --init"
	print(shlex.split(command))
	process = subprocess.Popen(shlex.split(command), stdout=subprocess.PIPE)
	print("Process PID is: " + str(process.pid))
	while True:
		output = process.stdout.readline()
		if output == '' and process.poll() is not None:
			break
		if output:
			# print("")
			formatted_output = output.strip().decode("utf-8")
			print(formatted_output)

			if "Submodule path 'tools/tflite2kmodel-colab': checked out" in formatted_output:
				break
			elif formatted_output == '':
				break
		else: break
	# process.terminate()
	process.terminate()
	try:
		process.wait(timeout=0.2)
		print('== subprocess exited with rc =', process.returncode)
	except subprocess.TimeoutExpired:
		print('subprocess did not terminate in time')




	print("(Step 2 of 3) Building darknet...")

	command = "make"
	os.chdir("./tools/darknet-colab/")
	print(shlex.split(command))
	process = subprocess.Popen(shlex.split(command), stdout=subprocess.PIPE)
	print("Process PID is: " + str(process.pid))
	while True:
		output = process.stdout.readline()
		if output == '' and process.poll() is not None:
			break
		if output:
			# print("")
			formatted_output = output.strip().decode("utf-8")
			print(formatted_output)

			if "Submodule path 'tools/tflite2kmodel-colab': checked out" in formatted_output:
				break
			elif formatted_output == '':
				break
		else: break
	# process.terminate()
	process.terminate()
	try:
		process.wait(timeout=0.2)
		print('== subprocess exited with rc =', process.returncode)
	except subprocess.TimeoutExpired:
		print('subprocess did not terminate in time')
	os.chdir("../../")




	print("(Step 3 of 3) Building darkflow...")

	command = "python3 setup.py build_ext --inplace"
	os.chdir("./tools/darkflow-colab/")
	print(shlex.split(command))
	process = subprocess.Popen(shlex.split(command), stdout=subprocess.PIPE)
	print("Process PID is: " + str(process.pid))
	while True:
		output = process.stdout.readline()
		if output == '' and process.poll() is not None:
			break
		if output:
			# print("")
			formatted_output = output.strip().decode("utf-8")
			print(formatted_output)

			if "Submodule path 'tools/tflite2kmodel-colab': checked out" in formatted_output:
				break
			elif formatted_output == '':
				break
		else: break
	# process.terminate()
	process.terminate()
	try:
		process.wait(timeout=0.2)
		print('== subprocess exited with rc =', process.returncode)
	except subprocess.TimeoutExpired:
		print('subprocess did not terminate in time')
	os.chdir("../../")


except KeyboardInterrupt:
	print("Keyboard Interrupted.")

print("""
  ____                   _ 
 |  _ \  ___  _ __   ___| |
 | | | |/ _ \| '_ \ / _ \ |
 | |_| | (_) | | | |  __/_|
 |____/ \___/|_| |_|\___(_)
                           
	""")
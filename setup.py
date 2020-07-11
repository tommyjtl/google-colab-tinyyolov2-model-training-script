'''
import os

os.system("git submodule update --init")
os.system("cd ./tools/darknet-colab/ && make && cd ../../")
os.system("cd ./tools/darkflow-colab/ && python3 setup.py build_ext --inplace && cd ../../")
'''

import subprocess, shlex, os, signal

def run_command(command, type):
	if type == 1:
		print(shlex.split(command))
		process = subprocess.Popen(shlex.split(command), stdout=subprocess.PIPE)
	elif type == 2:
		process = subprocess.Popen(command, stdout=subprocess.PIPE)
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
			'''
			if ("avg loss" in formatted_output) and ("rate" in formatted_output):
				print(formatted_output)
				iteration_times = int(formatted_output.split()[0][:-1])
				avg_loss = float(formatted_output.split()[2])
				# print(str(int(iteration_times)) + "," + str(float(formatted_output.split()[2])))
				if avg_loss < 0.06: break
			'''
	# process.terminate()
	process.terminate()
	try:
		process.wait(timeout=0.2)
		print('== subprocess exited with rc =', process.returncode)
	except subprocess.TimeoutExpired:
		print('subprocess did not terminate in time')

try:
	# print("(Step 1 of 3) Getting all the tools we need... (Darknet, Darkflow, Conversion tool)")
	# run_command("git submodule update --init", 1)
	print("(Step 2 of 3) Building darknet...")
	run_command(["cd ./tools/darknet-colab/ && make && cd ../../"], 2)
	print("(Step 3 of 3) Building darkflow...")
	run_command(["cd ./tools/darkflow-colab/ && python3 setup.py build_ext --inplace && cd ../../"], 2)
except KeyboardInterrupt:
	print("Keyboard Interrupted.")

print("""
  ____                   _ 
 |  _ \  ___  _ __   ___| |
 | | | |/ _ \| '_ \ / _ \ |
 | |_| | (_) | | | |  __/_|
 |____/ \___/|_| |_|\___(_)
                           
	""")
import subprocess, shlex, os, signal

def run_command(command):
	process = subprocess.Popen(shlex.split(command), stdout=subprocess.PIPE)
	print("Process PID is: " + str(process.pid))
	while True:
		output = process.stdout.readline()
		if output == '' and process.poll() is not None:
			break
		if output:
			formatted_output = output.strip().decode("utf-8")
			if ("avg loss" in formatted_output) and ("rate" in formatted_output):
				print(formatted_output)
				iteration_times = int(formatted_output.split()[0][:-1])
				avg_loss = float(formatted_output.split()[2])
				# print(str(int(iteration_times)) + "," + str(float(formatted_output.split()[2])))
				if avg_loss < 0.06: break
	# process.terminate()
	process.terminate()
	try:
		process.wait(timeout=0.2)
		print('== subprocess exited with rc =', process.returncode)
	except subprocess.TimeoutExpired:
		print('subprocess did not terminate in time')
	os.kill(int(process.pid)+1, signal.SIGKILL)

try:
	run_command("bash start-train.sh")
except KeyboardInterrupt:
	print("Keyboard Interrupted.")

print("""
  ____                   _ 
 |  _ \  ___  _ __   ___| |
 | | | |/ _ \| '_ \ / _ \ |
 | |_| | (_) | | | |  __/_|
 |____/ \___/|_| |_|\___(_)
	""")

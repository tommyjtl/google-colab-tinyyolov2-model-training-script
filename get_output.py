import subprocess

batcmd="bash check-aws.sh"
result = subprocess.check_output(batcmd, shell=True)
print(result.decode('unicode_escape').strip("\n"))

if result.decode('unicode_escape').strip("\n") == "yes":
	print("this is an aws server, activating tensorflow env...")
	os.system("source activate tensorflow_p36")
elif result.decode('unicode_escape').strip("\n") == "no":
	print("this is not an aws server, just go with the flow...")
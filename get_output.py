import subprocess

batcmd="watch -n 0.5 ls"
result = subprocess.check_output(batcmd, shell=True)
print(result)


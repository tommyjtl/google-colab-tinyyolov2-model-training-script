import subprocess

batcmd="bash check-aws.sh"
result = subprocess.check_output(batcmd, shell=True)
print(result.decode('unicode_escape'))
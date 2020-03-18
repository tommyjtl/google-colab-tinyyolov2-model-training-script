import os

while True:
	string = os.popen('watch -n 1 ls -l').read()
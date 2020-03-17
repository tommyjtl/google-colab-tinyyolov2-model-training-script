import os, random

num_lines = sum(1 for line in open('train.txt'))
print(num_lines)

f=open('train.txt')
lines=f.readlines()

cont_line = random.sample(range(num_lines), int(num_lines/2))
print(cont_line)

for i in range(0,int(num_lines/2),1):
	content = lines[cont_line[i]]
	print(content)
	with open("test.txt", "a") as myfile:
		myfile.write(content)
	
f.close()

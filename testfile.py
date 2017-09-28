#!/usr/bin/env python3 
import testmode

print('test file Function',end='')
print('*'*50)

fd=open("sample.txt")
test=fd.readline()  #read a line
print(test)
test=fd.read()  #read all content
print(test)
fd.close()
# nyy,shift+p,u,dd
fd=open("sample.txt")
test=fd.readlines()  #read all line
print(test)
fd.close()

fd=open("sample.txt")
for test in fd:
	print(test,end='')
fd.close()
print('test write****************')
#fd=open("sample.txt",'a')
#fd.write('write a new line1\n')
#fd.write('write a new line2\n')
#fd.write('write a new line3\n')
#fd.write('write a new line4\n')
#fd.close()

fd=open("sample.txt")
test=fd.read()
print(test)
fd.close()

print('test sys modes*************')
import sys
print("First value ",sys.argv[0])
print('All values ')
for i,x in enumerate(sys.argv):
	print(i,x)

print('test sys and os modes*************')
import os
import sys
def parse_file(path):
	"""
	:arg path: file path name
	:return: include sparces,tabs,line of yuanzu
	"""
	fd=open(path)
	i=0
	spaces=0
	tabs=0
	for i,line in enumerate(fd):
		spaces += line.count(' ')
		tabs += line.count('\t')
	fd.close()
	return spaces,tabs,i+1

def main(path):
	"""
	:arg path: path
	:return: True or False
	"""
	if os.path.exists(path):
		print(parse_file.__doc__)
		spaces,tabs,lines=parse_file(path)
		print("Spaces {}. tabs {}. lines {}".format(spaces,tabs,lines))
		return True
	else:
		return False
if __name__ == '__main__':
	if len(sys.argv)>1:
		main(sys.argv[1])
	else:
		print('main para less 2')
		#sys.exit(-1)
#	sys.exit(0)

print('************test with keys*************')
with open('sample.txt') as fobj:
	for line in fobj:
		print(line,end='')
print('************test lscpu keys*************')
with open('/proc/cpuinfo') as fobj:
	for line in fobj:
		print(line,end='')

















































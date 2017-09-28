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
fd=open("sample.txt",'a')
fd.write('write a new line1\n')
fd.write('write a new line2\n')
fd.write('write a new line3\n')
fd.write('write a new line4\n')
fd.close()

fd=open("sample.txt")
test=fd.read()
print(test)
fd.close()











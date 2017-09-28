#!/usr/bin/env python3

import helloworld
print('*'*50)
def change():
	global a
	a=90
	print(a)

a=9
print('befor :{:4}'.format(a))
change()
print('after :',a)

def test(a,b=-99):   #defult para value," def test(a,b=-99,c)" is erro
	if a>b:
		return True
	else:
		return False
test(12,23)
test(12)

def f(a,data=[]):
	data.append(a)
	return data

print(f(1))
print(f(2))
print(f(3))	

def ff(a,data=None):
	if data is None:
		data=[]
	data.append(a)
	return data
print(ff(1))
print(ff(2))
print(ff(3))















	


















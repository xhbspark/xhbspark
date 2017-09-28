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

print('docstrings**********')
import math
def longest_side(a,b):
	"""
	Function to find the length of the longest side of a right triangle.
	:arg a: Side a of the triangle 
	:arg b: Side b of the triangle
	:return: Length of the longest side c as float
	"""
	return math.sqrt(a*a+b*b)
print('print(longest_side.__doc__)')
print(longest_side.__doc__)
print('side: ',longest_side(4,5))
























	


















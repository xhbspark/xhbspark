#!/usr/bin/env/ python3
print('Hello World')

#number = int(input("Enter an integer:"))
#if number < 1000:
#	print("Your number is samller than 100")
#else:
#	print("Your number is greater than 100")

#amout = float(input("Enter amount: "))
#inrate = float(input("Enter Interest rate: "))
#period = int(input("Enter period: "))
#value = 0
#year = 1

#while year <= period:
#	value = amout+(inrate*amout)
#	print("Year {} Rs. {:.2f}".format(year,value))
#	amout = value
#	year = year + 1

import math

v=math.pi*2*2
print("hat {} val {:.5f}".format(2,v))

i=1
print("-"*50)
while i<11:
	n=1
	while n<=10:
		print("{:4d}".format(i*n),end=' ')
		n += 1
	print()
	i += 1
print("-"*50)

a=['xiao','hai','bin']
for x in a:
	print(x,end=' ')
print()

print('list: ')
print(list(range(1,15,3)))

def pali(s):
	return s==s[::-1]
if __name__ == '__main__':
	s=input("please enter string: ")
#a=s[::-1]
#if a==s:
	if pali(s):
		print("this is pali")
	else:
		print("this is not pali")

file=open('/home/shiyanlou/xhbspark/String.txt')
filetext=file.read()
print(filetext)
x=0
#while x<len(filetext):
for x in filetext[::]:
	if x.isdigit():
		print(x,end='')
#	t=filetext[x]
#	if t.isdigit():
#		print(t,end='')
#	x = x+1
print()













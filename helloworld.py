#!/usr/bin/env/ python3
print('Hello World')

#number = int(input("Enter an integer:"))
#if number < 1000:
#	print("Your number is samller than 100")
#else:
#	print("Your number is greater than 100")

amout = float(input("Enter amount: "))
inrate = float(input("Enter Interest rate: "))
period = int(input("Enter period: "))
value = 0
year = 1

while year <= period:
	value = amout+(inrate*amout)
	print("Year {} Rs. {:.2f}".format(year,value))
	amout = value
	year = year + 1





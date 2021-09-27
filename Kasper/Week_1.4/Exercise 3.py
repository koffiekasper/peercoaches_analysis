#!/bin/python3

outputstr = ""

inputNo = int(input("Enter a number: "))

i = 0

while i <= inputNo:
	if i % 3 == 0:
		outputstr += "Fizz"
	if i % 5 == 0:
		outputstr += "Buzz"
	if outputstr == "":
		outputstr += str(i)
	print(outputstr)
	outputstr = ""
	i += 1

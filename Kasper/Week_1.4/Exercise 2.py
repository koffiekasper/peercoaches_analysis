#!/bin/python3

limit = int(input("How big will the pyramid be: "))

i = 0
pyr = ""
while i < limit:
	pyr += "#"
	print(pyr)
	i += 1
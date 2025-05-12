#!/usr/bin/env python3
nbr = input("Give me a number: ")

if nbr.type == float(nbr):
	print("This number is a decimal")
elif nbr == int(nbr):
	print("This number is an integer")
# try:
# except:
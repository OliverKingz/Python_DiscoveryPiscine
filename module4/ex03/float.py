#!/usr/bin/env python3

nbr_str = input("Give me a number: ")

try:
	nbr_float = float(nbr_str)
	if nbr_float == int(nbr_float):
		print("This number is a integer")
	else:
		print("This number is an decimal")

except ValueError:
	print("Error: Invalid input. Please enter a valid number.")
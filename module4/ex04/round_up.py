#!/usr/bin/env python3

nbr_str = input("Give me a number: ")

try:
	nbr_float = float(nbr_str)
	nbr_integer_part = int(nbr_float)
	if nbr_integer_part == nbr_float:
		nbr_rounded_up = nbr_integer_part
	else:
		nbr_rounded_up = nbr_integer_part + 1
	print(nbr_rounded_up)
except ValueError:
	print("Invalid input. Please enter a valid number.")

# import math
# try:
# 	nbr_float = float(nbr_str)
# 	nbr_rounded_up = math.ceil(nbr_float)
# 	print(nbr_rounded_up)
# except ValueError:
# 	print("Invalid input. Please enter a valid number.")
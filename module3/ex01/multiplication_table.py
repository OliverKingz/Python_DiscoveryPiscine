#!/usr/bin/env python3

try:
	nbr = int(input("Enter a number\n"))

	i = 0
	while i <= 9:
		res = i * nbr
		print(i, "x", nbr, "=", res)
		i += 1

except ValueError:
	print("Error: input an integer number.")
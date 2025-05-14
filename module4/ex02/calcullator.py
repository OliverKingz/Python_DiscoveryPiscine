#!/usr/bin/env python3

try:
	nbr1 = int(input("Give me the first number: "))
	nbr2 = int(input("Give me the second number: "))
	print("Thank you!")
	print(nbr1, "+", nbr2, "=", nbr1 + nbr2)
	print(nbr1, "-", nbr2, "=", nbr1 - nbr2)
	if nbr2 != 0:
		print(nbr1, "/", nbr2, "=", int(nbr1 / nbr2))
	else:
		print("Error: second number must be different than 0 to do a divison")
	print(nbr1, "*", nbr2, "=", nbr1 * nbr2)

except ValueError:
	print("Error: input an integer")

# except ZeroDivisionError:
# 	print("Error: second number must be different than 0")
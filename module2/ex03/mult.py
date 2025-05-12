#!/usr/bin/env python3
print("Enter the first number: ")
nbr1 = int(input())
print("Enter the second number: ")
nbr2 = int(input())
mult = nbr1 * nbr2

print(nbr1, "X", nbr2, "=", mult)
if mult > 0:
	print("The result is positive.")
elif mult < 0:
	print("The result is negative.")
elif mult == 0:
	print("The result is positive and negative.")
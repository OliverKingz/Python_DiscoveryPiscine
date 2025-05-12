#!/usr/bin/env python3
print("Enter a number less than 25")
i = int(input())

if i > 25:
	print("Error")

while i <= 25:
	print("Inside the loop, my variable is", i)
	i += 1
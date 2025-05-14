#!/usr/bin/env python3

try:
	og_arr = [2, 8, 9, 48, 8, 22, -12, 2]
	print(og_arr)

	og_set = set(og_arr)
	new_arr = []
	for num in og_set:
		if (num + 2) > 5:
			new_arr.append(num + 2)

	# print(new_arr)
	# print(set(new_arr))

	print("{", end="")
	for i in range(len(new_arr)):
		print(new_arr[i], end="")
		if i != len(new_arr) - 1:
			print(", ", end="")
	print("}")

except TypeError:
	print("Error casting")
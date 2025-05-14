#!/usr/bin/env python3

"""
?> ./string_are_arrays.py | cat -e
none$
?> ./string_are_arrays.py "The character Z is not found in this string" | cat -e
none$
?> ./string_are_arrays.py "The character z is found in this string" | cat -e
z$
?> ./string_are_arrays.py "Zaz visits the zoo with Zazie" | cat -e
zzz$
?>
"""

import sys

if len(sys.argv) == 2:

	counter = 0
	for i in range(len(sys.argv[1])):
		if sys.argv[1][i] == 'z':
			counter = counter + 1
			print("z", end="")
	if counter == 0:
		print("none")
	else:
		print()

else:
	print("none")
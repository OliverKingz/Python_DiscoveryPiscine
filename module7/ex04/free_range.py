#!/usr/bin/env python3

"""
?> ./free_range.py | cat -e
none$
?> ./free_range.py 10 14 | cat -e
[10, 11, 12, 13, 14]$
?>
"""

import sys

try:
	if len(sys.argv) == 3:
		start = int(sys.argv[1])
		end = int(sys.argv[2])
		array = list(range(start, end + 1))
		print(array)

	else:
		print("none")

except ValueError:
	print("Error: enter an integer as parameters")
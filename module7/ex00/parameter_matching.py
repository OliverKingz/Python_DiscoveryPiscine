#!/usr/bin/env python3

"""
?> ./parameter_matching.py
none
?> ./parameter_matching.py "Hello"
What was the parameter? Bonjour
Nope, sorry...
?> ./parameter_matching.py "Hello"
What was the parameter? Hello
Good job!
?>
"""

import sys

if len(sys.argv) == 2:
	stdin = input("What was the parameter? ")

	if stdin == sys.argv[1]
		print("Good job!")
	else
		print("Nope, sorry...")
else:
	print("none")
#!/usr/bin/env python3

"""
?> ./append_it.py | cat -e
none$
?> ./append_it.py "parallel" "egoism" "human" | cat -e
parallelism$
humanism$
?>
"""

import sys, re

if len(sys.argv) > 1:
	for x in sys.argv:
		if re.search("ism", x):
			print(x)
		else:
			print(x + "ism")

else:
	print("none")
#!/usr/bin/env python3

import sys

# if len(sys.argv) > 2:
# 	for i in range(1, len(sys.argv)):
# 		print(sys.argv[len(sys.argv) - i])
# else:
# 	print("none")

## Another method
if len(sys.argv) > 2:
	reversed_args = sys.argv[1:][::-1]
	for arg in reversed_args:
		print(arg)
else:
 	print("none")
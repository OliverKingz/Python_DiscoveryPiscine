#!/usr/bin/env python3

import sys, re

if len(sys.argv) == 3:
	keyword = sys.argv[1]
	to_be_searched = sys.argv[2]
	count_keywords = re.findall(keyword, to_be_searched).count(keyword)
	print(count_keywords)
else:
	print("none")
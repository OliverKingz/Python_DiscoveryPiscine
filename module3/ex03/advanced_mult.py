#!/usr/bin/env python3
table_of = 0
while table_of <= 10:
	print(f"Table of {table_of}:", end=" ")
	i = 0
	while i <= 10:
		res = table_of * i
		print(res, end=" ")
		i += 1
	print()
	table_of += 1
#!/usr/bin/env python3

og_arr = [2, 8, 9, 48, 8, 22, -12, 2]
print(og_arr)

new_arr = []
for x in og_arr:
	if x > 3:
		new_arr.append(x + 2)
print(new_arr)

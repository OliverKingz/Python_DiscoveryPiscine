#!/usr/bin/env python3

og_arr = [2, 8, 9, 48, 8, 22, -12, 2]
print("Original array:", og_arr)

# # Method 1
# new_arr = og_arr.copy()
# i = 0
# while i < len(og_arr):
# 	new_arr[i] = og_arr[i] + 2
# 	i += 1
# print("New array:", new_arr)

# # Method 2
# new_arr = og_arr.copy()
# for i in range(len(new_arr)):
# 	new_arr[i] = new_arr[i] + 2
# print("New array:", new_arr)

# # Method 3
# new_arr = [x + 2 for x in og_arr]
# print("New array:", new_arr)

# # Method 4
new_arr = []
for x in og_arr:
	new_arr.append(x + 2)
print("New array:", new_arr)

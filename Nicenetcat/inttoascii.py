#!/usr/bin/python
string = open("output.txt", "r")
string = str(string.read().replace("\n", ""))
parts = list(map(int, string.split()))
for x in parts:
	print(chr(x), end= '')
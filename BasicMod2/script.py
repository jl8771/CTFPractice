#!/usr/bin/python
in_file = open('message.txt', 'r')
str = in_file.read()
out_file = open('flag.txt', 'w')
keys = list("_abcdefghijklmnopqrstuvwxyz0123456789_")
output = 'picoCTF{'

rawValues = str.split()
for i in range(len(rawValues)):
	value = int(rawValues[i])
	prime = 41
	charValue = pow(value, prime-2, prime)
	output += keys[charValue]
print(output+'}')
out_file.write(output+'}')
out_file.close()
in_file.close()
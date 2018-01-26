import os, sys

file_name = sys.argv[1]
with open(file_name, 'r') as inFile:
	for line in inFile:
		print line
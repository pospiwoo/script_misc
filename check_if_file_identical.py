import sys
import os

infilename1 = sys.argv[1]
infilename2 = sys.argv[2]
with open(infilename1, 'r') as inFile1, \
        open(infilename2, 'r') as inFile2:
    data1 = inFile1.readlines()
    data2 = inFile2.readlines()

if data1 == data2:
    print 'two files are identical', True
else:
    print 'two files are different', False

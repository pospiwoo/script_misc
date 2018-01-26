import sys, os

infilename = sys.argv[1]
outfilename = sys.argv[2]
inFile = open(infilename, 'r')
oFile = open(outfilename, 'w')
for line in inFile:
    if line.startswith('#'):
        continue
    oFile.write('chr'+line)





import sys

in_file_name = sys.argv[1]
oFile = open(in_file_name.replace(
    '.vcf', '_' + 'simple' + '.vcf'), 'w')
prev_chr = ''
with open(in_file_name, 'r') as inFile:
    for line in inFile:
        if line.startswith('#'):
            continue
        data = line.split('\t')
        # if not data[0].startswith('chr'):
        #     data[0] = 'chr' + data[0]
        CHROM = data[0]
        # POS = int(data[1])
        # ID = data[2]
        # REF = data[3]
        # ALT = data[4]
        # QUAL = data[5]
        # FILTER = data[6]
        # INFO = data[7]
        if CHROM.count('_') > 0:
            continue
        oFile.write(line)
oFile.close()
# CHROM  POS ID  REF ALT QUAL    FILTER  INFO

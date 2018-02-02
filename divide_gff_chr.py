import sys

replace_chr = 'chr'
gff_or_gtf = '.gff3'
replace_chr = ''
gff_or_gtf = '.gtf'
in_file_name = sys.argv[1]
oFile = open(in_file_name.replace(gff_or_gtf, '_' + 'empty' + gff_or_gtf), 'a')
prev_chr = ''
with open(in_file_name, 'r') as inFile:
    for line in inFile:
        if line.startswith('#'):
            continue
        data = line.split('\t')
        if not data[0].startswith('chr'):
            data[0] = 'chr' + data[0]
        CHROM = data[0]  # chr1
        REF = data[1]  # hg19_knownGene
        TYPE = data[2]  # exon
        START = data[3]  # 12613
        END = data[4]  # 12721
        VAL = data[5]  # 0.000000
        STRND = data[6]  # +
        STR = data[7]  # .
        INFO = data[8]  # gene_id "uc001aaa.3"; transcript_id "uc001aaa.3";
#Parent=transcript:ENST00000637938;Name=ENSE00002040385;constitutive=0;ensembl_end_phase=0;ensembl_phase=-1;exon_id=ENSE00002040385;rank=1;version=1
        if CHROM != prev_chr:
            oFile.close()
            # .replace('_20170403','')
            oFile = open(in_file_name.replace(
                gff_or_gtf, '_' + CHROM + gff_or_gtf), 'a')
            prev_chr = CHROM
        if gff_or_gtf == '.gff':
            oFile.write(replace_chr + line)
        elif gff_or_gtf == '.gtf':
            write_str = ''
            write_str += CHROM + '\t'
            write_str += REF + '\t'
            write_str += TYPE + '\t'
            write_str += START + '\t'
            write_str += END + '\t'
            write_str += VAL + '\t'
            write_str += STRND + '\t'
            write_str += STR + '\t'
            info_list = INFO.split(';')
            info_str = ''
            for i in info_list:
                if i.find('gene_id') > -1:
                    info_str += 'Parent=' + i.replace('\"','').replace('gene_id ', '') + ';'
                if i.find('transcript_id') > -1:
                    info_str += 'Name=' + i.replace('\"','').replace('transcript_id ', '') + ';'
                # elif i == 'exon_id=':
                #     info_str += 'transcript_id \"' + i.replace('exon_id=', '') + '\"; '
            write_str += info_str + '\n'
            oFile.write(write_str)
oFile.close()
# CHROM  POS ID  REF ALT QUAL    FILTER  INFO

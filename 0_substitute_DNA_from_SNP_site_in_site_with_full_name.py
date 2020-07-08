#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a script to substitute DNA from SNP site id '
__author__ = 'Sheng Zuo'
# Usage: python3 script.py seqFile SNPFile outfile

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("seqFile", help="input a sequence file", type=str)
parser.add_argument("SNPFile", help="input a SNP file", type=str)
parser.add_argument("outfile", help="output a sequence file", type=str)
args = parser.parse_args()
seq_fa = args.seqFile
SNP = args.SNPFile
outseq = args.outfile


def read_seq_fasta(filename):
	f = open(filename, 'r')
	victor = {}
	for line in f:
		line = line.strip('\n')
		temp = line.split('\t')
		ID = '>'+temp[0]+'_'+temp[1]
		victor[ID] = temp[2]
	return victor
SNP_pos = read_seq_fasta(SNP)

#for i,j in SNP_pos.items():
#	print(i,j)

if __name__ == "__main__":
	with open(seq_fa,'r')as f1, open(outseq,'a') as f:	
		for line in f1:
			line = line.strip('\n')
			temp = line.split('\t')
			temp1 = temp[0].split('_')
			seq_name = temp1[0]+'_'+temp1[4]
			if seq_name in SNP_pos.keys():
				f.write(temp[0]+'\n'+SNP_pos[seq_name]+'\n')
			else:
				f.write(temp[0]+'\n'+temp[1]+'\n')

		
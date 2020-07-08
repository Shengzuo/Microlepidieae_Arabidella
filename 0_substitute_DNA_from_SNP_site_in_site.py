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
sequence = args.seqFile
SNP = args.SNPFile
outseq = args.outfile


def read_seq_fasta(filename):
	f = open(filename, 'r')
	victor = {}
	for line in f:
		if line.startswith('>'):           
			ID = line.strip('\n')
		else:           
			victor[ID] = line.strip('\n')
	return victor
seq = read_seq_fasta(sequence)

#for i,j in seq.items():
	#print(i,j)

if __name__ == "__main__":
	with open(SNP,'r')as f1, open(outseq,'a') as f:	
		for line in f1:
			line1 = line.strip('\n')
			temp = line1.split('\t')
			SNP_name = '>'+temp[0]+'_'+temp[1]
			if SNP_name in seq.keys():
				seq[SNP_name] = temp[2]
			else:
				pass
		for i,j in seq.items():
			#print(i,j)
			f.write(i+'\n'+j+'\n')


		
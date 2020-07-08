#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a script to extract from blast result id '
__author__ = 'Sheng Zuo'
# Usage: python3 script.py seqFile tabFile outfile

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("seqFile", help="input a sequence file", type=str)
parser.add_argument("tabFile", help="input a table file", type=str)
parser.add_argument("outfile", help="output a sequence file", type=str)
args = parser.parse_args()
sequence = args.seqFile
id_file = args.tabFile
outseq = args.outfile


def readfasta(filename):
	fa = open(filename, 'r')
	victor = {}
	
	for line in fa:
		if line.startswith('>'):           
			ID = line.strip('\n')
		else:           
			victor[ID] = line.strip('\n')
	return victor
seq = readfasta(sequence)


if __name__ == "__main__":
	
	with open(id_file,'r')as f1, open(outseq,'a') as f:	
		for line in f1:
			line1 = line.strip('\n')
			temp = line.split('\t')
			temp1 = temp[0]
			temp2 = temp1.split('-')
			enq_name = '>'+(temp2[0]).split('_')[0]
			enq_position = temp2[1]
			if enq_name in seq.keys():	
				f.write('>'+temp1+'\t')
				values = seq[enq_name]
				f.write(str(values[int(enq_position)-1]) + '\n')
			else:
				pass
		


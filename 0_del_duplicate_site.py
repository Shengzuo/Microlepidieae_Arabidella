#!/usr/bin/env python3
# -*- coding: utf-8 -*-


__author__ = 'Sheng Zuo'
# Usage: python3 script.py seqFile tabFile outfile

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("seqFile", help="input a sequence file", type=str)

parser.add_argument("outfile", help="output a sequence file", type=str)
args = parser.parse_args()
seq_file = args.seqFile
outseq = args.outfile




if __name__ == "__main__":	
	with open(seq_file,'r')as f1, open(outseq,'a') as f:	
		victor = {}
		for line in f1:
			if line.startswith('>'):           
				ID = line.strip('\n')
			else:           
				victor[ID] = line.strip('\n')

	
		for key,values in victor.items():
			f.write(key+'\n'+values+'\n')
			


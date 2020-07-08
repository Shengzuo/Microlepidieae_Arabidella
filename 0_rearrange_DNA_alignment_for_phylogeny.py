#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a script to substitute DNA from SNP site id '
__author__ = 'Sheng Zuo'
# Usage: python3 script.py seqFile SNPFile outfile

import sys
import os

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("seqFile", help="input a sequence file", type=str)
parser.add_argument("outfile", help="output a sequence file", type=str)
args = parser.parse_args()
sequence = args.seqFile
outseq = args.outfile


def read_seq_fasta(filename):
    # This dict represents the fasta sequences. The keys are sequences name that contains '>'. The values are corresponding sequences.
	fa = open(filename, 'r')
	victor = []
	
	for line in fa:
		if line.startswith('>'):           
			pass
		else:           
			victor.append(line.strip('\n'))
	return victor
seq = read_seq_fasta(sequence)


with open(outseq,'a') as f:	
	file_name = os.path.basename(sys.argv[1])	
	species_name = file_name.split('.')
	f.write(">"+species_name[0]+'\n')
	
	for i in seq:
		f.write(i)






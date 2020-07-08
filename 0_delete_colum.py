#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a script to substitute DNA from SNP site id '
__author__ = 'Sheng Zuo'
# Usage: python3 script.py seqFile SNPFile outfile

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
	victor = {}
	ID = ''
	for line in fa:
		if line.startswith('>'):           
			ID = line.strip('\n')
			victor[ID] = ''
		else:           
			victor[ID] += line.strip('\n')
	return victor
seq = read_seq_fasta(sequence)

seq_key_name = []
for key in seq.keys():
	seq_key_name.append(key)



position = []

for i in range(len(seq[">Pachycladon_exilis"])): #get whole sequence length cycle
	count = 0
	for j in range(len(seq_key_name)):
		if seq[seq_key_name[j]][i] == seq[">Pachycladon_exilis"][i]:
			count +=1
		else:
			pass
	if count >1:
		position.append(i)
	else:
		pass



with open(outseq,'a') as f:	
	for i in range(len(seq_key_name)):
		f.write('\n'+seq_key_name[i]+'\n')
		for j in range(len(position)):
			f.write(seq[seq_key_name[i]][position[j]])
		
	

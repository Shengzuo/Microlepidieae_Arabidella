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




def read_SNP_site(filename):
	#This function is processed the SNP id file.
	tables = open(filename, 'r')
	apple = {}
	ID = ''
	for line in tables:
		line = line.strip('\n')
		ab = line.split("\t",2)
		ID = ab[0]+'_'+ab[1]
		apple[ID] = ab[2]
	return apple
SNP_position = read_SNP_site(SNP)


for i in SNP_position.keys():
	x = i.split("_")
	xy = int(x[1])
	y = x[0]
		
	for j in seq.keys():
		if y in j:
			xz = ''
			xz = j.split("_",2)
			if xy>=int(xz[1]) and xy <= int(xz[2]):
				xa = xy-int(xz[1])
				xb = seq[j]
				seq[j]= str(xb[:int(xa)]) + str(SNP_position[i]) + str(xb[int(xa+1):])			
			else:
				pass				
		else:
			pass


with open(outseq,'a') as f:	
	for key,values in seq.items():
		f.write(key+'\n')
		f.write(values+'\n')
		
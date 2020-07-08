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
table = args.tabFile
outseq = args.outfile


def readfasta(filename):
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
seq = readfasta(sequence)


def readid(filename):
	#This function is processed the table id file.
	tables = open(filename, 'r')
	apple = {}
	ID = ''
	for line in tables:
		line = line.strip('\n')
		ab = line.split("\t",2)
		ID = ab[0]+'_'+ab[1]+'_'+ab[2]
		apple[ID] = ab[1:]
	return apple
enquiry = readid(table)


seq_name =[]
for i in seq.keys():
	seq_name.append(i)
	
with open(outseq,'a') as f:	
	for i in enquiry.keys():
		ac = i.split('_',2)
		k = ac[0]
		if k in seq_name:	
			f.write(i+'\n')
			aa = seq[k]
			bb = enquiry[i]
			f.write(str(aa[(int(bb[0])-1):int(bb[1])]) + '\n')
		else:
			pass
	


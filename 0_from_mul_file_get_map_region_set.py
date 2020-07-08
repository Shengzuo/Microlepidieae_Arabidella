#!/usr/bin/env python3
# -*- coding: utf-8 -*-


__author__ = 'Sheng Zuo'
# Usage: python3 script.py seqFile SNPFile outfile

import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("inputfile", help="input a sequence file", type=str)
parser.add_argument("outfile", help="output a sequence file", type=str)
args = parser.parse_args()

input_file = args.inputfile
out_file = args.outfile



if __name__ == "__main__":
	with open(input_file,'r') as read1:
		input_name = []
		for line in read1:
			line1 = line.strip('\n')
			input_name.append(line1)
	
	victor = {}		
	for i in input_name:
		with open(i,'r') as f:
			single_position = {}
			for line in f:
				line = line.strip('\n')
				temp = line.split('\t')
				for i in range(int(temp[1]),int(temp[2])+1):
					key = temp[3]+'-'+str(i)
					single_position[key] = 1
			for keys in single_position.keys():
				if keys in victor.keys():
					victor[keys] = int(victor[keys])+1
				else:
					victor[keys] = 1
							
	with open(out_file,'a') as f1:
		for key,value in victor.items():			
			f1.write(str(key)+'\t'+str(value)+'\t'+'\n')



#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a script to substitute DNA from SNP site id '
__author__ = 'Sheng Zuo'
# Usage: python3 script.py seqFile SNPFile outfile

import argparse
parser = argparse.ArgumentParser()

parser.add_argument("SNPFile", help="input a SNP file", type=str)

args = parser.parse_args()

mapping = args.SNPFile


with open(mapping, 'r') as f:
	victor = []
	sum = 0
	for line in f:
		line = line.strip('\n')        
		temp = line.split('\t') 
		x = int(temp[2])-int(temp[1])+1
		sum += x
	print(sum)
	

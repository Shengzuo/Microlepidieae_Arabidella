#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os


if __name__ == "__main__":
	list_file1 = open('./list1','r')
	victor = []
	for line in list_file1:
		line1 = line.strip('\n')
		victor.append(line1)
		temp = line1.split('.')
	out_name = temp[0]+'_consen.bed'
	cmd = ['bedtools','intersect','-a',victor[1],'-b',victor[0],'>',out_name]
	print(" ".join(cmd))
	#os.system(" ".join(cmd))

	list_file2 = open('./list2','r')
	for line in list_file2:
		line2 = line.strip('\n')
		temp2 = line2.split('.')
		new_out_name = temp2[0]+'_consen.bed'
		cmd = ['bedtools','intersect','-a',out_name,'-b',line2,'>',new_out_name]
		print(" ".join(cmd))
		#os.system(" ".join(cmd))
		out_name = new_out_name
		
class BED:
	
	def _init_(self):
		pass

	def Readfile(self, filename):
		handle = open(filename,'r')
		matrix_of_bed_file = []
		for line in handle:
			temp = line.strip().split('\t')
			temp2 = list(temp)
			matrix_of_bed_file.append(temp2)
		return matrix_of_bed_file
	
	def ConvertBEDtoWiggle(self, BED):
		total = 0
		wiggle_header = 'track type=wiggle_0\nfixedStep chrom='
		wiggle_matrix = []
		previous_chromosome_name = 'null'
		for line in BED:
			if(line[0] != previous_chromosome_name):
				wiggle_matrix.append(wiggle_header+line[0]+'\n')
				previous_chromosome_name = line[0]
			start = int(line[1])
			end = int(line[2])
			for i in range(start,end):
				wiggle_matrix.append(line[3])
				total += float(line[3])
		return wiggle_matrix, round(total)
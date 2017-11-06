import numpy
#open the file assuming the data above is in a file called 'dataFile'
inFile = open('dataFile','r')
#save the column/row headers (conditions/genes) into an array
colHeaders = inFile.next().strip().split()[1:]
rowHeaders = []
dataMatrix = []

for line in inFile:
	data = line.strip().split('\t')
	rowHeaders.append(data[0])
	dataMatrix.append([float(x) for x in data[1:]])

#convert native data array into a numpy array
dataMatrix = numpy.array(dataMatrix)

distanceMatrix = dist.pdist(dataMatrix)

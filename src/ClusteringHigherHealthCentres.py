import csv
import matplotlib.pyplot as plt

def isInteger(str):
	try:
		num = int(str)
	except ValueError:
		return False
	return True

def intValueOf(str):
	if isInteger(str):
		return int(str)
	else:
		return 0

subDivisionalHospitals = []
districtHospitals = []

maxSubDivisionalHospitals = 0
maxDistrictHospitals = 0

datasetList = []

with open('../data/MergedWithLowerHealthLevel.csv', 'r') as dataset:
	headingRow = True
	datasetList = list(dataset)
	for row in datasetList:
		
		if headingRow:
			headingRow = False
			continue
		
		rowList = row.split(",")

		totalPopulation = intValueOf(rowList[8].strip())

		noOfSubDivisional = intValueOf(rowList[20].strip()) * (10 ** 5) / (3 * totalPopulation)
		noOfDistrict = intValueOf(rowList[21].strip()) * (10 ** 5) / totalPopulation

		maxSubDivisionalHospitals = noOfSubDivisional if noOfSubDivisional > maxSubDivisionalHospitals else maxSubDivisionalHospitals
		maxDistrictHospitals = noOfDistrict if noOfDistrict > maxDistrictHospitals else maxDistrictHospitals

		subDivisionalHospitals.append(noOfSubDivisional)
		districtHospitals.append(noOfDistrict)

higherHealthLevel = []
for i in range(len(datasetList)):
	higherHealthLevel.append(0)

centroid1 = [0, 0] # red
centroid2 = [maxSubDivisionalHospitals / 2, 0] # green
centroid3 = [0, maxDistrictHospitals / 4] # blue

def findColourFor(index):
	minDistanceCentroid = findMinDistanceCentroid(index)
	if minDistanceCentroid == 1:
		return 'red'
	elif minDistanceCentroid == 2:
		return 'green'
	elif minDistanceCentroid == 3:
		return 'blue'

def findMinDistanceCentroid(index):
	minDistance = findDistance(index, centroid1)
	minCentroid = 1
	if findDistance(index, centroid2) < minDistance:
		minDistance = findDistance(index, centroid2)
		minCentroid = 2
	if findDistance(index, centroid3) < minDistance:
		minDistance = findDistance(index, centroid3)
		minCentroid = 3
	return minCentroid

def findDistance(index, centroid):
	return ((centroid[0] - subDivisionalHospitals[index]) ** 2 + (centroid[1] - districtHospitals[index]) ** 2) ** 1 / 2

for times in range(4):
	sumCentroid1 = [0, 0]
	sumCentroid2 = [0, 0]
	sumCentroid3 = [0, 0]

	noOfElementsCentroid1 = 0
	noOfElementsCentroid2 = 0
	noOfElementsCentroid3 = 0
	for index in range(len(subDivisionalHospitals)):
		colour = findColourFor(index);
		if colour == 'red':
			higherHealthLevel[index] = 1
			noOfElementsCentroid1 += 1
			sumCentroid1 = [sumCentroid1[0] + subDivisionalHospitals[index], sumCentroid1[1] + districtHospitals[index]]
			if noOfElementsCentroid1 == 1 and times == 3:
				plt.scatter(subDivisionalHospitals[index], districtHospitals[index], c = colour, label = 'Level 1')
			else:
				plt.scatter(subDivisionalHospitals[index], districtHospitals[index], c = colour)

		elif colour == 'green':
			higherHealthLevel[index] = 2
			noOfElementsCentroid2 += 1
			sumCentroid2 = [sumCentroid2[0] + subDivisionalHospitals[index], sumCentroid2[1] + districtHospitals[index]]
			if noOfElementsCentroid2 == 2 and times == 3:
				plt.scatter(subDivisionalHospitals[index], districtHospitals[index], c = colour, label = 'Level 2')
			else:
				plt.scatter(subDivisionalHospitals[index], districtHospitals[index], c = colour)
		elif colour == 'blue':
			higherHealthLevel[index] = 3
			noOfElementsCentroid3 += 1
			sumCentroid3 = [sumCentroid3[0] + subDivisionalHospitals[index], sumCentroid3[1] + districtHospitals[index]]
			if noOfElementsCentroid3 == 1 and times == 3:
				plt.scatter(subDivisionalHospitals[index], districtHospitals[index], c = colour, label = 'Level 3')
			else:
				plt.scatter(subDivisionalHospitals[index], districtHospitals[index], c = colour)

	if noOfElementsCentroid1 != 0:
		centroid1 = [sumCentroid1[0] / noOfElementsCentroid1, sumCentroid1[1] / noOfElementsCentroid1]
	if noOfElementsCentroid2 != 0:
		centroid2 = [sumCentroid2[0] / noOfElementsCentroid2, sumCentroid2[1] / noOfElementsCentroid2]
	if noOfElementsCentroid3 != 0:
		centroid3 = [sumCentroid3[0] / noOfElementsCentroid3, sumCentroid3[1] / noOfElementsCentroid3]

finalList = []
finalList.append(['State', 'District', 'SC Current', 'ST Current', 'General Current', 'SC Covered', 'ST Covered', 'General Covered', 'Total Population', 'Percentage SC', 'Percentage SC covered',  'Percentage ST', 'Percentage ST covered',  'Percentage General', 'Percentage General Covered', 'State Index', 'Backward Concentrated', 'Number of Sub Centres', 'Number of Primary Health Centres', 'Number of Community Health Centres', 'Sub Divisional Hospitals', 'District Hospitals', 'Lower Health Centre Level', 'Higher Health Centre Level'])
headingRow = True
for row in range(len(datasetList)):
	if headingRow:
		headingRow = False
		continue
		
	rowList = datasetList[row].split(",")
	rowList[len(rowList) - 1] = rowList[len(rowList) - 1].strip()
	rowList.append(higherHealthLevel[row - 1])
	finalList.append(rowList)

with open('../data/MergedWithHealthLevels.csv', 'w') as merged:
	writer = csv.writer(merged)
	writer.writerows(finalList)


plt.legend()
plt.xlabel('Normalised Sub Divisional Hospitals')
plt.ylabel('Normalised District Hospitals')
plt.show()
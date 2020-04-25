import csv
from mpl_toolkits.mplot3d import Axes3D
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

subCentres = []
primaryCentres = []
communityCentres = []
subDivisionalHospitals = []
districtHospitals = []

maxSubCentres = 0
maxPrimaryCentres = 0
maxCommunityCentres = 0
maxSubDivisionalHospitals = 0
maxDistrictHospitals = 0

datasetList = []

with open('../data/AddedAttributesMerged.csv', 'r') as dataset:
	datasetList = list(dataset)

	headingRow = True
	for row in datasetList:
		
		if headingRow:
			headingRow = False
			continue
		
		rowList = row.split(",")

		totalPopulation = intValueOf(rowList[8].strip())

		noOfSubCentres = intValueOf(rowList[17].strip()) * (10 ** 5) / (20 * totalPopulation)
		noOfPrimaryCentres = intValueOf(rowList[18].strip()) * (10 ** 5) / (5 * totalPopulation)
		noOfCommunityCentres = intValueOf(rowList[19].strip()) * (10 ** 5) * 2 / totalPopulation
		noOfSubDivisional = intValueOf(rowList[20].strip()) * (10 ** 5) / (3 * totalPopulation)
		noOfDistrict = intValueOf(rowList[21].strip()) * (10 ** 5) / totalPopulation

		maxSubCentres = noOfSubCentres if noOfSubCentres > maxSubCentres else maxSubCentres
		maxPrimaryCentres = noOfPrimaryCentres if noOfPrimaryCentres > maxPrimaryCentres else maxPrimaryCentres
		maxCommunityCentres = noOfCommunityCentres if noOfCommunityCentres > maxCommunityCentres else maxCommunityCentres
		maxSubDivisionalHospitals = noOfSubDivisional if noOfSubDivisional > maxSubDivisionalHospitals else maxSubDivisionalHospitals
		maxDistrictHospitals = noOfDistrict if noOfDistrict > maxDistrictHospitals else maxDistrictHospitals

		subCentres.append(noOfSubCentres)
		primaryCentres.append(noOfPrimaryCentres)
		communityCentres.append(noOfCommunityCentres)
		subDivisionalHospitals.append(noOfSubDivisional)
		districtHospitals.append(noOfDistrict)
		
lowerHealthLevel = []
for i in range(len(datasetList)):
	lowerHealthLevel.append(0)

centroidLower1 = [0, 0, 0] # red
centroidLower2 = [maxSubCentres / 3, maxPrimaryCentres / 3, maxCommunityCentres / 3] # green
centroidLower3 = [maxSubCentres * 2 / 3 , maxPrimaryCentres * 2 / 3, maxCommunityCentres * 2 / 3] # orange
centroidLower4 = [maxSubCentres, maxPrimaryCentres, maxCommunityCentres] # blue

def findColourForLower(index):
    # find which centroid it is closest to
	minDistanceCentroid = findMinDistanceCentroidLower(index)
	if minDistanceCentroid == 1:
		return 'red'
	elif minDistanceCentroid == 2:
		return 'green'
	elif minDistanceCentroid == 3:
		return 'orange'
	elif minDistanceCentroid == 4:
		return 'blue'
# which centroid is the point closest to in the lower level plot
def findMinDistanceCentroidLower(index):
	minDistance = findDistanceLower(index, centroidLower1)
	minCentroid = 1
	if findDistanceLower(index, centroidLower2) < minDistance:
		minDistance = findDistanceLower(index, centroidLower2)
		minCentroid = 2
	if findDistanceLower(index, centroidLower3) < minDistance:
		minDistance = findDistanceLower(index, centroidLower3)
		minCentroid = 3
	if findDistanceLower(index, centroidLower4) < minDistance:
		minDistance = findDistanceLower(index, centroidLower4)
		minCentroid = 4
	return minCentroid

def findDistanceLower(index, centroid):
	return ((centroid[0] - subCentres[index]) ** 2 + (centroid[1] - primaryCentres[index]) ** 2 + (centroid[2] - communityCentres[index]) ** 2) ** 1 / 2

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
for times in range(4):
	sumCentroid1 = [0, 0, 0]
	sumCentroid2 = [0, 0, 0]
	sumCentroid3 = [0, 0, 0]
	sumCentroid4 = [0, 0, 0]

	noOfElementsCentroid1 = 0
	noOfElementsCentroid2 = 0
	noOfElementsCentroid3 = 0
	noOfElementsCentroid4 = 0
	for index in range(len(subCentres)):
		colour = findColourForLower(index);
		if colour == 'red':
			lowerHealthLevel[index] = 1
			noOfElementsCentroid1 += 1
			sumCentroid1 = [sumCentroid1[0] + subCentres[index], sumCentroid1[1] + primaryCentres[index], sumCentroid1[2] + communityCentres[index]]
			if noOfElementsCentroid1 == 1 and times == 3:
				ax.scatter(subCentres[index], primaryCentres[index], communityCentres[index], c = colour, label = 'Level 1')
			else:
				ax.scatter(subCentres[index], primaryCentres[index], communityCentres[index], c = colour)
		elif colour == 'green':
			lowerHealthLevel[index] = 2
			noOfElementsCentroid2 += 1
			sumCentroid2 = [sumCentroid2[0] + subCentres[index], sumCentroid2[1] + primaryCentres[index], sumCentroid2[2] + communityCentres[index]]
			if noOfElementsCentroid2 == 1 and times == 3:
				ax.scatter(subCentres[index], primaryCentres[index], communityCentres[index], c = colour, label = 'Level 2')
			else:
				ax.scatter(subCentres[index], primaryCentres[index], communityCentres[index], c = colour)
		elif colour == 'orange':
			lowerHealthLevel[index] = 3
			noOfElementsCentroid3 += 1
			sumCentroid3 = [sumCentroid1[0] + subCentres[index], sumCentroid3[1] + primaryCentres[index], sumCentroid3[2] + communityCentres[index]]
			if noOfElementsCentroid3 == 1 and times == 3:
				ax.scatter(subCentres[index], primaryCentres[index], communityCentres[index], c = colour, label = 'Level 3')
			else:
				ax.scatter(subCentres[index], primaryCentres[index], communityCentres[index], c = colour)
		elif colour == 'blue':
			lowerHealthLevel[index] = 4
			noOfElementsCentroid4 += 1
			sumCentroid4 = [sumCentroid4[0] + subCentres[index], sumCentroid4[1] + primaryCentres[index], sumCentroid4[2] + communityCentres[index]]
			if noOfElementsCentroid4 == 1 and times == 3:
				ax.scatter(subCentres[index], primaryCentres[index], communityCentres[index], c = colour, label = 'Level 4')
			else:
				ax.scatter(subCentres[index], primaryCentres[index], communityCentres[index], c = colour)

	if noOfElementsCentroid1 != 0:
		centroidLower1 = [sumCentroid1[0] / noOfElementsCentroid1, sumCentroid1[1] / noOfElementsCentroid1, sumCentroid1[0] / noOfElementsCentroid1]
	if noOfElementsCentroid2 != 0:
		centroidLower2 = [sumCentroid2[0] / noOfElementsCentroid2, sumCentroid2[1] / noOfElementsCentroid2, sumCentroid2[0] / noOfElementsCentroid2]
	if noOfElementsCentroid3 != 0:
		centroidLower3 = [sumCentroid3[0] / noOfElementsCentroid3, sumCentroid3[1] / noOfElementsCentroid3, sumCentroid3[0] / noOfElementsCentroid3]
	if noOfElementsCentroid4 != 0:
		centroidLower4 = [sumCentroid4[0] / noOfElementsCentroid4, sumCentroid4[1] / noOfElementsCentroid4, sumCentroid4[0] / noOfElementsCentroid4]

ax.legend()

ax.set_xlabel('Normalised Sub Centres')
ax.set_ylabel('Normalised Primary Centres')
ax.set_zlabel('Normalised Community Centres')

plt.show()
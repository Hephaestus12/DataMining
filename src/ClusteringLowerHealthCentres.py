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

maxSubCentres = 0
maxPrimaryCentres = 0
maxCommunityCentres = 0

datasetList = []

with open('../data/AddedAttributesMerged.csv', 'r') as dataset:
	headingRow = True
	datasetList = list(dataset)
	for row in datasetList:
		
		if headingRow:
			headingRow = False
			continue
		
		rowList = row.split(",")

		totalPopulation = intValueOf(rowList[8].strip())

		noOfSubCentres = intValueOf(rowList[17].strip()) * (10 ** 5) / (20 * totalPopulation)
		noOfPrimaryCentres = intValueOf(rowList[18].strip()) * (10 ** 5) / (5 * totalPopulation)
		noOfCommunityCentres = intValueOf(rowList[19].strip()) * (10 ** 5) * 2 / totalPopulation

		maxSubCentres = noOfSubCentres if noOfSubCentres > maxSubCentres else maxSubCentres
		maxPrimaryCentres = noOfPrimaryCentres if noOfPrimaryCentres > maxPrimaryCentres else maxPrimaryCentres
		maxCommunityCentres = noOfCommunityCentres if noOfCommunityCentres > maxCommunityCentres else maxCommunityCentres

		subCentres.append(noOfSubCentres)
		primaryCentres.append(noOfPrimaryCentres)
		communityCentres.append(noOfCommunityCentres)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

lowerHealthLevel = []
for i in range(len(datasetList)):
	lowerHealthLevel.append(0)

centroid1 = [0, 0, 0] # red
centroid2 = [maxSubCentres / 3, maxPrimaryCentres / 3, maxCommunityCentres / 3] # green
centroid3 = [maxSubCentres * 2 / 3 , maxPrimaryCentres * 2 / 3, maxCommunityCentres * 2 / 3] # orange
centroid4 = [maxSubCentres, maxPrimaryCentres, maxCommunityCentres] # blue

def findColourFor(index):
	minDistanceCentroid = findMinDistanceCentroid(index)
	if minDistanceCentroid == 1:
		return 'red'
	elif minDistanceCentroid == 2:
		return 'green'
	elif minDistanceCentroid == 3:
		return 'orange'
	elif minDistanceCentroid == 4:
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
	if findDistance(index, centroid4) < minDistance:
		minDistance = findDistance(index, centroid4)
		minCentroid = 4
	return minCentroid

def findDistance(index, centroid):
	return ((centroid[0] - subCentres[index]) ** 2 + (centroid[1] - primaryCentres[index]) ** 2 + (centroid[2] - communityCentres[index]) ** 2) ** 1 / 2

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
		colour = findColourFor(index);
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
		centroid1 = [sumCentroid1[0] / noOfElementsCentroid1, sumCentroid1[1] / noOfElementsCentroid1, sumCentroid1[0] / noOfElementsCentroid1]
	if noOfElementsCentroid2 != 0:
		centroid2 = [sumCentroid2[0] / noOfElementsCentroid2, sumCentroid2[1] / noOfElementsCentroid2, sumCentroid2[0] / noOfElementsCentroid2]
	if noOfElementsCentroid3 != 0:
		centroid3 = [sumCentroid3[0] / noOfElementsCentroid3, sumCentroid3[1] / noOfElementsCentroid3, sumCentroid3[0] / noOfElementsCentroid3]
	if noOfElementsCentroid4 != 0:
		centroid4 = [sumCentroid4[0] / noOfElementsCentroid4, sumCentroid4[1] / noOfElementsCentroid4, sumCentroid4[0] / noOfElementsCentroid4]


#ax.scatter(centroid1[0], centroid1[1], centroid1[2], c = 'brown')
#ax.scatter(centroid2[0], centroid2[1], centroid2[2], c = 'brown')
#ax.scatter(centroid3[0], centroid3[1], centroid3[2], c = 'brown')
#ax.scatter(centroid4[0], centroid4[1], centroid4[2], c = 'brown')

finalList = []
finalList.append(['State', 'District', 'SC Current', 'ST Current', 'General Current', 'SC Covered', 'ST Covered', 'General Covered', 'Total Population', 'Percentage SC', 'Percentage SC covered',  'Percentage ST', 'Percentage ST covered',  'Percentage General', 'Percentage General Covered', 'State Index', 'Backward Concentrated', 'Number of Sub Centres', 'Number of Primary Health Centres', 'Number of Community Health Centres', 'Sub Divisional Hospitals', 'District Hospitals', 'Lower Health Centre Level'])
headingRow = True
for row in range(len(datasetList)):
	if headingRow:
		headingRow = False
		continue
		
	rowList = datasetList[row].split(",")
	rowList[len(rowList) - 1] = rowList[len(rowList) - 1].strip()
	rowList.append(lowerHealthLevel[row - 1])
	finalList.append(rowList)

with open('../data/MergedWithLowerHealthLevel.csv', 'w') as merged:
	writer = csv.writer(merged)
	writer.writerows(finalList)

ax.legend()
plt.title("Fig: Normalized health care centre figure (Lower Level)")
ax.set_xlabel('Normalised Sub Centres')
ax.set_ylabel('Normalised Primary Centres')
ax.set_zlabel('Normalised Community Centres')

plt.show()
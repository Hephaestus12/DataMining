import csv

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

def percentage(big, small):
	if big != 0 and small != 0:
		return small / big * 100
	else:
		return "NA"

with open('../data/healthAndHabitatMerged.csv', 'r') as merged:
	mergedList = list(merged)
	headingRow = True

	stateIndices = dict()

	addedCSVList = []
	addedCSVList.append(['State', 'District', 'SC Current', 'ST Current', 'General Current', 'SC Covered', 'ST Covered', 'General Covered', 'Total Population','Lower Health Index per Capita', 'Higher Health Index per Capita', 'Percentage SC', 'Percentage SC covered',  'Percentage ST', 'Percentage ST covered',  'Percentage General', 'Percentage General Covered', 'State Index', 'Health Level(lower)', 'Health Level(higher)', 'Backward Concentrated'])

	for row in mergedList:
		if headingRow:
			headingRow = False
			continue
		rowList = row.split(",")

		state = rowList[0]
		stateIndex = -1
		if state in stateIndices:
			stateIndex = stateIndices[state]
		else:
			stateIndices[state] = len(stateIndices)
			stateIndex = stateIndices[state]

		backwardConcentrated = 0
		lowerLevel = 0
		higherLevel = 0

		stCurrent = intValueOf(rowList[3])
		scCurrent = intValueOf(rowList[2])
		generalCurrent = intValueOf(rowList[4])
		
		stCovered = intValueOf(rowList[6])
		scCovered = intValueOf(rowList[5])
		generalCovered = intValueOf(rowList[7])

		perStCovered = percentage(stCurrent, stCovered)
		perScCovered = percentage(scCurrent, stCovered)
		perGenCovered = percentage(generalCurrent, generalCovered)

		totalPopulation = stCurrent + scCurrent + generalCurrent

		perSc = percentage(totalPopulation, scCurrent)
		perSt = percentage(totalPopulation, stCurrent)
		if(intValueOf(perSc) + intValueOf(perSt) > 50) :
			backwardConcentrated = 1
		perGen = percentage(totalPopulation, generalCurrent)

		lowerHealthIndexPerCapita = intValueOf(rowList[8]) / totalPopulation * 10 ** 5
		higherHealthIndexPerCapita = intValueOf(rowList[9]) / totalPopulation * 10 ** 5

		if(lowerHealthIndexPerCapita>=0 and lowerHealthIndexPerCapita<37) :
			lowerLevel = 1
		elif(lowerHealthIndexPerCapita>=37 and lowerHealthIndexPerCapita<49) :
			lowerLevel = 2
		elif(lowerHealthIndexPerCapita>=49 and lowerHealthIndexPerCapita<64) :
			lowerLevel = 3
		else :
			lowerLevel = 4
		
		if(higherHealthIndexPerCapita>=0 and higherHealthIndexPerCapita<0.24) :
			higherLevel = 1
		elif(higherHealthIndexPerCapita>=0.24 and higherHealthIndexPerCapita<0.57) :
			higherLevel = 2
		elif(higherHealthIndexPerCapita>=0.57 and higherHealthIndexPerCapita<0.95) :
			higherLevel = 3
		else :
			higherLevel = 4

        
		addedCSVList.append([rowList[0], rowList[1], rowList[2], rowList[3], rowList[4], rowList[5], rowList[6], rowList[7], totalPopulation, lowerHealthIndexPerCapita, higherHealthIndexPerCapita, perSc, perScCovered, perSt, perStCovered, perGen, perGenCovered, stateIndex, lowerLevel, higherLevel, backwardConcentrated])

	#print (stateIndices)
	#print(addedCSVList)

	with open('../data/AddedAttributesMerged.csv', 'w') as merged:
		writer = csv.writer(merged)
		writer.writerows(addedCSVList)
		



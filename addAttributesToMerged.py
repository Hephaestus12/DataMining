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

with open('healthAndHabitatMerged.csv', 'r') as merged:
	mergedList = list(merged)
	headingRow = True

	addedCSVList = []
	addedCSVList.append(['State', 'District', 'SC Current', 'ST Current', 'General Current', 'SC Covered', 'ST Covered', 'General Covered', 'Total Health Centres', 'Total Population', 'People per Health Centre', 'Percentage SC', 'Percentage SC covered',  'Percentage ST', 'Percentage ST covered',  'Percentage General', 'Percentage General Covered'])

	for row in mergedList:
		if headingRow:
			headingRow = False
			continue
		rowList = row.split(",")

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
		perGen = percentage(totalPopulation, generalCurrent)

		peoplePerHealthCentre = "NA"
		if(intValueOf(rowList[8]) != 0):
			peoplePerHealthCentre = totalPopulation / intValueOf(rowList[8])
        
		addedCSVList.append([rowList[0], rowList[1], rowList[2], rowList[3], rowList[4], rowList[5], rowList[6], rowList[7], rowList[8].strip(), totalPopulation, peoplePerHealthCentre, perSc, perScCovered, perSt, perStCovered, perGen, perGenCovered])

	#print(addedCSVList)

	with open('AddedAttributesMerged.csv', 'w') as merged:
		writer = csv.writer(merged)
		writer.writerows(addedCSVList)
		



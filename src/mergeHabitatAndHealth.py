import csv

with open('../data/healthCleanReduced.csv', 'r') as healthCareReducedCSV:
	healthCareReducedList = list(healthCareReducedCSV)
	with open('../data/habitation_reduced.csv', 'r') as habitationReduced:
		habitationReducedList = list(habitationReduced)
		stateSetInHabitation = dict()
		headingRow = True
		indexInHabitation = 1
		for rowHabitation in habitationReducedList:
			if headingRow:
				headingRow = False
				continue
			rowList = rowHabitation.split(",")
			stateSetInHabitation[rowList[1].upper().strip()] = indexInHabitation
			indexInHabitation += 1

		stateSetInHealth = dict([])
		headingRow = True
		for rowHealth in healthCareReducedList:
			if headingRow:
				headingRow = False
				continue
			rowList = rowHealth.split(",")
			stateSetInHealth[rowList[1].upper().strip()] = rowList[2] + "," + rowList[3] + "," + rowList[4] + "," + rowList[5] + "," + rowList[6]

		reducedCSVList = []
		reducedCSVList.append(['State', 'District', 'SC Current', 'ST Current', 'General Current', 'SC Covered', 'ST Covered', 'General Covered', 'Number of Sub Centres', 'Number of Primary Health Centres', 'Number of Community Health Centres', 'Sub Divisional Hospitals', 'District Hospitals'])

		for stateHabitat in stateSetInHabitation:
			if(stateHabitat in stateSetInHealth):
				tempList = habitationReducedList[stateSetInHabitation[stateHabitat]].split(",")
				tempValue = stateSetInHealth[stateHabitat].strip().split(",")
				reducedCSVList.append([tempList[0], tempList[1], tempList[2], tempList[3], tempList[4], tempList[5], tempList[6], tempList[7].strip(), tempValue[0], tempValue[1], tempValue[2], tempValue[3], tempValue[4]])


		with open('../data/healthAndHabitatMerged.csv', 'w') as merged:
			writer = csv.writer(merged)
			writer.writerows(reducedCSVList)
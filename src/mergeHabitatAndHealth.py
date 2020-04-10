import csv

with open('healthCleanReduced.csv', 'r') as healthCareReducedCSV:
	healthCareReducedList = list(healthCareReducedCSV)
	with open('habitation_reduced.csv', 'r') as habitationReduced:
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
		#print (stateSetInHabitation)

		stateSetInHealth = dict([])
		headingRow = True
		for rowHealth in healthCareReducedList:
			if headingRow:
				headingRow = False
				continue
			rowList = rowHealth.split(",")
			stateSetInHealth[rowList[1].upper().strip()] = rowList[2] + "," + rowList[3]

		commonCount = 0
		uncommonCount = 0

		reducedCSVList = []
		reducedCSVList.append(['State', 'District', 'SC Current', 'ST Current', 'General Current', 'SC Covered', 'ST Covered', 'General Covered', 'Lower Health Index', 'Higher Health Index'])

		for stateHabitat in stateSetInHabitation:
			if(stateHabitat in stateSetInHealth):
				tempList = habitationReducedList[stateSetInHabitation[stateHabitat]].split(",")
				tempValue = stateSetInHealth[stateHabitat].strip().split(",")
				reducedCSVList.append([tempList[0], tempList[1], tempList[2], tempList[3], tempList[4], tempList[5], tempList[6], tempList[7].strip(), tempValue[0], tempValue[1]])
		#print(commonCount)
		#print(uncommonCount)
		#print (reducedCSVList)

		with open('healthAndHabitatMerged.csv', 'w') as merged:
			writer = csv.writer(merged)
			writer.writerows(reducedCSVList)
import csv
import re

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

with open('../data/HealthCare.csv', 'r') as healthCareCSV:
    healthCareList = list(healthCareCSV)
    headingRow = True
    reducedCSVList = []
    reducedCSVList.append(['State', 'District', 'Lower Health Index', 'Higher Health Index'])
    for row in healthCareList:
        if headingRow:
            headingRow = False
            continue
        rowList = row.split(",")
        
        noOfSubCentres = intValueOf(rowList[2].strip())
        noOfPrimaryCentres = intValueOf(rowList[3].strip())
        noOfCommunityCentres = intValueOf(rowList[4].strip())
       	noOfSubDivisional = intValueOf(rowList[5].strip())
       	noOfDistrict = intValueOf(rowList[6].strip())

        lowerHealthIndex = noOfSubCentres + (5 * noOfPrimaryCentres) + (25 * noOfCommunityCentres)
        higherHealthIndex = (noOfSubDivisional) + (5 * noOfDistrict)
       	
       	# removing special characters
       	stateClean = re.sub('\W+',' ', rowList[0])
       	districtClean = re.sub('\W+',' ', rowList[1])

       	reducedCSVList.append([stateClean, districtClean, lowerHealthIndex, higherHealthIndex])

    with open('../data/healthCleanReduced.csv', 'w') as healthCleanReduced:
    	writer = csv.writer(healthCleanReduced)
    	writer.writerows(reducedCSVList)
    	
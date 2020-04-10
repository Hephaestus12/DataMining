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

with open('HealthCare.csv', 'r') as healthCareCSV:
    healthCareList = list(healthCareCSV)
    headingRow = True
    reducedCSVList = []
    reducedCSVList.append(['State', 'District', 'Total number of Health Care Centres'])
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
       	totalHealthCareCentres = noOfDistrict + noOfSubDivisional + noOfCommunityCentres + noOfPrimaryCentres + noOfSubCentres
       	# removing special characters
       	stateClean = re.sub('\W+',' ', rowList[0])
       	districtClean = re.sub('\W+',' ', rowList[1])
       	reducedCSVList.append([stateClean, districtClean, totalHealthCareCentres])

    with open('healthCleanReduced.csv', 'w') as healthCleanReduced:
    	writer = csv.writer(healthCleanReduced)
    	writer.writerows(reducedCSVList)



       	
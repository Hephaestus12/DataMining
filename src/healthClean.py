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
    reducedCSVList.append(['State', 'District', 'Number of Sub Centres', 'Number of Primary Health Centres', 'Number of Community Health Centres', 'Sub Divisional Hospitals', 'District Hospitals'])
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
       	
       	# removing special characters
       	stateClean = re.sub('\W+',' ', rowList[0])
       	districtClean = re.sub('\W+',' ', rowList[1])

       	reducedCSVList.append([stateClean, districtClean, noOfSubCentres, noOfPrimaryCentres, noOfCommunityCentres, noOfSubDivisional, noOfDistrict])

    with open('../data/healthCleanReduced.csv', 'w') as healthCleanReduced:
    	writer = csv.writer(healthCleanReduced)
    	writer.writerows(reducedCSVList)
    	
#! python3
#compare data in rows of 2 csv files

import csv, os, sys, re
#Read in the manifest
first = sys.argv[1]
csvFile1 = open(first)
readerFile1 = csv.reader(csvFile1)
file1list = list(readerFile1)
file1 = []

#reg expression to identify Study Id
studyIdRegex = re.compile(r'([/])(\w\w\w\d{3,4})')
os.chdir('/SD5/people/t862537')

#create list of destination variables from manigest
for i in file1list:
    file1.append(i[1])

#read destination variables into text variable        
file1text = ''
for i in file1list:
    file1text += str(i)

#search destination text for clarity Id and assign it
mo = studyIdRegex.search(file1text)
clarityId = mo.group(2)

#create list of files in Clarity Id directory
clarityIdFiles = []
os.chdir('/project/'+ clarityId)
for fileName in os.listdir('.'):
    clarityIdFiles.append('demeter:'+ os.getcwd() +'/' + fileName)

#compare files from manifest to files in clarity ID directory, write failed files to csv file
os.chdir('/SD5/people/t862537') 
csvFile3 = open(os.path.join(os.getcwd(), clarityId + '_failedlog.csv'), 'w')
file3Writer = csv.writer(csvFile3)
file3 = []
file3Writer.writerow(['destination'])
for i in file1:
    if i != 'source' and i !='destination':
        if i not in clarityIdFiles:
            file3Writer.writerow([i])
            file3.append(i)

#compare files from manifest to files in clarity ID directory, write verified files to csv file
csvFile4 = open(os.path.join(os.getcwd(), clarityId + '_verifiedlog.csv'), 'w')
file4Writer = csv.writer(csvFile4)
file4 = []
file4Writer.writerow(['destination'])
for i in file1:
    if i != 'source' and i !='destination':
        if i in clarityIdFiles:
            file4Writer.writerow([i])
            file4.append(i)

#output count of errors
print("There were " + str(len(file3)) + " errors")
csvFile3.close()
csvFile4.close()
csvFile1.close()


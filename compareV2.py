#! python3
#compare data in rows of 2 csv files

import csv, os, sys, re

first = sys.argv[1]
csvFile1 = open(first)
readerFile1 = csv.reader(csvFile1)
file1list = list(readerFile1)
file1 = []
second = sys.argv[2]
csvFile2 = open(second)
readerFile2 = csv.reader(csvFile2)
file2list = list(readerFile2)
file2 = []

os.makedirs('comparisonLogs', exist_ok=True)

for i in range(0, len(file1list)):
    for j in range(1,2):
        file1.append(file1list[i][j])

for i in range(0, len(file2list)):
    for j in range(1):
        file2.append(file2list[i][j])
 
csvFile3 = open(os.path.join('comparisonLogs', 'comparelog.csv'), 'w', newline='')
file3Writer = csv.writer(csvFile3)
file3 = []
for i in file2:
    if i not in file1:
        file3Writer.writerow(i)
        file3.append(i)
print("There were " + str(len(file3)) + " errors")
csvFile3.close()
csvFile1.close()
csvFile2.close()

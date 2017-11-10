#! python3
#compare data in rows of 2 csv files

import csv, os, sys
first = sys.argv[1]
csvFile1 = open(first)
readerFile1 = csv.reader(csvFile1)
file1 = []
second = sys.argv[2]
csvFile2 = open(second)
readerFile2 = csv.reader(csvFile2)
file2 = []

os.makedirs('comparisonLogs', exist_ok=True)

for row in readerFile1:
    for j in range(1,2):
        file1.append(row)

for line in readerFile2:
    for j in range(1,2):
        file2.append(line)
 
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

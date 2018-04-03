#!Python3
'''
fasta file parser
diplay name and read count for each item
sort output by read count total
'''
import sys, argparse, openpyxl, os
from openpyxl.styles import Font, PatternFill, Border, Side
from openpyxl.chart import(
    Reference,
    Series,
    BarChart3D,
    BarChart
)
from Bio import SeqIO
from pprint import pprint

infile = sys.argv[1]

#New blank metadata
meta = openpyxl.Workbook()
meta_sheet = meta.get_sheet_names()
meta_source = meta_sheet[0]
meta_page = meta.get_sheet_by_name(meta_source)

#Headers
meta_page['A1'] = "infile"
meta_page['B1'] = "max"
meta_page['C1'] = "min"
meta_page['D1'] = "outfile"

#Global variables
low_count = {}
low_reads = []
normal_count = {}
normal_reads = []
high_count = {}
high_reads = []
results = {}
steps = []
groups = {}
try:
    low_limit = int(sys.argv[2])
    upper_limit = int(sys.argv[3])
except ValueError:
    print("lower and upper limits must be integers")
    sys.exit(0)

#loop through each read and compare read length to upper and lower limits
records = list(SeqIO.parse(infile, "fasta"))
for i in range(0, len(records)):
    if len(records[i].seq) <= low_limit:
        low_count[records[i].id] = len(records[i].seq)
        ##records[i].id = records[i].id + "_filtered"
        low_reads.append(records[i])
    elif len(records[i].seq) >= upper_limit:
        high_count[records[i].id] = len(records[i].seq)
        ##records[i].id = records[i].id + "_filtered"
        high_reads.append(records[i])
    else:
        normal_count[records[i].id] = len(records[i].seq)
        ##records[i].id = records[i].id + "_filtered"
        normal_reads.append(records[i])
    
#metadata information
meta_page['A2'] = str(infile)
meta_page['B2'] = int(low_limit)
meta_page['C2'] = int(upper_limit)
meta_page['D2'] = "fasta_filtered_" + str(low_limit) + "_" + str(upper_limit)
meta_page.title = "metadata"

#compile dictionary of read lengths by increment
steps.append(0)
for i in range(1,28):
    steps.append(i*100)
for i in range(0, len(steps)):
    groups.append(str(i) + "00")
records = list(SeqIO.parse(infile, "fasta"))
results.setdefault("2800+", {'Total':0})
for j in range(0, len(steps)):
    results.setdefault(str(groups[j] + "-" + (str(j) + "99")), {'Total':0})
    for i in range(0, len(records)):
        if len(records[i].seq) >= steps[j] and len(records[i].seq) <= (steps[j]+99):
            results[groups[j] + "-" + (str(j)+ "99")]['Total'] += int(1)
for i in range(0, len(records)):
    if len(records[i].seq) > 2800:
        results["2800+"]['Total'] += int(1)


#create result sheet in excel metadata workbook
meta.create_sheet(index=1, title="result data")
meta_new_sheet = meta.get_sheet_names()
meta_result_source = meta_new_sheet[1]
meta_result = meta.get_sheet_by_name(meta_result_source)
meta_result['A1'] = "Interval"
meta_result['B1'] = "Read Count"
for i, (key, value) in enumerate(results.items()):
    meta_result['A' + str(i+2)] = key
    meta_result['B' + str(i+2)] = value['Total']

#Generate Chart with read length increment data
data = openpyxl.chart.Reference(meta_result, min_col=2, min_row=1, max_row=(len(steps) +2))
titles = openpyxl.chart.Reference(meta_result, min_col=1, min_row=2, max_row=(len(steps) +2))
chart = BarChart()
chart.style = 11
chart.type = 'bar'
chart.title = "Read Count by Grouping"
chart.add_data(data=data, titles_from_data=True)
chart.set_categories(titles)
meta_result.add_chart(chart, 'D2')

#print results to console
print("Total Read Count:" + str(len(records)))
pprint(results)
pprint("Low reads: " + str(len(low_count)))
##pprint(low_count)
pprint("Normal reads: " + str(len(normal_count)))
##pprint(normal_count)
pprint("High reads: " + str(len(high_count)))
##pprint(high_count)

#save data to ouput files. windows then linux
try:
    meta.save(os.getcwd()+ "\\fasta_filtered_" + str(low_limit) + "_" + str(upper_limit) + "_metadata.xlsx")
    SeqIO.write(normal_reads, os.getcwd() +"\\fasta_filtered_" + str(low_limit) + "_" + str(upper_limit), "fasta")
except PermissionError:
    meta.save(os.getcwd()+ "/fasta_filtered_" + str(low_limit) + "_" + str(upper_limit) + "_metadata.xlsx")
    SeqIO.write(normal_reads, os.getcwd() +"/fasta_filtered_" + str(low_limit) + "_" + str(upper_limit), "fasta")

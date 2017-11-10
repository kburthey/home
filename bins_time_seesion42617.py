Python 3.6.0 (v3.6.0:41df79263a11, Dec 23 2016, 07:18:10) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> from math import pi
>>> from time import sleep
>>> from datetime import datetime
>>> now = datetime.now()
>>> now
datetime.datetime(2017, 4, 26, 11, 34, 17, 400088)
>>> print ("Current time: %s/%s/%s " % now.month, now.day, now.year)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    print ("Current time: %s/%s/%s " % now.month, now.day, now.year)
TypeError: not enough arguments for format string
>>> now.month
4
>>> print ("current time %s" % (now.month))
current time 4
>>> print ("Current time: %s/%s/%s " % (now.month, now.day, now.year))
Current time: 4/26/2017 
>>> 
>>> pi
3.141592653589793
>>> area = pi
>>> print ("area : %.2f" % (area))
area : 3.14
>>> area **2
9.869604401089358
>>> print (math)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    print (math)
NameError: name 'math' is not defined
>>> now
datetime.datetime(2017, 4, 26, 11, 34, 17, 400088)
>>> date
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    date
NameError: name 'date' is not defined
>>> datetime
<class 'datetime.datetime'>
>>> later = datetime.now()
>>> later - now
datetime.timedelta(0, 4596, 896171)
>>> int (later-now)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    int (later-now)
TypeError: int() argument must be a string, a bytes-like object or a number, not 'datetime.timedelta'
>>> int (str(later-now))
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    int (str(later-now))
ValueError: invalid literal for int() with base 10: '1:16:36.896171'
>>> (later-now).total_seconds()
4596.896171
>>> 4596 / 60
76.6
>>> start = datetime.now(day, month)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    start = datetime.now(day, month)
NameError: name 'day' is not defined
>>> start = datetime.now(now.day, now.month)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    start = datetime.now(now.day, now.month)
TypeError: now() takes at most 1 argument (2 given)
>>> start = datetime.now.day()
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    start = datetime.now.day()
AttributeError: 'builtin_function_or_method' object has no attribute 'day'
>>> start = datetime.now.day
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    start = datetime.now.day
AttributeError: 'builtin_function_or_method' object has no attribute 'day'
>>> from datetime import date
>>> date.today()
datetime.date(2017, 4, 26)
>>> datetime.date(2016, 3, 15)
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    datetime.date(2016, 3, 15)
TypeError: descriptor 'date' requires a 'datetime.datetime' object but received a 'int'
>>> datetime.date()
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    datetime.date()
TypeError: descriptor 'date' of 'datetime.datetime' object needs an argument
>>> datetime.date(today)
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    datetime.date(today)
NameError: name 'today' is not defined
>>> date.max
datetime.date(9999, 12, 31)
>>> date.month
<attribute 'month' of 'datetime.date' objects>
>>> date.timetuple()
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    date.timetuple()
TypeError: descriptor 'timetuple' of 'datetime.date' object needs an argument
>>> date.timetuple(2017, 4, 16)
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    date.timetuple(2017, 4, 16)
TypeError: descriptor 'timetuple' requires a 'datetime.date' object but received a 'int'
>>> date.timetuple(d.year)
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    date.timetuple(d.year)
NameError: name 'd' is not defined
>>> date.timetuple(year)
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    date.timetuple(year)
NameError: name 'year' is not defined
>>> d = date.today()
>>> d
datetime.date(2017, 4, 26)
>>> d.replace(day=31)
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    d.replace(day=31)
ValueError: day is out of range for month
>>> d.replace(day=30)
datetime.date(2017, 4, 30)
>>> d
datetime.date(2017, 4, 26)
>>> date.today()
datetime.date(2017, 4, 26)
>>> d - date.today()
datetime.timedelta(0)
>>> d - date.today().total_seconds()
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    d - date.today().total_seconds()
AttributeError: 'datetime.date' object has no attribute 'total_seconds'
>>> (d - date.today()).total_seconds()
0.0
>>> datetime.day()
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    datetime.day()
TypeError: 'getset_descriptor' object is not callable
>>> datetime.day
<attribute 'day' of 'datetime.date' objects>
>>> day = datetime.day
>>> day
<attribute 'day' of 'datetime.date' objects>
>>> d
datetime.date(2017, 4, 26)
>>> e = d.replace(day=30)
>>> d - date.today()
datetime.timedelta(0)
>>> d - e
datetime.timedelta(-4)
>>> c = int (d-e)
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    c = int (d-e)
TypeError: int() argument must be a string, a bytes-like object or a number, not 'datetime.timedelta'
>>> c = str(d-e)
>>> c
'-4 days, 0:00:00'
>>> c = str((d-e) /1)
>>> c
'-4 days, 0:00:00'
>>> c = str(abs(d-e))
>>> c
'4 days, 0:00:00'
>>> print( c + " until complete")
4 days, 0:00:00 until complete
>>> e - date.today()
datetime.timedelta(4)
>>> e - d
datetime.timedelta(4)
>>> c = str ( e-d)
>>> c
'4 days, 0:00:00'
>>> print( c + " until complete")
4 days, 0:00:00 until complete
>>> c.split()
['4', 'days,', '0:00:00']
>>> f = c.split()
>>> f[0]
'4'
>>> 35/26
1.3461538461538463
>>> 25/26
0.9615384615384616
>>> 20/25
0.8
>>> d
datetime.date(2017, 4, 26)
>>> d.replace(day=30, month=5)
datetime.date(2017, 5, 30)
>>> 
========== RESTART: C:/Users/t862537/Python/Python36-32/datetime.py ==========
Traceback (most recent call last):
  File "C:/Users/t862537/Python/Python36-32/datetime.py", line 3, in <module>
    from datetime import datetime, date
  File "C:/Users/t862537/Python/Python36-32\datetime.py", line 3, in <module>
    from datetime import datetime, date
ImportError: cannot import name 'datetime'
>>> 
========== RESTART: C:/Users/t862537/Python/Python36-32/datetime.py ==========
Traceback (most recent call last):
  File "C:/Users/t862537/Python/Python36-32/datetime.py", line 3, in <module>
    from datetime import datetime
  File "C:/Users/t862537/Python/Python36-32\datetime.py", line 3, in <module>
    from datetime import datetime
ImportError: cannot import name 'datetime'
>>> from datetime import datetime
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    from datetime import datetime
  File "C:/Users/t862537/Python/Python36-32\datetime.py", line 3, in <module>
    from datetime import datetime
ImportError: cannot import name 'datetime'
>>> from datetime import datetime
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    from datetime import datetime
  File "C:/Users/t862537/Python/Python36-32\datetime.py", line 3, in <module>
    from datetime import datetime
ImportError: cannot import name 'datetime'
>>> 
========== RESTART: C:/Users/t862537/Python/Python36-32/testdate.py ==========
Traceback (most recent call last):
  File "C:/Users/t862537/Python/Python36-32/testdate.py", line 3, in <module>
    from datetime import datetime
  File "C:/Users/t862537/Python/Python36-32\datetime.py", line 3, in <module>
    from datetime import datetime
ImportError: cannot import name 'datetime'
>>> from time import sleep
>>> from datetime import datetime
Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    from datetime import datetime
  File "C:/Users/t862537/Python/Python36-32\datetime.py", line 3, in <module>
    from datetime import datetime
ImportError: cannot import name 'datetime'
>>> 
=============================== RESTART: Shell ===============================
>>> from datetime import datetime
Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    from datetime import datetime
  File "C:\Users\t862537\Python\Python36-32\datetime.py", line 3, in <module>
    from datetime import datetime
ImportError: cannot import name 'datetime'
>>> 
========== RESTART: C:/Users/t862537/Python/Python36-32/testdate.py ==========
-34 days, 0:00:00
>>> 
========== RESTART: C:/Users/t862537/Python/Python36-32/testdate.py ==========
34 days, 0:00:00
>>> 
========== RESTART: C:/Users/t862537/Python/Python36-32/testdate.py ==========
34 days, 0:00:00
Traceback (most recent call last):
  File "C:/Users/t862537/Python/Python36-32/testdate.py", line 11, in <module>
    d = c.split()
AttributeError: 'datetime.timedelta' object has no attribute 'split'
>>> 
========== RESTART: C:/Users/t862537/Python/Python36-32/testdate.py ==========
34 days, 0:00:00
['34', 'days,']
>>> 
========== RESTART: C:/Users/t862537/Python/Python36-32/testdate.py ==========
34 days, 0:00:00
Traceback (most recent call last):
  File "C:/Users/t862537/Python/Python36-32/testdate.py", line 12, in <module>
    print (d[:2].join())
AttributeError: 'list' object has no attribute 'join'
>>> 
========== RESTART: C:/Users/t862537/Python/Python36-32/testdate.py ==========
34 days, 0:00:00
Traceback (most recent call last):
  File "C:/Users/t862537/Python/Python36-32/testdate.py", line 12, in <module>
    print ((d[:2]).join())
AttributeError: 'list' object has no attribute 'join'
>>> 
========== RESTART: C:/Users/t862537/Python/Python36-32/testdate.py ==========
34 days, 0:00:00
34days,
>>> 
========== RESTART: C:/Users/t862537/Python/Python36-32/testdate.py ==========
34 days, 0:00:00
34 days
>>> from datetime import date
>>> date.today()
datetime.date(2017, 4, 26)
>>> a = datetime.date()
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    a = datetime.date()
TypeError: descriptor 'date' of 'datetime.datetime' object needs an argument
>>> a = date.today()
>>> a - 30
Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    a - 30
TypeError: unsupported operand type(s) for -: 'datetime.date' and 'int'
>>> int (a)
Traceback (most recent call last):
  File "<pyshell#90>", line 1, in <module>
    int (a)
TypeError: int() argument must be a string, a bytes-like object or a number, not 'datetime.date'
>>> z = 01-12-2017
SyntaxError: invalid token
>>> z = "01-12-2017"
>>> z.split(-)
SyntaxError: invalid syntax
>>> z.split()
['01-12-2017']
>>> z.split('-'_
	
SyntaxError: invalid syntax
>>> z.split('-')
['01', '12', '2017']
>>> import openpyxl
>>> import os
>>> import sys
>>> bins = sys.argv[1]
Traceback (most recent call last):
  File "<pyshell#100>", line 1, in <module>
    bins = sys.argv[1]
IndexError: list index out of range
>>> wb = openpyxl.load_workbook('BiNSReport(6).xlsx')
Traceback (most recent call last):
  File "<pyshell#101>", line 1, in <module>
    wb = openpyxl.load_workbook('BiNSReport(6).xlsx')
  File "C:\Users\t862537\Python\Python36-32\lib\site-packages\openpyxl\reader\excel.py", line 164, in load_workbook
    archive = _validate_archive(filename)
  File "C:\Users\t862537\Python\Python36-32\lib\site-packages\openpyxl\reader\excel.py", line 118, in _validate_archive
    archive = ZipFile(filename, 'r', ZIP_DEFLATED)
  File "C:\Users\t862537\Python\Python36-32\lib\zipfile.py", line 1082, in __init__
    self.fp = io.open(file, filemode)
FileNotFoundError: [Errno 2] No such file or directory: 'BiNSReport(6).xlsx'
>>> wb = openpyxl.load_workbook('BiNSReport(6).xlsx')
Traceback (most recent call last):
  File "<pyshell#102>", line 1, in <module>
    wb = openpyxl.load_workbook('BiNSReport(6).xlsx')
  File "C:\Users\t862537\Python\Python36-32\lib\site-packages\openpyxl\reader\excel.py", line 164, in load_workbook
    archive = _validate_archive(filename)
  File "C:\Users\t862537\Python\Python36-32\lib\site-packages\openpyxl\reader\excel.py", line 118, in _validate_archive
    archive = ZipFile(filename, 'r', ZIP_DEFLATED)
  File "C:\Users\t862537\Python\Python36-32\lib\zipfile.py", line 1082, in __init__
    self.fp = io.open(file, filemode)
FileNotFoundError: [Errno 2] No such file or directory: 'BiNSReport(6).xlsx'
>>> wb = openpyxl.load_workbook('BiNSReport(6).xlsx')
>>> sheet = wb.active
>>> for row in range(2, sheet.max_row +1):
	print (str(sheet.cell(row=row, column=9).value))

	
04-30-2016
07-01-2016
05-09-2016
01-31-2017
02-28-2017
11-30-2016
01-31-2017
10-31-2016
07-03-2017
04-05-2017
03-31-2017
03-31-2017
08-01-2016
06-21-2016
04-28-2017
04-17-2017
03-15-2017
03-15-2017
02-28-2017
02-21-2017
04-05-2017
04-05-2017
03-31-2017
04-05-2017
04-12-2017
03-31-2017
03-29-2017
12-31-2017
08-31-2016
06-30-2016
07-04-2016
07-04-2016
12-01-2016
03-31-2017
08-25-2016
06-30-2017
06-30-2017
12-01-2017
06-30-2017
01-31-2017
06-30-2017
06-30-2017
02-18-2016
03-31-2016
05-31-2016
05-31-2016
08-21-2016
08-21-2016
04-19-2017
06-01-2017
06-12-2016
06-01-2016
05-31-2017
03-31-2017
05-31-2016
05-31-2017
03-31-2017
03-31-2017
04-30-2017
06-30-2017
12-31-2014
12-31-2017
12-31-2017
05-31-2016
09-12-2016
12-31-2017
12-31-2014
09-01-2015
12-31-2017
06-30-2017
09-30-2015
06-30-2017
12-31-2015
06-30-2017
06-01-2016
01-15-2016
09-30-2015
03-31-2016
02-29-2016
07-26-2016
08-01-2016
01-18-2016
01-18-2016
01-18-2016
03-10-2016
03-31-2016
12-31-2016
06-02-2016
06-02-2016
06-02-2016
04-15-2016
05-01-2016
05-09-2016
05-09-2016
07-01-2016
06-01-2016
05-23-2016
06-30-2017
12-01-2017
10-02-2017
05-01-2017
>>> for row in range(2, sheet.max_row +1):
	print (str(sheet.cell(row=row, column=1).value) + str(sheet.cell(row=row, column=9).value))

	
BRI205104-30-2016
BHA225707-01-2016
BHA175205-09-2016
KRA225801-31-2017
DAN241002-28-2017
SUN235611-30-2016
SUN240801-31-2017
LOK225710-31-2016
LIU255807-03-2017
LIU256204-05-2017
BRI255503-31-2017
BRI255603-31-2017
DAN230508-01-2016
PIN212306-21-2016
WAT260104-28-2017
CAD265104-17-2017
KAD226203-15-2017
KAD226303-15-2017
LEE270502-28-2017
CLA270102-21-2017
DIE270304-05-2017
BUR270404-05-2017
BUR270603-31-2017
BUR270704-05-2017
LOK255704-12-2017
BUR270803-31-2017
KAV270903-29-2017
email url testing12-31-2017
KRA240208-31-2016
KRA240906-30-2016
WID245107-04-2016
WID245307-04-2016
SHE241112-01-2016
DAN245203-31-2017
RIC245508-25-2016
GED245806-30-2017
GED245906-30-2017
LIU246012-01-2017
MAG250106-30-2017
DAN255101-31-2017
BUR255206-30-2017
BHA255406-30-2017
SUN226002-18-2016
BUR221403-31-2016
BUR235405-31-2016
WID226105-31-2016
KUM226508-21-2016
KUM230908-21-2016
DIE256104-19-2017
LIU255906-01-2017
COH240306-12-2016
COH240406-01-2016
LOK286505-31-2017
KRA280103-31-2017
RIC230605-31-2016
SUN240705-31-2017
DIE285603-31-2017
SHE271203-31-2017
DIE285404-30-2017
KAV286306-30-2017
LIU71012-31-2014
KRA100312-31-2017
BUR96412-31-2017
BUR98405-31-2016
KAV133209-12-2016
DAC160212-31-2017
LIU65412-31-2014
BTY185209-01-2015
BTY65912-31-2017
DAN195506-30-2017
DAC195309-30-2015
BUR220306-30-2017
BUR215512-31-2015
KRA175406-30-2017
NIC221006-01-2016
KWA221101-15-2016
KRA210509-30-2015
BUR221403-31-2016
BHA215202-29-2016
DIE175307-26-2016
DAN225508-01-2016
LIU211001-18-2016
LIU211901-18-2016
LIU212101-18-2016
DIE220103-10-2016
BON225603-31-2016
BUR230212-31-2016
KUM225206-02-2016
KUM225306-02-2016
KUM225406-02-2016
BHA215304-15-2016
BRI210105-01-2016
BHA230705-09-2016
DON230805-09-2016
DIE175507-01-2016
BUR226406-01-2016
BHA240105-23-2016
LIU235506-30-2017
LIU285312-01-2017
LIU286610-02-2017
DIE286705-01-2017
>>> for row in range(2, sheet.max_row +1):
	print (str(sheet.cell(row=row, column=1).value) + " " + str(sheet.cell(row=row, column=9).value))

	
BRI2051 04-30-2016
BHA2257 07-01-2016
BHA1752 05-09-2016
KRA2258 01-31-2017
DAN2410 02-28-2017
SUN2356 11-30-2016
SUN2408 01-31-2017
LOK2257 10-31-2016
LIU2558 07-03-2017
LIU2562 04-05-2017
BRI2555 03-31-2017
BRI2556 03-31-2017
DAN2305 08-01-2016
PIN2123 06-21-2016
WAT2601 04-28-2017
CAD2651 04-17-2017
KAD2262 03-15-2017
KAD2263 03-15-2017
LEE2705 02-28-2017
CLA2701 02-21-2017
DIE2703 04-05-2017
BUR2704 04-05-2017
BUR2706 03-31-2017
BUR2707 04-05-2017
LOK2557 04-12-2017
BUR2708 03-31-2017
KAV2709 03-29-2017
email url testing 12-31-2017
KRA2402 08-31-2016
KRA2409 06-30-2016
WID2451 07-04-2016
WID2453 07-04-2016
SHE2411 12-01-2016
DAN2452 03-31-2017
RIC2455 08-25-2016
GED2458 06-30-2017
GED2459 06-30-2017
LIU2460 12-01-2017
MAG2501 06-30-2017
DAN2551 01-31-2017
BUR2552 06-30-2017
BHA2554 06-30-2017
SUN2260 02-18-2016
BUR2214 03-31-2016
BUR2354 05-31-2016
WID2261 05-31-2016
KUM2265 08-21-2016
KUM2309 08-21-2016
DIE2561 04-19-2017
LIU2559 06-01-2017
COH2403 06-12-2016
COH2404 06-01-2016
LOK2865 05-31-2017
KRA2801 03-31-2017
RIC2306 05-31-2016
SUN2407 05-31-2017
DIE2856 03-31-2017
SHE2712 03-31-2017
DIE2854 04-30-2017
KAV2863 06-30-2017
LIU710 12-31-2014
KRA1003 12-31-2017
BUR964 12-31-2017
BUR984 05-31-2016
KAV1332 09-12-2016
DAC1602 12-31-2017
LIU654 12-31-2014
BTY1852 09-01-2015
BTY659 12-31-2017
DAN1955 06-30-2017
DAC1953 09-30-2015
BUR2203 06-30-2017
BUR2155 12-31-2015
KRA1754 06-30-2017
NIC2210 06-01-2016
KWA2211 01-15-2016
KRA2105 09-30-2015
BUR2214 03-31-2016
BHA2152 02-29-2016
DIE1753 07-26-2016
DAN2255 08-01-2016
LIU2110 01-18-2016
LIU2119 01-18-2016
LIU2121 01-18-2016
DIE2201 03-10-2016
BON2256 03-31-2016
BUR2302 12-31-2016
KUM2252 06-02-2016
KUM2253 06-02-2016
KUM2254 06-02-2016
BHA2153 04-15-2016
BRI2101 05-01-2016
BHA2307 05-09-2016
DON2308 05-09-2016
DIE1755 07-01-2016
BUR2264 06-01-2016
BHA2401 05-23-2016
LIU2355 06-30-2017
LIU2853 12-01-2017
LIU2866 10-02-2017
DIE2867 05-01-2017
>>> for row in range(1, sheet.max_row +1):
	print (str(sheet.cell(row=row, column=1).value) + " " + str(sheet.cell(row=row, column=9).value))

	
Study Name  Target Result Delivery Date 
BRI2051 04-30-2016
BHA2257 07-01-2016
BHA1752 05-09-2016
KRA2258 01-31-2017
DAN2410 02-28-2017
SUN2356 11-30-2016
SUN2408 01-31-2017
LOK2257 10-31-2016
LIU2558 07-03-2017
LIU2562 04-05-2017
BRI2555 03-31-2017
BRI2556 03-31-2017
DAN2305 08-01-2016
PIN2123 06-21-2016
WAT2601 04-28-2017
CAD2651 04-17-2017
KAD2262 03-15-2017
KAD2263 03-15-2017
LEE2705 02-28-2017
CLA2701 02-21-2017
DIE2703 04-05-2017
BUR2704 04-05-2017
BUR2706 03-31-2017
BUR2707 04-05-2017
LOK2557 04-12-2017
BUR2708 03-31-2017
KAV2709 03-29-2017
email url testing 12-31-2017
KRA2402 08-31-2016
KRA2409 06-30-2016
WID2451 07-04-2016
WID2453 07-04-2016
SHE2411 12-01-2016
DAN2452 03-31-2017
RIC2455 08-25-2016
GED2458 06-30-2017
GED2459 06-30-2017
LIU2460 12-01-2017
MAG2501 06-30-2017
DAN2551 01-31-2017
BUR2552 06-30-2017
BHA2554 06-30-2017
SUN2260 02-18-2016
BUR2214 03-31-2016
BUR2354 05-31-2016
WID2261 05-31-2016
KUM2265 08-21-2016
KUM2309 08-21-2016
DIE2561 04-19-2017
LIU2559 06-01-2017
COH2403 06-12-2016
COH2404 06-01-2016
LOK2865 05-31-2017
KRA2801 03-31-2017
RIC2306 05-31-2016
SUN2407 05-31-2017
DIE2856 03-31-2017
SHE2712 03-31-2017
DIE2854 04-30-2017
KAV2863 06-30-2017
LIU710 12-31-2014
KRA1003 12-31-2017
BUR964 12-31-2017
BUR984 05-31-2016
KAV1332 09-12-2016
DAC1602 12-31-2017
LIU654 12-31-2014
BTY1852 09-01-2015
BTY659 12-31-2017
DAN1955 06-30-2017
DAC1953 09-30-2015
BUR2203 06-30-2017
BUR2155 12-31-2015
KRA1754 06-30-2017
NIC2210 06-01-2016
KWA2211 01-15-2016
KRA2105 09-30-2015
BUR2214 03-31-2016
BHA2152 02-29-2016
DIE1753 07-26-2016
DAN2255 08-01-2016
LIU2110 01-18-2016
LIU2119 01-18-2016
LIU2121 01-18-2016
DIE2201 03-10-2016
BON2256 03-31-2016
BUR2302 12-31-2016
KUM2252 06-02-2016
KUM2253 06-02-2016
KUM2254 06-02-2016
BHA2153 04-15-2016
BRI2101 05-01-2016
BHA2307 05-09-2016
DON2308 05-09-2016
DIE1755 07-01-2016
BUR2264 06-01-2016
BHA2401 05-23-2016
LIU2355 06-30-2017
LIU2853 12-01-2017
LIU2866 10-02-2017
DIE2867 05-01-2017
>>> data = []
>>> for row in range(1, sheet.max_row +1):
	print (data.append(str(sheet.cell(row=row, column=9).value)))

	
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
>>> data
['Target Result Delivery Date ', '04-30-2016', '07-01-2016', '05-09-2016', '01-31-2017', '02-28-2017', '11-30-2016', '01-31-2017', '10-31-2016', '07-03-2017', '04-05-2017', '03-31-2017', '03-31-2017', '08-01-2016', '06-21-2016', '04-28-2017', '04-17-2017', '03-15-2017', '03-15-2017', '02-28-2017', '02-21-2017', '04-05-2017', '04-05-2017', '03-31-2017', '04-05-2017', '04-12-2017', '03-31-2017', '03-29-2017', '12-31-2017', '08-31-2016', '06-30-2016', '07-04-2016', '07-04-2016', '12-01-2016', '03-31-2017', '08-25-2016', '06-30-2017', '06-30-2017', '12-01-2017', '06-30-2017', '01-31-2017', '06-30-2017', '06-30-2017', '02-18-2016', '03-31-2016', '05-31-2016', '05-31-2016', '08-21-2016', '08-21-2016', '04-19-2017', '06-01-2017', '06-12-2016', '06-01-2016', '05-31-2017', '03-31-2017', '05-31-2016', '05-31-2017', '03-31-2017', '03-31-2017', '04-30-2017', '06-30-2017', '12-31-2014', '12-31-2017', '12-31-2017', '05-31-2016', '09-12-2016', '12-31-2017', '12-31-2014', '09-01-2015', '12-31-2017', '06-30-2017', '09-30-2015', '06-30-2017', '12-31-2015', '06-30-2017', '06-01-2016', '01-15-2016', '09-30-2015', '03-31-2016', '02-29-2016', '07-26-2016', '08-01-2016', '01-18-2016', '01-18-2016', '01-18-2016', '03-10-2016', '03-31-2016', '12-31-2016', '06-02-2016', '06-02-2016', '06-02-2016', '04-15-2016', '05-01-2016', '05-09-2016', '05-09-2016', '07-01-2016', '06-01-2016', '05-23-2016', '06-30-2017', '12-01-2017', '10-02-2017', '05-01-2017']
>>> data = []
>>> for row in range(2, sheet.max_row +1):
	data.append(str(sheet.cell(row=row, column=9).value)))
	
SyntaxError: invalid syntax
>>> for row in range(2, sheet.max_row +1):
	data.append(str(sheet.cell(row=row, column=9).value))

	
>>> data
['04-30-2016', '07-01-2016', '05-09-2016', '01-31-2017', '02-28-2017', '11-30-2016', '01-31-2017', '10-31-2016', '07-03-2017', '04-05-2017', '03-31-2017', '03-31-2017', '08-01-2016', '06-21-2016', '04-28-2017', '04-17-2017', '03-15-2017', '03-15-2017', '02-28-2017', '02-21-2017', '04-05-2017', '04-05-2017', '03-31-2017', '04-05-2017', '04-12-2017', '03-31-2017', '03-29-2017', '12-31-2017', '08-31-2016', '06-30-2016', '07-04-2016', '07-04-2016', '12-01-2016', '03-31-2017', '08-25-2016', '06-30-2017', '06-30-2017', '12-01-2017', '06-30-2017', '01-31-2017', '06-30-2017', '06-30-2017', '02-18-2016', '03-31-2016', '05-31-2016', '05-31-2016', '08-21-2016', '08-21-2016', '04-19-2017', '06-01-2017', '06-12-2016', '06-01-2016', '05-31-2017', '03-31-2017', '05-31-2016', '05-31-2017', '03-31-2017', '03-31-2017', '04-30-2017', '06-30-2017', '12-31-2014', '12-31-2017', '12-31-2017', '05-31-2016', '09-12-2016', '12-31-2017', '12-31-2014', '09-01-2015', '12-31-2017', '06-30-2017', '09-30-2015', '06-30-2017', '12-31-2015', '06-30-2017', '06-01-2016', '01-15-2016', '09-30-2015', '03-31-2016', '02-29-2016', '07-26-2016', '08-01-2016', '01-18-2016', '01-18-2016', '01-18-2016', '03-10-2016', '03-31-2016', '12-31-2016', '06-02-2016', '06-02-2016', '06-02-2016', '04-15-2016', '05-01-2016', '05-09-2016', '05-09-2016', '07-01-2016', '06-01-2016', '05-23-2016', '06-30-2017', '12-01-2017', '10-02-2017', '05-01-2017']
>>> data.split('-')
Traceback (most recent call last):
  File "<pyshell#126>", line 1, in <module>
    data.split('-')
AttributeError: 'list' object has no attribute 'split'
>>> for row in range(2, sheet.max_row +1):
	z = ""
	z +=(str(sheet.cell(row=row, column=9).value))
	print(z.split('-'))

	
['04', '30', '2016']
['07', '01', '2016']
['05', '09', '2016']
['01', '31', '2017']
['02', '28', '2017']
['11', '30', '2016']
['01', '31', '2017']
['10', '31', '2016']
['07', '03', '2017']
['04', '05', '2017']
['03', '31', '2017']
['03', '31', '2017']
['08', '01', '2016']
['06', '21', '2016']
['04', '28', '2017']
['04', '17', '2017']
['03', '15', '2017']
['03', '15', '2017']
['02', '28', '2017']
['02', '21', '2017']
['04', '05', '2017']
['04', '05', '2017']
['03', '31', '2017']
['04', '05', '2017']
['04', '12', '2017']
['03', '31', '2017']
['03', '29', '2017']
['12', '31', '2017']
['08', '31', '2016']
['06', '30', '2016']
['07', '04', '2016']
['07', '04', '2016']
['12', '01', '2016']
['03', '31', '2017']
['08', '25', '2016']
['06', '30', '2017']
['06', '30', '2017']
['12', '01', '2017']
['06', '30', '2017']
['01', '31', '2017']
['06', '30', '2017']
['06', '30', '2017']
['02', '18', '2016']
['03', '31', '2016']
['05', '31', '2016']
['05', '31', '2016']
['08', '21', '2016']
['08', '21', '2016']
['04', '19', '2017']
['06', '01', '2017']
['06', '12', '2016']
['06', '01', '2016']
['05', '31', '2017']
['03', '31', '2017']
['05', '31', '2016']
['05', '31', '2017']
['03', '31', '2017']
['03', '31', '2017']
['04', '30', '2017']
['06', '30', '2017']
['12', '31', '2014']
['12', '31', '2017']
['12', '31', '2017']
['05', '31', '2016']
['09', '12', '2016']
['12', '31', '2017']
['12', '31', '2014']
['09', '01', '2015']
['12', '31', '2017']
['06', '30', '2017']
['09', '30', '2015']
['06', '30', '2017']
['12', '31', '2015']
['06', '30', '2017']
['06', '01', '2016']
['01', '15', '2016']
['09', '30', '2015']
['03', '31', '2016']
['02', '29', '2016']
['07', '26', '2016']
['08', '01', '2016']
['01', '18', '2016']
['01', '18', '2016']
['01', '18', '2016']
['03', '10', '2016']
['03', '31', '2016']
['12', '31', '2016']
['06', '02', '2016']
['06', '02', '2016']
['06', '02', '2016']
['04', '15', '2016']
['05', '01', '2016']
['05', '09', '2016']
['05', '09', '2016']
['07', '01', '2016']
['06', '01', '2016']
['05', '23', '2016']
['06', '30', '2017']
['12', '01', '2017']
['10', '02', '2017']
['05', '01', '2017']
>>> for row in range(2, sheet.max_row +1):
	z = ""
	z +=(str(sheet.cell(row=row, column=9).value))
	h=(z.split('-'))
	a = date.today()
	b = a.replace(day=h[1], month=h[0])
	print (b-a)

	
Traceback (most recent call last):
  File "<pyshell#134>", line 6, in <module>
    b = a.replace(day=h[1], month=h[0])
TypeError: an integer is required (got type str)
>>> for row in range(2, sheet.max_row +1):
	z = ""
	z +=(str(sheet.cell(row=row, column=9).value))
	h=(z.split('-'))
	a = date.today()
	b = a.replace(day=int(h[1]), month=int(h[0]))
	print (b-a)

	
4 days, 0:00:00
66 days, 0:00:00
13 days, 0:00:00
-85 days, 0:00:00
-57 days, 0:00:00
218 days, 0:00:00
-85 days, 0:00:00
188 days, 0:00:00
68 days, 0:00:00
-21 days, 0:00:00
-26 days, 0:00:00
-26 days, 0:00:00
97 days, 0:00:00
56 days, 0:00:00
2 days, 0:00:00
-9 days, 0:00:00
-42 days, 0:00:00
-42 days, 0:00:00
-57 days, 0:00:00
-64 days, 0:00:00
-21 days, 0:00:00
-21 days, 0:00:00
-26 days, 0:00:00
-21 days, 0:00:00
-14 days, 0:00:00
-26 days, 0:00:00
-28 days, 0:00:00
249 days, 0:00:00
127 days, 0:00:00
65 days, 0:00:00
69 days, 0:00:00
69 days, 0:00:00
219 days, 0:00:00
-26 days, 0:00:00
121 days, 0:00:00
65 days, 0:00:00
65 days, 0:00:00
219 days, 0:00:00
65 days, 0:00:00
-85 days, 0:00:00
65 days, 0:00:00
65 days, 0:00:00
-67 days, 0:00:00
-26 days, 0:00:00
35 days, 0:00:00
35 days, 0:00:00
117 days, 0:00:00
117 days, 0:00:00
-7 days, 0:00:00
36 days, 0:00:00
47 days, 0:00:00
36 days, 0:00:00
35 days, 0:00:00
-26 days, 0:00:00
35 days, 0:00:00
35 days, 0:00:00
-26 days, 0:00:00
-26 days, 0:00:00
4 days, 0:00:00
65 days, 0:00:00
249 days, 0:00:00
249 days, 0:00:00
249 days, 0:00:00
35 days, 0:00:00
139 days, 0:00:00
249 days, 0:00:00
249 days, 0:00:00
128 days, 0:00:00
249 days, 0:00:00
65 days, 0:00:00
157 days, 0:00:00
65 days, 0:00:00
249 days, 0:00:00
65 days, 0:00:00
36 days, 0:00:00
-101 days, 0:00:00
157 days, 0:00:00
-26 days, 0:00:00
Traceback (most recent call last):
  File "<pyshell#136>", line 6, in <module>
    b = a.replace(day=int(h[1]), month=int(h[0]))
ValueError: day is out of range for month
>>> for row in range(2, sheet.max_row +1):
	z = ""
	z +=(str(sheet.cell(row=row, column=9).value))
	h=(z.split('-'))
	a = date.today()
	b = a.replace(day=int(h[1]), month=int(h[0]))
	print (b-a + ' ' +str(sheet.cell(row=row, coulumn=9).value))

	
Traceback (most recent call last):
  File "<pyshell#138>", line 7, in <module>
    print (b-a + ' ' +str(sheet.cell(row=row, coulumn=9).value))
TypeError: unsupported operand type(s) for +: 'datetime.timedelta' and 'str'
>>> for row in range(2, sheet.max_row +1):
	z = ""
	z +=(str(sheet.cell(row=row, column=9).value))
	h=(z.split('-'))
	a = date.today()
	b = a.replace(day=int(h[1]), month=int(h[0]))
	print (str(b-a )+ ' ' +str(sheet.cell(row=row, coulumn=9).value))

	
Traceback (most recent call last):
  File "<pyshell#140>", line 7, in <module>
    print (str(b-a )+ ' ' +str(sheet.cell(row=row, coulumn=9).value))
TypeError: cell() got an unexpected keyword argument 'coulumn'
>>> for row in range(2, sheet.max_row +1):
	z = ""
	z +=(str(sheet.cell(row=row, column=9).value))
	h=(z.split('-'))
	a = date.today()
	b = a.replace(day=int(h[1]), month=int(h[0]))
	print (str(b-a )+ ' ' +str(sheet.cell(row=row, column=9).value))

	
4 days, 0:00:00 04-30-2016
66 days, 0:00:00 07-01-2016
13 days, 0:00:00 05-09-2016
-85 days, 0:00:00 01-31-2017
-57 days, 0:00:00 02-28-2017
218 days, 0:00:00 11-30-2016
-85 days, 0:00:00 01-31-2017
188 days, 0:00:00 10-31-2016
68 days, 0:00:00 07-03-2017
-21 days, 0:00:00 04-05-2017
-26 days, 0:00:00 03-31-2017
-26 days, 0:00:00 03-31-2017
97 days, 0:00:00 08-01-2016
56 days, 0:00:00 06-21-2016
2 days, 0:00:00 04-28-2017
-9 days, 0:00:00 04-17-2017
-42 days, 0:00:00 03-15-2017
-42 days, 0:00:00 03-15-2017
-57 days, 0:00:00 02-28-2017
-64 days, 0:00:00 02-21-2017
-21 days, 0:00:00 04-05-2017
-21 days, 0:00:00 04-05-2017
-26 days, 0:00:00 03-31-2017
-21 days, 0:00:00 04-05-2017
-14 days, 0:00:00 04-12-2017
-26 days, 0:00:00 03-31-2017
-28 days, 0:00:00 03-29-2017
249 days, 0:00:00 12-31-2017
127 days, 0:00:00 08-31-2016
65 days, 0:00:00 06-30-2016
69 days, 0:00:00 07-04-2016
69 days, 0:00:00 07-04-2016
219 days, 0:00:00 12-01-2016
-26 days, 0:00:00 03-31-2017
121 days, 0:00:00 08-25-2016
65 days, 0:00:00 06-30-2017
65 days, 0:00:00 06-30-2017
219 days, 0:00:00 12-01-2017
65 days, 0:00:00 06-30-2017
-85 days, 0:00:00 01-31-2017
65 days, 0:00:00 06-30-2017
65 days, 0:00:00 06-30-2017
-67 days, 0:00:00 02-18-2016
-26 days, 0:00:00 03-31-2016
35 days, 0:00:00 05-31-2016
35 days, 0:00:00 05-31-2016
117 days, 0:00:00 08-21-2016
117 days, 0:00:00 08-21-2016
-7 days, 0:00:00 04-19-2017
36 days, 0:00:00 06-01-2017
47 days, 0:00:00 06-12-2016
36 days, 0:00:00 06-01-2016
35 days, 0:00:00 05-31-2017
-26 days, 0:00:00 03-31-2017
35 days, 0:00:00 05-31-2016
35 days, 0:00:00 05-31-2017
-26 days, 0:00:00 03-31-2017
-26 days, 0:00:00 03-31-2017
4 days, 0:00:00 04-30-2017
65 days, 0:00:00 06-30-2017
249 days, 0:00:00 12-31-2014
249 days, 0:00:00 12-31-2017
249 days, 0:00:00 12-31-2017
35 days, 0:00:00 05-31-2016
139 days, 0:00:00 09-12-2016
249 days, 0:00:00 12-31-2017
249 days, 0:00:00 12-31-2014
128 days, 0:00:00 09-01-2015
249 days, 0:00:00 12-31-2017
65 days, 0:00:00 06-30-2017
157 days, 0:00:00 09-30-2015
65 days, 0:00:00 06-30-2017
249 days, 0:00:00 12-31-2015
65 days, 0:00:00 06-30-2017
36 days, 0:00:00 06-01-2016
-101 days, 0:00:00 01-15-2016
157 days, 0:00:00 09-30-2015
-26 days, 0:00:00 03-31-2016
Traceback (most recent call last):
  File "<pyshell#142>", line 6, in <module>
    b = a.replace(day=int(h[1]), month=int(h[0]))
ValueError: day is out of range for month
>>> for row in range(2, sheet.max_row +1):
	z = ""
	z +=(str(sheet.cell(row=row, column=9).value))
	h=(z.split('-'))
	a = date.today()
	b = a.replace(day=int(h[1]), month=int(h[0]), year=int(h[2]))
	print (str(b-a )+ ' ' +str(sheet.cell(row=row, column=9).value))

	
-361 days, 0:00:00 04-30-2016
-299 days, 0:00:00 07-01-2016
-352 days, 0:00:00 05-09-2016
-85 days, 0:00:00 01-31-2017
-57 days, 0:00:00 02-28-2017
-147 days, 0:00:00 11-30-2016
-85 days, 0:00:00 01-31-2017
-177 days, 0:00:00 10-31-2016
68 days, 0:00:00 07-03-2017
-21 days, 0:00:00 04-05-2017
-26 days, 0:00:00 03-31-2017
-26 days, 0:00:00 03-31-2017
-268 days, 0:00:00 08-01-2016
-309 days, 0:00:00 06-21-2016
2 days, 0:00:00 04-28-2017
-9 days, 0:00:00 04-17-2017
-42 days, 0:00:00 03-15-2017
-42 days, 0:00:00 03-15-2017
-57 days, 0:00:00 02-28-2017
-64 days, 0:00:00 02-21-2017
-21 days, 0:00:00 04-05-2017
-21 days, 0:00:00 04-05-2017
-26 days, 0:00:00 03-31-2017
-21 days, 0:00:00 04-05-2017
-14 days, 0:00:00 04-12-2017
-26 days, 0:00:00 03-31-2017
-28 days, 0:00:00 03-29-2017
249 days, 0:00:00 12-31-2017
-238 days, 0:00:00 08-31-2016
-300 days, 0:00:00 06-30-2016
-296 days, 0:00:00 07-04-2016
-296 days, 0:00:00 07-04-2016
-146 days, 0:00:00 12-01-2016
-26 days, 0:00:00 03-31-2017
-244 days, 0:00:00 08-25-2016
65 days, 0:00:00 06-30-2017
65 days, 0:00:00 06-30-2017
219 days, 0:00:00 12-01-2017
65 days, 0:00:00 06-30-2017
-85 days, 0:00:00 01-31-2017
65 days, 0:00:00 06-30-2017
65 days, 0:00:00 06-30-2017
-433 days, 0:00:00 02-18-2016
-391 days, 0:00:00 03-31-2016
-330 days, 0:00:00 05-31-2016
-330 days, 0:00:00 05-31-2016
-248 days, 0:00:00 08-21-2016
-248 days, 0:00:00 08-21-2016
-7 days, 0:00:00 04-19-2017
36 days, 0:00:00 06-01-2017
-318 days, 0:00:00 06-12-2016
-329 days, 0:00:00 06-01-2016
35 days, 0:00:00 05-31-2017
-26 days, 0:00:00 03-31-2017
-330 days, 0:00:00 05-31-2016
35 days, 0:00:00 05-31-2017
-26 days, 0:00:00 03-31-2017
-26 days, 0:00:00 03-31-2017
4 days, 0:00:00 04-30-2017
65 days, 0:00:00 06-30-2017
-847 days, 0:00:00 12-31-2014
249 days, 0:00:00 12-31-2017
249 days, 0:00:00 12-31-2017
-330 days, 0:00:00 05-31-2016
-226 days, 0:00:00 09-12-2016
249 days, 0:00:00 12-31-2017
-847 days, 0:00:00 12-31-2014
-603 days, 0:00:00 09-01-2015
249 days, 0:00:00 12-31-2017
65 days, 0:00:00 06-30-2017
-574 days, 0:00:00 09-30-2015
65 days, 0:00:00 06-30-2017
-482 days, 0:00:00 12-31-2015
65 days, 0:00:00 06-30-2017
-329 days, 0:00:00 06-01-2016
-467 days, 0:00:00 01-15-2016
-574 days, 0:00:00 09-30-2015
-391 days, 0:00:00 03-31-2016
-422 days, 0:00:00 02-29-2016
-274 days, 0:00:00 07-26-2016
-268 days, 0:00:00 08-01-2016
-464 days, 0:00:00 01-18-2016
-464 days, 0:00:00 01-18-2016
-464 days, 0:00:00 01-18-2016
-412 days, 0:00:00 03-10-2016
-391 days, 0:00:00 03-31-2016
-116 days, 0:00:00 12-31-2016
-328 days, 0:00:00 06-02-2016
-328 days, 0:00:00 06-02-2016
-328 days, 0:00:00 06-02-2016
-376 days, 0:00:00 04-15-2016
-360 days, 0:00:00 05-01-2016
-352 days, 0:00:00 05-09-2016
-352 days, 0:00:00 05-09-2016
-299 days, 0:00:00 07-01-2016
-329 days, 0:00:00 06-01-2016
-338 days, 0:00:00 05-23-2016
65 days, 0:00:00 06-30-2017
219 days, 0:00:00 12-01-2017
159 days, 0:00:00 10-02-2017
5 days, 0:00:00 05-01-2017
>>> 
for row in range(2, sheet.max_row +1):
	if sheet.cell(row=row, column=8).value == "active":
		z = ""
		z +=(str(sheet.cell(row=row, column=9).value))
		h=(z.split('-'))
		a = date.today()
		b = a.replace(day=int(h[1]), month=int(h[0]), year=int(h[2]))
		print (str(b-a )+ ' ' +str(sheet.cell(row=row, column=9).value))

		
67 days, 0:00:00 07-03-2017
-22 days, 0:00:00 04-05-2017
1 day, 0:00:00 04-28-2017
-10 days, 0:00:00 04-17-2017
-43 days, 0:00:00 03-15-2017
-43 days, 0:00:00 03-15-2017
-22 days, 0:00:00 04-05-2017
-22 days, 0:00:00 04-05-2017
-15 days, 0:00:00 04-12-2017
-27 days, 0:00:00 03-31-2017
-29 days, 0:00:00 03-29-2017
248 days, 0:00:00 12-31-2017
64 days, 0:00:00 06-30-2017
64 days, 0:00:00 06-30-2017
218 days, 0:00:00 12-01-2017
64 days, 0:00:00 06-30-2017
-8 days, 0:00:00 04-19-2017
35 days, 0:00:00 06-01-2017
34 days, 0:00:00 05-31-2017
-27 days, 0:00:00 03-31-2017
34 days, 0:00:00 05-31-2017
-27 days, 0:00:00 03-31-2017
-27 days, 0:00:00 03-31-2017
3 days, 0:00:00 04-30-2017
64 days, 0:00:00 06-30-2017
248 days, 0:00:00 12-31-2017
248 days, 0:00:00 12-31-2017
248 days, 0:00:00 12-31-2017
64 days, 0:00:00 06-30-2017
64 days, 0:00:00 06-30-2017
64 days, 0:00:00 06-30-2017
218 days, 0:00:00 12-01-2017
158 days, 0:00:00 10-02-2017
4 days, 0:00:00 05-01-2017
>>> for row in range(2, sheet.max_row +1):
	if sheet.cell(row=row, column=8).value == "active":
		z = ""
		z +=(str(sheet.cell(row=row, column=9).value))
		h=(z.split('-'))
		a = date.today()
		b = a.replace(day=int(h[1]), month=int(h[0]), year=int(h[2]))
		print (str(b-a )+ ' ' +str(sheet.cell(row=row, column=1).value))

		
67 days, 0:00:00 LIU2558
-22 days, 0:00:00 LIU2562
1 day, 0:00:00 WAT2601
-10 days, 0:00:00 CAD2651
-43 days, 0:00:00 KAD2262
-43 days, 0:00:00 KAD2263
-22 days, 0:00:00 DIE2703
-22 days, 0:00:00 BUR2707
-15 days, 0:00:00 LOK2557
-27 days, 0:00:00 BUR2708
-29 days, 0:00:00 KAV2709
248 days, 0:00:00 email url testing
64 days, 0:00:00 GED2458
64 days, 0:00:00 GED2459
218 days, 0:00:00 LIU2460
64 days, 0:00:00 MAG2501
-8 days, 0:00:00 DIE2561
35 days, 0:00:00 LIU2559
34 days, 0:00:00 LOK2865
-27 days, 0:00:00 KRA2801
34 days, 0:00:00 SUN2407
-27 days, 0:00:00 DIE2856
-27 days, 0:00:00 SHE2712
3 days, 0:00:00 DIE2854
64 days, 0:00:00 KAV2863
248 days, 0:00:00 KRA1003
248 days, 0:00:00 BUR964
248 days, 0:00:00 BTY659
64 days, 0:00:00 DAN1955
64 days, 0:00:00 KRA1754
64 days, 0:00:00 LIU2355
218 days, 0:00:00 LIU2853
158 days, 0:00:00 LIU2866
4 days, 0:00:00 DIE2867
>>> 

Python 3.6.0 (v3.6.0:41df79263a11, Dec 23 2016, 07:18:10) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> text = "ABCDEFG"
>>> test
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    test
NameError: name 'test' is not defined
>>> text
'ABCDEFG'
>>> spam
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    spam
NameError: name 'spam' is not defined
>>> spam = {}
>>> for i in text:
	spam.append(i)

	
Traceback (most recent call last):
  File "<pyshell#7>", line 2, in <module>
    spam.append(i)
AttributeError: 'dict' object has no attribute 'append'
>>> spam = []
>>> for i in text:
	spam.append(i)

	
>>> spam
['A', 'B', 'C', 'D', 'E', 'F', 'G']
>>> import random
>>> random.randint(1,len(spam))
6
>>> for i in range(0, len(spam))
SyntaxError: invalid syntax
>>> 
>>> for i in range(0, len(spam)):
	print(spam[random.randint(1,len(spam))])

	
E
B
B
F
C
G
C
>>> blank = ""
>>> for i in range(0, len(spam)):
	blank+=(spam[random.randint(1,len(spam))])

	
Traceback (most recent call last):
  File "<pyshell#24>", line 2, in <module>
    blank+=(spam[random.randint(1,len(spam))])
IndexError: list index out of range
>>> for i in range(0, len(spam)):
	print(spam[random.randint(1,len(spam))])

	
E
B
B
G
G
G
B
>>> for i in range(0, len(spam)):
	print(spam[random.randint(1,len(spam))])
	blank += spam[random.randint(1,len(spam))]

	
G
Traceback (most recent call last):
  File "<pyshell#29>", line 2, in <module>
    print(spam[random.randint(1,len(spam))])
IndexError: list index out of range
>>> for i in range(0, len(spam)):
	print(spam[random.randint(1,len(spam))])

	
G
Traceback (most recent call last):
  File "<pyshell#31>", line 2, in <module>
    print(spam[random.randint(1,len(spam))])
IndexError: list index out of range
>>> for i in range(0, len(spam)):
	print(spam[random.randint(1,len(spam))])

	
C
B
G
D
F
B
D
>>> for i in range(0, len(spam)):
	print(spam[random.randint(1,len(spam))])

	
G
Traceback (most recent call last):
  File "<pyshell#35>", line 2, in <module>
    print(spam[random.randint(1,len(spam))])
IndexError: list index out of range
>>> for i in range(0, len(spam)):
	print(spam[random.randint(0,len(spam))])

	
D
D
A
E
A
F
A
>>> for i in range(0, len(spam)):
	print(spam[random.randint(0,len(spam))])

	
C
A
B
D
F
B
C
>>> for i in range(0, len(spam)):
	print(spam[random.randint(0,len(spam))])

	
G
G
C
E
G
G
F
>>> for i in range(0, len(spam)):
	blank += spam[random.randint(0,len(spam))]

	
>>> blank
'DBACAFBCF'
>>> for i in range(0, 6):
	blank += spam[random.randint(0,len(spam))]

	
Traceback (most recent call last):
  File "<pyshell#46>", line 2, in <module>
    blank += spam[random.randint(0,len(spam))]
IndexError: list index out of range
>>> for i in range(0, 6):
	blank += spam[random.randint(0,len(spam))]

	
Traceback (most recent call last):
  File "<pyshell#48>", line 2, in <module>
    blank += spam[random.randint(0,len(spam))]
IndexError: list index out of range
>>> blank = ''
>>> for i in range(0, 6):
	blank += spam[random.randint(0,len(spam))]

	
Traceback (most recent call last):
  File "<pyshell#51>", line 2, in <module>
    blank += spam[random.randint(0,len(spam))]
IndexError: list index out of range
>>> for i in range(0, 6):
	blank += spam[random.randint(0,10)]

	
Traceback (most recent call last):
  File "<pyshell#53>", line 2, in <module>
    blank += spam[random.randint(0,10)]
IndexError: list index out of range
>>> for i in range(0, 2):
	blank += spam[random.randint(0,len(spam))]

	
Traceback (most recent call last):
  File "<pyshell#56>", line 2, in <module>
    blank += spam[random.randint(0,len(spam))]
IndexError: list index out of range
>>> for i in range(0, 6):
	print(spam[random.randint(0,len(spam))])

	
C
D
D
E
Traceback (most recent call last):
  File "<pyshell#58>", line 2, in <module>
    print(spam[random.randint(0,len(spam))])
IndexError: list index out of range
>>> spam
['A', 'B', 'C', 'D', 'E', 'F', 'G']
>>> for i in range(0, 5):
	print(spam[random.randint(0,len(spam))])

	
E
G
Traceback (most recent call last):
  File "<pyshell#61>", line 2, in <module>
    print(spam[random.randint(0,len(spam))])
IndexError: list index out of range
>>> for i in range(0, 5):
	print(spam[random.randint(1,len(spam))])

	
E
E
Traceback (most recent call last):
  File "<pyshell#63>", line 2, in <module>
    print(spam[random.randint(1,len(spam))])
IndexError: list index out of range
>>> for i in range(0, 5):
	print(spam[random.randint(1,len(spam)+1)])

	
Traceback (most recent call last):
  File "<pyshell#65>", line 2, in <module>
    print(spam[random.randint(1,len(spam)+1)])
IndexError: list index out of range
>>> for i in range(0, 5):
	print(spam[random.randint(1,len(spam)-1)])

	
D
E
F
F
B
>>> for i in range(0, 5):
	print(spam[random.randint(0,len(spam)-1)])

	
F
C
C
D
C
>>> for i in range(0, 5):
	print(spam[random.randint(0,len(spam)-1)])

	
F
D
C
A
C
>>> for i in range(0, 6):
	print(spam[random.randint(0,len(spam)-1)])

	
F
F
F
D
B
C
>>> spam
['A', 'B', 'C', 'D', 'E', 'F', 'G']
>>> for i in range(0, 6):
	print(spam[random.randint(0,len(spam)-1)])

	
C
A
B
A
C
C
>>> for i in range(0, 6):
	print(spam[random.randint(0,len(spam)-1)])

	
C
C
B
B
G
B
>>> len(spam)
7
>>> for i in range(0, 6):
	print(spam[random.randint(0,len(spam)-1)])
	blank += (spam[random.randint(0,len(spam)-1)])

	
B
B
F
B
D
A
>>> blank
'AFEEEGFACBB'
>>> blank = ''
>>> for i in range(0, 6):
	print(spam[random.randint(0,len(spam)-1)])
	blank += (spam[random.randint(0,len(spam)-1)])

	
G
B
B
E
D
F
>>> blank
'BCEDAA'
>>> "#" + blank
'#BCEDAA'
>>> dec = 'ABCDEF0123456789'
>>> dec
'ABCDEF0123456789'
>>> for i in dec:
	print (i)

	
A
B
C
D
E
F
0
1
2
3
4
5
6
7
8
9
>>> for i in range(0,6):
	print (dec(i))

	
Traceback (most recent call last):
  File "<pyshell#96>", line 2, in <module>
    print (dec(i))
TypeError: 'str' object is not callable
>>> for i in range(0,6):
	print (dec[i])

	
A
B
C
D
E
F
>>> for i in range(0,6):
	print (dec[random.randint(0,len(dec)-1)])

	
3
B
7
0
D
7
>>> def color():
    hecks = 'ABCDEF012345678'
    randomcolor = "#"
    for i in range(0,6):
        randomcolor += (hecks[random.ranint(0, len(hecks)-1)])
    return randomcolor

>>> color()
Traceback (most recent call last):
  File "<pyshell#103>", line 1, in <module>
    color()
  File "<pyshell#102>", line 5, in color
    randomcolor += (hecks[random.ranint(0, len(hecks)-1)])
AttributeError: module 'random' has no attribute 'ranint'
>>> def color():
    hecks = 'ABCDEF012345678'
    randomcolor = "#"
    for i in range(0,6):
        randomcolor += (hecks[random.randint(0, len(hecks)-1)])
    return randomcolor

>>> def color():
    hecks = 'ABCDEF012345678'
    randomcolor = "#"
    for i in range(0,6):
        randomcolor += (hecks[random.randint(0, len(hecks)-1)])
    return randomcolor
	print(randomcolor)
	
SyntaxError: inconsistent use of tabs and spaces in indentation
>>> def color():
	hecks = 'ABCDEF012345678'
	randomcolor = "#"
	for i in range(0,6):
		randomcolor += (hecks[random.randint(0, len(hecks)-1)])
	return randomcolor
	print(randomcolor)

	
>>> color()
'#73703F'
>>> def cells(x, y):
	str(page.cell(row=x, column=y).value)

	
>>> print cells(1, 17)
SyntaxError: invalid syntax
>>> print (cells(1, 17))
Traceback (most recent call last):
  File "<pyshell#115>", line 1, in <module>
    print (cells(1, 17))
  File "<pyshell#113>", line 2, in cells
    str(page.cell(row=x, column=y).value)
NameError: name 'page' is not defined
>>> print(str(cells(1,17)))
Traceback (most recent call last):
  File "<pyshell#116>", line 1, in <module>
    print(str(cells(1,17)))
  File "<pyshell#113>", line 2, in cells
    str(page.cell(row=x, column=y).value)
NameError: name 'page' is not defined
>>> color()
'#600F23'
>>> color()
'#C5CDEE'
>>> color()
'#D3DE31'
>>> color()
'#5B66FC'
>>> color()
'#8DD8E5'
>>> def ice(x, y, z):
	return 5 + x + 2 + y + z

>>> def(10, 17, 19)
SyntaxError: invalid syntax
>>> ice(10, 17, 19)
53
>>> ice(10, 0, 0)
17
>>> 

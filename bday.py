#! python3
import ast
import pprint
import os

if os.path.exists(os.getcwd() + '\\bday.txt'):
    birthdayList = open(os.getcwd() + '\\bday.txt', 'r').read()
    birthdays = ast.literal_eval(birthdayList)

else:
    birthdays = {}

pprint.pprint(birthdays)

while True:
    print ('Enter a name: (blank to quit)')
    name = input()
    if name == '':
        break
    elif name in birthdays:
        print(birthdays[name] + ' is the birthday of ' + name)
    else:
        print ('I do not have birthday information for ' + name)
        print ('What is their birthday?')
        bday = input()
        birthdays[name] = bday
        print ('Birthday database updated.')

while True:
    print ('Enter a name to delete: (blank to quit) ')
    name = input()
    if name == '':
        break
    elif name in birthdays:
        print (name + ' Will be removed')
        del birthdays[name]
        print (birthdays)


bdayFile = open('c:\\Users\\t862537\\Python\\Python36-32\\bday.txt', 'w')
bdayFile.write(str(birthdays))
bdayFile.close()

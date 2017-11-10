#! python3

import ast
import pprint
import os

if os.path.exists(os.getcwd() + '\\todolist.txt'):
    toDoList = open(os.getcwd() + '\\todolist.txt', 'r').read()
    toDo = ast.literal_eval(toDoList)
else:
    toDo = {}

print('Your to do list: ')
pprint.pprint(toDo)

while True:
    print ('Enter a date (MM/DD): ')
    date = input()
    if date == '':
        break
    elif len(date) != 5:
        print ('Please enter the date in the correct format - MM/DD')
    elif date[0:2].isnumeric() and date[3:].isnumeric():
        if date in toDo:
            print (toDo[date] + ' is the task for ' + date)
        else:
            print ('There is no task for: ' + date)
            print ('What task would you like to add?')
            task = input()
            toDo[date] = task
            print('To Do list updated.')
    else:
        print ('Please enter the date in the correct format - 01/01')

toDoFile = open('c:\\Users\\t862537\\Python\\Python36-32\\todolist.txt', 'w')
toDoFile.write(str(toDo))
toDoFile.close()
        
'''while True:
    print ('Enter a task to delete: ')
    task = input()
    if task == '':
        break
    elif task in toDo.values():
        spam = 
        
        print (task + 'will be removed')
        del 
'''

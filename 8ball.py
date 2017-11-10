#! python 3
# Magic 8 ball

import random
from time import sleep

def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'It is certain'
    elif answerNumber == 2:
        return 'It is decidedly so'
    elif answerNumber == 3:
        return 'Yes'
    elif answerNumber == 4:
        return 'Reply hazy try again'
    elif answerNumber == 5:
        return 'Ask again later'
    elif answerNumber == 6:
        return 'Concentrate and ask again'
    elif answerNumber == 7:
        return 'My reply is no'
    elif answerNumber == 8:
        return 'Outlook not so good'

def fortune():
	r = random.randint(1,9)
	print ("Ask the Magic 8 ball a question to see your fortune:")
	input()
	print('Behold your fortune in')
	print('...3')
	sleep(1)
	print('...2')
	sleep(1)
	print('...1')
	sleep(1)
	print (getAnswer(r))

fortune()

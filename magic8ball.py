#! python3
#magic 8 ball with switch dictionary

import random
from time import sleep

def getAnswer(answerNumber):
    response = {
        1: 'It is certain',
        2: 'It is decidedly so',
        3: 'Yes',
        4: 'Reply hazy, try again',
        5: 'Ask again later',
        6: 'Concentrate and ask again',
        7: 'My reply is no',
        8: 'Outlook not so good',
        }
    return response.get(answerNumber, "fortune teller is unavailable")

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

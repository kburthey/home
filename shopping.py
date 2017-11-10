#! Python3
import logging
logging.basicConfig(filename='ShoppingLog.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
#this will take items and store a shopping list
logging.disable(logging.DEBUG)
from time import sleep
import sys
import os
import ast
from time import strftime
import logging

if os.path.exists(os.getcwd() + '\\food.txt'):
    shoppingList = open(os.getcwd() + '\\food.txt', 'r').read()
    groce = ast.literal_eval(shoppingList)
else:
    groce = []
    
def welcome():
    name = input("Enter Your Name: ")
    print ("Now opening " + name + "'s grocery list...")
    sleep(2)
    print ("Ready!")
def eats():
    welcome()
    shop = True
    while shop:
        grub = []
        try:
            print ("Current shopping list: " + str(groce).strip('[]'))
            food = input("What would you like to add to your list?: ")
            if food.isalpha():
                print (food)
                groce.append(food)
                grub.append(food)
                more = input("Do you have another item? Y/N: ")
                more = more.upper()
                if more == "Y":
                    continue
                elif more != "N":
                    print ("Sorry, I didn't understand that")
                else:
                    shop = False
            elif food == "":
                break
            else:
                print ("You must enter a word, not a number!")
        except TypeError:
            print ("You must inter a word, not a number")
    print ("Here are your recently added items: " + str(grub).strip('[]'))



eats()

with open("food.txt", "w") as food:
    food.write(str(groce))
    #for x in groce:
        #food.write("%s\n" %x)

with open("food.txt", "r+") as food:
    print ("The following items are now in your list: ")
    print (str(food.read()).strip('[]'))
    '''eating = ""
    for i in food.read():
        if i.isalpha() or i.isspace():
            eating += i
    print (eating)'''


def removal():
    shoppingList = open(os.getcwd() + '\\food.txt', 'r').read()
    groce = ast.literal_eval(shoppingList)
    while True:
        response = input("Would you like to remove anything from the list? Y/N: ")
        response = response.upper()
        if response == "Y":
            try:
                logging.debug(groce) 
                to_remove = input("Which Item?: ")
                groce.remove(to_remove)
                logging.debug(groce)
                with open("food.txt", "w+") as food:
                    food.write(str(groce))
                with open("food.txt", "r") as food:
                    print ("The following items remain in your list: ")
                    print (str(food.read()).strip('[]'))
            except ValueError:
                print ("That item isn't in the list!")
        elif response == "N":
            print ("OK, Bye!")
            break
        else:
            print ("You didn't say yes or no, so I am closing now")
            break

removal()

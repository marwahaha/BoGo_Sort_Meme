#BoGo Sort Meme Code | Python | Mehmet Yilmaz | Feb 22, 2019

import random

# Variables for changing Terminal Text Output
class variables:
   PURPLE = '\033[95m';     CYAN = '\033[96m';      DARKCYAN = '\033[36m';   BLUE = '\033[94m'
   GREEN = '\033[92m';      YELLOW = '\033[93m';    RED = '\033[91m';        BOLD = '\033[1m'
   UNDERLINE = '\033[4m';   END = '\033[0m';        KARMA = "{:,d}";         list = [];
   list_og = [];            counter = 1;            STOP = True

# Over all BoGo Sort function
def bogo_sort(): #bogo_sort() needs class variables to work
    print(" "); print(variables.UNDERLINE + variables.BOLD + variables.GREEN + "BoGo Sort → O((n+1)!)" + variables.END)
    x = int(input(variables.DARKCYAN + "Enter a Size: " + variables.END))
    for i in range(x):
        variables.list.append(i)
        variables.list_og.append(i)
        random.shuffle(variables.list)
    print(variables.PURPLE + "    Unsorted:" + variables.END, str(variables.list))
    while(True):
        random.shuffle(variables.list)
        if (variables.list == variables.list_og):
            print(variables.DARKCYAN + "      Sorted:" + variables.END, str(variables.list_og))
            print(variables.CYAN + "  # of Tries:" + variables.END, (variables.RED + variables.KARMA.format(variables.counter) + variables.END)); print(" ")
            break
        variables.counter += 1

# Prints meme if demanded
# meme_print() needs class variables to work
def meme_print():
    import time ; time.sleep(1); print(" " + variables.YELLOW)
    print("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
    print("░░░░░░▄▄▄▄▀▀▀▀▀▀▀▀▄▄▄▄▄▄░░░░░░░░░░")
    print("░░░░░░█░░░░▒▒▒▒▒▒▒▒▒▒▒▒░░▀▀▄░░░░░░")
    print("░░░░░█░░░▒▒▒▒▒▒░░░░░░░░▒▒▒░░█░░░░░")
    print("░░░░█░░░░░░▄██▀▄▄░░░░░▄▄▄░░░█░░░░░")
    print("░░░▀▒▄▄▄▒░█▀▀▀▀▄▄█░░░██▄▄█░░░█░░░░")
    print("░░█▒█▒▄░▀▄▄▄▀░░░░░░░░█░░░▒▒▒▒▒█░░░")
    print("░░█▒█░█▀▄▄░░░░░█▀░░░░▀▄░░▄▀▀▀▄▒█░░")
    print("░░░█▀▄░█▄░█▀▄▄░▀░▀▀░▄▄▀░░░░█░░█░░░")
    print("░░░░█░░▀▄▀█▄▄░█▀▀▀▄▄▄▄▀▀█▀██░█░░░░")
    print("░░░░░█░░██░░▀█▄▄▄█▄▄█▄████░█░░░░░░")
    print("░░░░░░█░░░▀▀▄░█░░░█░███████░█░░░░░")
    print("░░░░░░░▀▄░░░▀▀▄▄▄█▄█▄█▄█▄▀░░█░░░░░")
    print("░░░░░░░░░▀▄▄░▒▒▒▒░░░░░░░░░░█░░░░░░")
    print("░░░░░░░░░░░░▀▀▄▄░▒▒▒▒▒▒▒▒▒▒░█░░░░░")
    print("░░░░░░░░░░░░░░░░▀▄▄▄▄▄▄▄▄▄▄█░░░░░░")
    print("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
    print("░░" + variables.RED + " I don't always write my own " + variables.YELLOW + " ░░")
    print("░░" + variables.RED + " sorting algorithm, But ... " + variables.YELLOW + "  ░░")
    print("░░" + variables.RED + " when I do, I use Bogosort " + variables.YELLOW + "   ░░")
    print(variables.YELLOW + "░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
    print("░░ See BoGo Output(s) above ... ░░")
    print("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")

def looping(choice):
    if(choice == 1):
        while (True):
            print(variables.UNDERLINE + variables.BOLD + variables.GREEN + "BoGo Sort Code" + variables.END)
            x = input(variables.DARKCYAN + "Meme Mode ['y' or 'n']: " + variables.END); x = x.lower()
            if (x == "yes" or x == "y"):
                meme_print()
                bogo_sort()
                break
            elif (x == "no" or x == "n"):
                bogo_sort()
                break
            else:
                print(variables.RED + "Invalid Entry, Try Again! " + variables.END); print(" ")
    elif(choice == 0):
        while(True):
            x = input(variables.DARKCYAN + "Run Again ['y' or 'n']: " + variables.END); x = x.lower()
            if (x == "yes" or x == "y"):
                print(" "); break
            elif (x == "no" or x == "n"):
                variables.STOP = False
                print(" "); print(variables.BOLD + variables.BLUE + "Shut Down")
                break
            else:
                print(variables.RED + "Invalid Entry, Try Again! " + variables.END); print(" ")

def main():
    while (variables.STOP):
        # [1] = Part 1 of GUI   |   [0] = Part 2 of GUI #
        looping(1); looping(0)
        variables.list_og.clear(); variables.list.clear()

main()
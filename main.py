import random
import easygui as eg
from easygui import *
import os


def randPass():

    title = "Random Password Generation"
    x = enterbox("How long do you want your generated password to be?")

    value = str(x)

    symbols = "default"
    numbers = "default"

    print("Answer with yes/no")
    passAskSym = input('Include symbols?: ')
    if passAskSym == 'yes' or passAskSym == 'Yes':
        symbols = "yes"
        print("User Entered Yes\n")
    if passAskSym == 'no' or passAskSym == 'No':
        symbols = "no"
        print("User Entered No\n")
    else:
        error = "True"

    print("Answer with yes/no")
    passAskNum = input('Include numbers?: ')
    if passAskNum == 'yes' or passAskNum == 'Yes':
        numbers = "yes"
        print("User entered yes\n")
    if passAskNum == 'no' or passAskNum == 'No':
        numbers = "no"
        print("User entered no\n")
    else:
        error = "True"

    randLower = "abcdefghijklmnopqrstuvwxyz"
    randUpper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    randNumber = "01234567890"
    randSymbol = "!@#$^&*()?"

    default = randLower + randUpper

    if numbers == 'yes' and symbols == 'no':
        default = randLower + randUpper + randNumber
        pickRandom = "".join(random.sample(default, int(value)))
        print("Password: " + pickRandom)

    if numbers == 'yes' and symbols == 'yes':
        default = randLower + randUpper + randNumber + randSymbol
        pickRandom = "".join(random.sample(default, int(value)))
        print("Password: " + pickRandom)

    if numbers == 'no' and symbols == 'no':
        default = randLower + randUpper
        pickRandom = "".join(random.sample(default, int(value)))
        print("Password: " + pickRandom)

    if numbers == 'no' and symbols == 'yes':
        default = randLower + randUpper + randSymbol
        pickRandom = "".join(random.sample(default, int(value)))
        print("Password: " + pickRandom)


randPass()

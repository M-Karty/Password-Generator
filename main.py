import random
import easygui as eg
from easygui import *

def randPass():
    
    def passwordLength():
        global value, title1, enterBox
        
        title1 = "Random Password Generation"
        enterBox = enterbox("How long do you want your generated password to be?")
        value = str(enterBox)
        
    passwordLength()

    def choiceBox():
        global reply, title2
        title2 = "Random Password Generation"
        msg = "Do you want to use symbols, numbers or both?"
        choices = ["Symbols", "Numbers", "Both", "None"]
        reply = choicebox(msg, title2, choices)
    choiceBox()
    
    randLower = "abcdefghijklmnopqrstuvwxyz"
    randUpper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    randNumber = "01234567890"
    randSymbol = "!@#$^&*()?"
    
    default = randLower + randUpper
    
    password = ""
    
    if reply == "Symbols":
        print("Symbols")
        default = default + randSymbol
        pickRandom = "".join(random.sample(default, int(value)))
        password = pickRandom

    if reply == "Numbers":
        print("Numbers")
        default = default + randNumber
        pickRandom = "".join(random.sample(default, int(value)))
        password = pickRandom
        
    if reply == "Both":
        print("Both")
        default = default + randSymbol + randNumber
        pickRandom = "".join(random.sample(default, int(value)))
        password = pickRandom

    if reply == "None":
        print("None")
        default = default
        pickRandom = "".join(random.sample(default, int(value)))
        password = pickRandom
    
    def finalPassword():
        global title3
        title3 = "Random Password Generation"
        msgbox("Password: " + password) 

    finalPassword()
randPass()
    
    

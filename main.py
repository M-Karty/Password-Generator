import random


def randPass():

    print("Random Password Generation")

    symbols = "default"
    numbers = "default"

    error = "False"

    passlen = int(input('How long do you want your password?: '))
    print('\n')

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
        pickRandom = "".join(random.sample(default, passlen))
        print("Password: " + pickRandom)

    if numbers == 'yes' and symbols == 'yes':
        default = randLower + randUpper + randNumber + randSymbol
        pickRandom = "".join(random.sample(default, passlen))
        print("Password: " + pickRandom)

    if numbers == 'no' and symbols == 'no':
        default = randLower + randUpper
        pickRandom = "".join(random.sample(default, passlen))
        print("Password: " + pickRandom)

    if numbers == 'no' and symbols == 'yes':
        default = randLower + randUpper + randSymbol
        pickRandom = "".join(random.sample(default, passlen))
        print("Password: " + pickRandom)


randPass()

from lib2to3.pygram import Symbols
import string
from random import choice, shuffle
from symtable import Symbol

def randomPass():
    # Possible values for password
    lowercase = list(string.ascii_lowercase)
    uppercase = list(string.ascii_uppercase)
    numbers = list(string.digits)
    symbol = list(r'\/:*?"<>-@#$^&|') 

    # Combination of mixed values
    combinatrix = uppercase + lowercase + numbers + symbol
    shuffle(combinatrix)

    # User input for password length
    length = int(input("Length of password?:"))
    password = " "

    for i in range(length):
        password += choice(combinatrix)
    print(password)

randomPass()


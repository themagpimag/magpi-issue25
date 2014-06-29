#!/usr/bin/python
#Filename: Py-Enigma.py

#A Python implementation of the Pocket Enigma Cypher Machine.

#Ian Neill (c)2014
# - Works with Python v2.7

import random

VERSION = "v1.0.0"
BUILDDATE = "01/06/2014"

#WHEEL DEFINITIONS
WHEEL1 = [-1,3,-5,7,-3,2,3,-2,4,-3,-7,6,-4,1,-1,6,3,-6,2,-3,-2,-6,2,5,-2,1]
WHEEL2 = [2,2,-2,-2,-8,3,9,5,-3,1,-1,2,-5,-2,2,-9,-2,8,2,2,-2,-2,8,1,-1,-8]

#GLOBAL VARIABLES WITH STARTING VALUES
wheel = 1
pointer_l = 'D'
pointer_n = ord(pointer_l)-65
code_start_l = 'J'
code_start_n = ord(code_start_l)-65
increment = 1
blocksize = 5

DEFAULT_MESSAGE = "ATTACK AT DAWN" #And why not? They will never expect it...

#MAIN PROGRAM
def main():
    global wheel, pointer_l, pointer_n, code_start_l, code_start_n, increment, blocksize
    welcome("Py-Enigma - The Pocket Enigma Cypher Machine")
    menu_min = 1
    menu_max = 7
    menu_quit = 0
    prg_quit = False
    while not prg_quit:
        #Show the Menu.
        show_menu(menu_min, menu_max, menu_quit)
        #Get the User Choice.
        user_choice = get_choice(menu_min, menu_max, menu_quit)
        #Take action as per selected menu-option.
        if user_choice == menu_quit:
            prg_quit = True
        elif user_choice == 1:
            wheel = prg_choice1()
        elif user_choice == 2:
            pointer_l = prg_choice2()
            pointer_n = ord(pointer_l)-65
        elif user_choice == 3:
            code_start_l = prg_choice3()
            code_start_n = ord(code_start_l )-65
        elif user_choice == 4:
            increment = prg_choice4()
        elif user_choice == 5:
            blocksize = prg_choice5()
        elif user_choice == 6:
            prg_choice6()
        elif user_choice == 7:
            prg_choice7()
        elif user_choice == 8:
            prg_choice6()
        elif user_choice == 9:
            prg_choice7()
    print "\nGoodbye.\n"
    return
    #End

#FUNCTIONS

#Welcome Function
def welcome(message):
    print message
    print "   Version,", str(VERSION), ",", str(BUILDDATE)
    print
    return

#Show Menu
def show_menu(min, max, quit):
    print (30 * '-')
    print "      P y - E N I G M A"
    print "      M A I N - M E N U"
    print (30 * '-')
    print
    if (min <= 1 <= max):
        print " 1. Set Wheel      =", wheel
    if (min <= 2 <= max):
        print " 2. Set Pointer    =", pointer_l
    if (min <= 3 <= max):
        print " 3. Set Code Start =", code_start_l
    if (min <= 4 <= max):
        print " 4. Set Increment  =", increment
    if (min <= 5 <= max):
        print " 5. Set Block Size =", blocksize
    if (min <= 6 <= max):
        print " 6. Encrypt a Message"
    if (min <= 7 <= max):
        print " 7. Decrypt a Message"
    if (min <= 8 <= max):
        print " 8. Nothing Yet"
    if (min <= 9 <= max):
        print " 9. Nothing Yet"
    print
    print " " + str(quit) + ". Exit program"
    print
    print (30 * '-')
    return

def getValue(min,max):
  while 1:
    inputValue = raw_input("Enter choice [%s--%s]: " % (str(min),str(max)))
    if len(inputValue) == 0:
      print("Error: no value given")
      continue
    return inputValue

def getInteger(min,max):
  while 1:
    inputValue = getValue(min,max)
    try:
      intValue = int(inputValue)
    except ValueError:
      print("Error: \"%s\" is not an integer" % inputValue)
      continue
    if intValue < min or intValue > max:
      print("Error: \"%d\" is outside range [%d--%d]" % (intValue,min,max))
      continue
    return intValue

def getCharacter(min,max):
  while 1:
    inputValue = getValue(min,max)
    if len(inputValue) != 1:
      print("Error: \"%s\" is not a single character" % inputValue)
      continue
    charValue = inputValue.upper()
    if ord(charValue) < ord(min) or ord(charValue) > ord(max):
      print("Error: %s is outside range [%s--%s]" % (charValue,min,max))
      continue
    return charValue

#Get User Choice
def get_choice(min, max, quit):
    #Wait for valid choice in while...not.
    choice_is_valid=False
    while not choice_is_valid:
        try:
            choice = int(raw_input("Enter choice [" + str(min) + "-" + str(max) + "]: "))
            if (min <= choice <= max or choice == quit):
                #A valid choice will terminate the while...not loop.
                choice_is_valid = True
            else:
                print"Error! Only numbers " + str(min) + "-" + str(max) + " or " + str(quit) + " are valid."
        except ValueError as e:
            print ("Error! %s is not a valid choice." % e.args[0].split(": ")[1])
    return(choice)

#Option 1
def prg_choice1():
    print
    #Wait for valid choice in while...not.
    choice_is_valid=False
    while not choice_is_valid:
        try:
            choice = int(raw_input("Enter Coding Wheel [1 or 2]: "))
            if (1 <= choice <= 2):
                #A valid choice will terminate the while...not loop.
                choice_is_valid = True
            else:
                print"Error! Only numbers 1 or 2 are valid."
        except ValueError as e:
            print ("Error! %s is not a valid choice." % e.args[0].split(": ")[1])
    print
    return(choice)

#Option 2
def prg_choice2():
    print
    #Wait for valid choice in while...not.
    choice_is_valid=False
    while not choice_is_valid:
        try:
            choice = raw_input("Enter Pointer Position [A to Z]: ").upper()
            if (65 <= ord(choice) <= 90):
                #A valid choice will terminate the while...not loop.
                choice_is_valid = True
            else:
                print"Error! Only letters A to Z are valid."
        except ValueError as e:
            print ("Error! %s is not a valid choice." % e.args[0].split(": ")[1])
    print
    return(choice)

#Option 3
def prg_choice3():
    print
    #Wait for valid choice in while...not.
    choice_is_valid=False
    while not choice_is_valid:
        try:
            choice = raw_input("Enter Coding Start Position [A to Z]: ").upper()
            if (65 <= ord(choice) <= 90):
                #A valid choice will terminate the while...not loop.
                choice_is_valid = True
            else:
                print"Error! Only letters A to Z are valid."
        except ValueError as e:
            print ("Error! %s is not a valid choice." % e.args[0].split(": ")[1])
    print
    return(choice)

#Option 4
def prg_choice4():
    print
    #Wait for valid choice in while...not.
    choice_is_valid=False
    while not choice_is_valid:
        try:
            choice = int(raw_input("Enter Increment [-1, 0 or 1]: "))
            if (-1 <= choice <= 1):
                #A valid choice will terminate the while...not loop.
                choice_is_valid = True
            else:
                print"Error! Only numbers -1, 0 and 1 are valid."
        except ValueError as e:
            print ("Error! %s is not a valid choice." % e.args[0].split(": ")[1])
    print
    return(choice)

#Option 5
def prg_choice5():
    print
    #Wait for valid choice in while...not.
    choice_is_valid=False
    while not choice_is_valid:
        try:
            choice = int(raw_input("Enter Block Size [1 to 10]: "))
            if (1 <= choice <= 10):
                #A valid choice will terminate the while...not loop.
                choice_is_valid = True
            else:
                print"Error! Only numbers 1 to 10 are valid."
        except ValueError as e:
            print ("Error! %s is not a valid choice." % e.args[0].split(": ")[1])
    print
    return(choice)

#Option 6
def prg_choice6():
    print
    plaintext = raw_input("Enter Plaintext: ")
    print "Encryption:", plaintext, "=>", encrypt(plaintext)
    print

#Option 7
def prg_choice7():
    print
    cypher = raw_input("Enter Cypher: ")
    print "Plaintext:", cypher, "=>", decrypt(cypher)
    print

#Encrypt a string
def encrypt(plaintext):
    #Set the wheel to the key character.
    pointer = pointer_n
    cypher = ''
    #Encrypt the Alpha Start character.
    cypher += transform_char(code_start_l, wheel, pointer)
    cypher += ' '
    #Set the wheel to the Alpha Start character.
    pointer = code_start_n
    block = 0
    for o_char in plaintext:
        #Substitute periods with X's.
        if o_char == '.':
            o_char = 'X'
        #Encrypt each letter in the plaintext.
        e_char = transform_char(o_char, wheel, pointer)
        #Do something if the character was encrypted ok.
        if len(e_char) > 0:
            block += 1
            #Add a space after a block of blocksize characters.
            if block > blocksize:
                cypher += ' '
                block = 1 #Remembering the character that was blocksize+1.
            #Add the character to the result.
            cypher += e_char
            #Turn the wheel.
            pointer = (pointer + increment)%26
    return(cypher)

#Decrypt a string
def decrypt(cypher):
    #Set the wheel to the key character.
    pointer = pointer_n
    #Extract and decrypt the Alpha Start character.
    pointer = ord(transform_char(cypher[:1], wheel, pointer))-65
    plaintext = ''
    for e_char in cypher[1:]:
        #Decrypt each letter in the cypher.
        o_char = transform_char(e_char, wheel, pointer)
        #Do something if the character was decrypted ok.
        if len(o_char) > 0:
            #Add the character to the result.
            plaintext += o_char
            #Turn the wheel.
            pointer = (pointer + increment)%26
    return(plaintext)

#Encrypt/Decrypt a single character
def transform_char(char, wheel, pointer):
    #Ensure that the character is Upper Case.
    char = char.upper()
    #Only characters A-Z can be encrypted or decrypted.
    if(65 <= ord(char) <= 90):
        #ASCII => Alphabetical position of the character.
        char_num = ord(char)-65
        if (wheel == 1):
            #Get the Wheel1 Offset for this character with this pointer.
            #Uses MOD maths to turn the Wheel1 List into a circle.
            offset = WHEEL1[(char_num - pointer)%26]
        else:
            #Get the Wheel2 Offset for this character with this pointer.
            #Uses MOD maths to turn the Wheel2 List into a circle.
            offset = WHEEL2[(char_num - pointer)%26]
        #Transformed alphabetical position of the character => ASCII.
        #Uses MOD maths to turn the alphabet into a circle.
        char = chr(65 + (char_num + offset)%26)
    else:
        #Ensure nothing is returned if the character is not A-Z.
        char = ''
    return(char)

#Run the program if it is the primary module
if __name__ == '__main__':
    main()

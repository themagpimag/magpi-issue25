#!/usr/bin/python
#Filename: Py-Enigma.py

#A Python implementation of the Pocket Enigma Cipher Machine.

#Ian Neill (c)2014
# - Works with Python v2.7

VERSION = "v1.0.0"
BUILDDATE = "01/06/2014"

# Global variables with starting values
selectedWheel = 1
pointerChar = 'D'
pointerInt = ord(pointerChar)-65
codeStartChar = 'J'
codeStartInt = ord(codeStartChar)-65
increment = 1
blocksize = 5

# Wheel definitions
wheel1 = [-1,3,-5,7,-3,2,3,-2,4,-3,-7,6,-4,1,-1,6,3,-6,2,-3,-2,-6,2,5,-2,1]
wheel2 = [2,2,-2,-2,-8,3,9,5,-3,1,-1,2,-5,-2,2,-9,-2,8,2,2,-2,-2,8,1,-1,-8]

#---------------------------------------
# Encrypt or decrypt a single character
def transformChar(character, selectedWheel, pointer):
  character = character.upper()  # Ensure that the character is Upper Case.
  if(65 <= ord(character) <= 90):  # Only characters A-Z can be encrypted or decrypted.    
    char_num = ord(character) - 65  # Convert ASCII to alphabetical position of the character.

    # Choose the offset for wheel one or two.  Then use the pointer value.
    if (selectedWheel == 1):
      offset = wheel1[(char_num - pointer)%26]  # Use mod with 26 to stay within circle
    else:
      offset = wheel2[(char_num - pointer)%26]  # Use mod with 26 to stay within circle

    # Convert alphabetical position of the character back to ASCII
    character = chr(65 + (char_num + offset)%26)  # Convert position back to ASCII character
  else:
    character = ''  # Ensure that nothing is returned if the character is not A-Z.
  return character
#---------------------------------------
# Encrypt a string
def encrypt(plaintext):
  pointer = pointerInt  # Set the wheel to the key character.
  cipher = ''
  cipher += transformChar(codeStartChar, selectedWheel, pointer)  # Encrypt the Alpha Start character.
  cipher += ' '
  pointer = codeStartInt # Set the wheel to the Alpha Start character.
  block = 0

  # Encrypt each letter in the plaintext string
  for o_char in plaintext:
    # Substitute '.' with 'X'
    if o_char == '.':
      o_char = 'X'

    # Encrypt this character
    e_char = transformChar(o_char, selectedWheel, pointer)

    # Do something if the character was encrypted ok.
    if len(e_char) > 0:
      block += 1
      if block > blocksize:
        cipher += ' ' # Add a space after a block of blocksize characters.
        block = 1   # Remembering the character that was blocksize+1.
         
      cipher += e_char  # Add the character to the result.
      pointer = (pointer + increment)%26  # Turn the wheel, using mod 26 to return to zero
  return cipher
#---------------------------------------
# Decrypt a string
def decrypt(cipher):
  pointer = pointerInt  # Set the wheel to the key character.

  # Extract and decrypt the Alpha Start character.
  pointer = ord(transformChar(cipher[:1], selectedWheel, pointer))-65

  plaintext = '' # Output string with no characters
  # Decrypt each letter in the cipher.
  for e_char in cipher[1:]:
    # Decrypt this character
    o_char = transformChar(e_char, selectedWheel, pointer)

    # Do something if the character was decrypted ok.
    if len(o_char) > 0:
      plaintext += o_char   # Add the character to the result.
      pointer = (pointer + increment)%26   # Turn the wheel, using mod 26 to return to zero
  return plaintext
#---------------------------------------
# Welcome message
def welcome(message):
  print(message)
  print("   Version, %s, %s" % (VERSION, BUILDDATE))
#---------------------------------------
# Print the available menu options
def showMenu(min, max, quit):
  print("\n" + 30 * '-')
  print("      P y - E N I G M A")
  print("      M A I N - M E N U")
  print(30 * '-' + "\n")
  for i in xrange(min,max+1):
    if i == 1:
      print(" 1. Set Wheel      = %d" % selectedWheel)
    elif i == 2:
      print(" 2. Set Pointer    = %s" % pointerChar)
    elif i == 3:
      print(" 3. Set Code Start = %s" % codeStartChar)
    elif i == 4:
      print(" 4. Set Increment  = %d" % increment)
    elif i == 5:
      print(" 5. Set Block Size = %d" % blocksize)
    elif i == 6:
      print(" 6. Encrypt a Message")
    elif i == 7:
      print(" 7. Decrypt a Message")
    elif i == 8:
      print(" 8. Nothing Yet")
    elif i == 9:
      print(" 9. Nothing Yet")
    else:
        continue
    
  print("\n %d. Exit program\n" % quit)
  print(30 * '-')
#---------------------------------------
def getValue(request="Enter choice: "):
  while 1:
    inputValue = raw_input(request)
    if len(inputValue) == 0:
      print("Error: no value given")
      continue
    return inputValue
#---------------------------------------
def getInteger(min,max,request,checkRange = True):
  while 1:
    inputValue = getValue(request)
    try:
      intValue = int(inputValue)
    except ValueError:
      print("Error: \"%s\" is not an integer" % inputValue)
      continue
    if (intValue < min or intValue > max) and checkRange:
      print("Error: \"%d\" is outside range [%d--%d]" % (intValue,min,max))
      continue
    return intValue
#---------------------------------------
def getCharacter(min,max,request):
  while 1:
    inputValue = getValue(request)
    if len(inputValue) != 1:
      print("Error: \"%s\" is not a single character" % inputValue)
      continue
    charValue = inputValue.upper()
    if ord(charValue) < ord(min) or ord(charValue) > ord(max):
      print("Error: \"%s\" is outside range [%s--%s]" % (charValue,min,max))
      continue
    return charValue
#---------------------------------------
# Main function
def main():
  global selectedWheel, pointerChar, pointerInt, codeStartChar, codeStartInt, increment, blocksize
  welcome("Py-Enigma - The Pocket Enigma Cipher Machine")
  menuMin = 1
  menuMax = 7
  menuQuit = 0

  while 1:
    showMenu(menuMin, menuMax, menuQuit) # Show the menu

    # Get the user choice, without checking the range
    userChoice = getInteger(0,0,"Enter choice [%d--%d]: " % (menuMin, menuMax),False)
    
    # Take action as per selected menu-option.
    if userChoice == menuQuit:
      break # Leave the while loop
    elif userChoice == 1:
      selectedWheel = getInteger(1,2,"Enter Coding Wheel [1 or 2]: ")
    elif userChoice == 2:
      pointerChar = getCharacter('A','Z',"Enter Pointer Position [A to Z]: ")
      pointerInt = ord(pointerChar)-65
    elif userChoice == 3:
      codeStartChar = getCharacter('A','Z',"Enter Coding Start Position [A to Z]: ")
      codeStartInt = ord(codeStartChar)-65
    elif userChoice == 4:
      increment = getInteger(-1,1,"Enter Increment [-1, 0 or 1]: ")
    elif userChoice == 5:
      blocksize = getInteger(1,10,"Enter Block Size [1 to 10]: ")
    elif userChoice == 6:
      plaintext = getValue("Enter Plaintext: ")
      print("Encryption: %s => %s" % (plaintext,encrypt(plaintext)))
    elif userChoice == 7:
      cipher = getValue("Enter Cipher: ")
      print("Plaintext: %s => %s" % (cipher,decrypt(cipher)))
    else:
      print("Error: \"%d\" is not a valid choice" % userChoice)

  print("\nGoodbye.\n")

#--------------------------------------- 

#Run the program if it is the primary module
if __name__ == '__main__':
  main()

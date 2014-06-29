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

print getValue(0,1)
print getInteger(-1,10)
print getCharacter('A','F')

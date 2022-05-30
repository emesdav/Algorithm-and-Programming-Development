
#Class for manipulating string a bit. 
class String:
  #Check if input conditions are met and if not, insist on conditions
  def getInput(fieldName, textToDisplay, requiredfield):
    inputResult = ""
    if requiredfield == True:
      while inputResult == "":
        print("***" + fieldName + " is required")
        inputResult = input(textToDisplay + "*: ")
    else:
      inputResult = input(textToDisplay + ": ")

    return inputResult

  def evenSpacing(numberOfAllowedCharacters, string):
    lengthOfString = len(string)
    totalWhiteSpacesToAdd =  numberOfAllowedCharacters - lengthOfString

    return (string + " " * totalWhiteSpacesToAdd)
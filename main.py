from ContactClass import Contact
from MenuClass import Menu
from StringClass import String
import os

#Lets clear out the screen and start fresh and nice
os.system('cls||clear')

print("""
#####################################################################################
##### WELCOME TO THE PUBLIC CONTACT BOOK ############################################
#####################################################################################
######## Please read carefully through each prompt and follow instructions###########
#####################################################################################
""")
FullName = String.getInput("Entering a name", "Please provide your name", True)
print("Hi " + FullName + ", What Would you like to do? Please select an action in the next prompt")
Menu.Start()

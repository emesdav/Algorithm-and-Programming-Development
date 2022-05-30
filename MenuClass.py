from ContactClass import Contact
from StringClass import String

class Menu:
  # This displays the main menu
  def Start():
    selectedMenu = String.getInput("value", "Select an option: [1]Create Contact [2]Search Contacts [3]Exit", True)
    Menu.CheckSelected(selectedMenu)

  # This checks the slected menu by the user and displays the relevant prompts
  def CheckSelected(selectedMenu):
    if selectedMenu == "1":
      returnedContactID = Contact.Create()
      Menu.ContactAction(returnedContactID) #Display Action Menu
    if selectedMenu == "2":
      selectedSubMenu = String.getInput("value", "Search By: [1]ID [2]Value [3]All", True)
      if selectedSubMenu == "1":
        ContactID = String.getInput("value", "Please Enter Contact ID", True)
        Contact.SearchByID(ContactID)
        Menu.ContactAction(ContactID)
      elif selectedSubMenu == "2":
        value = String.getInput("value", "Please Enter search text", True)
        sortingOrder = String.getInput("value", "Please select sorting order [1]Default [2]By First Name [3]Mobile Number", True)
        Contact.SearchByValue(value, sortingOrder)
        Menu.ContactsAction()
      elif selectedSubMenu == "3":
        sortingOrder = String.getInput("value", "Please select sorting order [1]Default [2]By First Name [3]Mobile Number", True)
        Contact.SearchByValue("", sortingOrder)
        Menu.ContactsAction()
    if selectedMenu == "3":
      print("Thank you for swinging by. :)")
      exit()
    else:
      print("Your selection could not be recognize")
      Menu.Start()

  def ContactAction(ContactID):
    selectedAction = String.getInput("value", "Select an action to execute: [1]Delete Contact [2]Edit Contact [3]Return to Main Menu", False)
    if selectedAction == "1":
      response = String.getInput("Yes or No value",  "Are you sure you want to delete this user? Yes/No", True)
      if response == "Yes" or response == "yes":
        result = Contact.DeleteByID(ContactID)
        print(f"{result} has been successfully deleted.")
        Menu.Start()
      else:
        print("Delete Action Canceled by user")
    elif selectedAction == "2":
      response = String.getInput("Yes or No value", "Do you want to update the selected contact? Yes/No", True)
    elif selectedAction == "3":
      Menu.Start()

  def ContactsAction():
    selectedAction = String.getInput("value", "Select an action to execute: [1]View Contact Details [2]Return to Main Menu", False)
    if selectedAction == "1":
      ContactID = String.getInput("Contact ID",  "Enter the contact ID", True)
      Contact.SearchByID(ContactID)
      Menu.ContactAction(ContactID)
    elif selectedAction == "2":
      Menu.Start()

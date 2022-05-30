from StringClass import String
from DatabaseClass import Database
import datetime


class Contact:
  def Create():
    #We first collect the data of the new user using our String.getInput Class
    # String.getInput(textToDisplayToUserString, isFieldRequiredBoolean)
    print("Please follow the prompts below to complete the creation of your new contact. (required fields are marked with an *)")
    firstName       = String.getInput("First Name", "\nEnter First Name", True)
    middleName      = String.getInput("Middle Name", "\nEnter Middle Name", False)
    lastName        = String.getInput("Last Name", "\nplease enter the Last Name for", False)
    mobileNumber    = String.getInput("Mobile Number", "\nPlease Enter Mobile Number", True)
    workNumber      = String.getInput("Work Number", "\nPlease Enter Work Number", False)
    email           = String.getInput("Email", "\nPlease Enter Email Address", False)
    webURL          = String.getInput("URL", "\nPlease Enter URL", False)
    address         = String.getInput("Address", "\nPlease Enter Address", False)
    comment         = String.getInput("Comment", "\nPlease Enter Comment", False)
    statusID        = 1
    DateOfCreation  = datetime.datetime.now()

    #Then we insert Data into Database
    sql = "INSERT INTO ContactTable (FirstName, MiddleName, LastName, MobileNumber, WorkNumber, Email, WebURL, Address, Comment, StatusID, DateOfCreation) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    val = (firstName, middleName, lastName, mobileNumber, workNumber, email, webURL, address, comment, statusID, DateOfCreation)
    result = Database.Insert(sql, val)

    #Then We display record back to user on success
    Contact.SearchByID(result)

    print("\n\n" + firstName + " has been added to your Contact Book")

  def ShowAll():
    #Get All Data from Contacts
    #Display number of records found
    #Display  ID | FullName | MobileNumber on each line

    print("We read all contacts here")

  def SearchByID(ContactID):
    #Search specific record with ID
    """Display complete data
                ID:
                First Name:
                Middile Name:  
                LastName: 
                Mobile Number:
                Work Number:
                Email:
                Web URL:
                Address:
                Comment:
    """
    sql = "SELECT * FROM ContactTable WHERE ContactID = %s"
    val = (ContactID,)
    result = Database.Read(sql, val)
    #print(result)
    contact = result[0]
    # Result Example: (3, 'Edward', 'Sam', 'Mahama', '303203204234', '2342342334234234', 'There', 'here', 'around', 'ok', 1, datetime.date(2022, 2, 7), None, None)
    (contactID, firstName, middleName, lastName, mobileNumber, workNumber, email, webURL, address, comment, statusID, creationDate, modificationDate, DeletionDate) = contact
    print(f"""Contact Details for {contact[1]}:
    -------------------------------------
    ID:            | {contactID}       
    -------------------------------------
    First Name:    | {firstName}
    -------------------------------------
    Middile Name:  | {middleName}
    -------------------------------------
    LastName:      | {lastName}
    -------------------------------------
    Mobile Number: | {mobileNumber}
    -------------------------------------
    Work Number:   | {workNumber}
    -------------------------------------
    Email:         | {email}
    -------------------------------------
    Web URL:       | {webURL}
    -------------------------------------
    Address:       | {address}
    -------------------------------------
    Comment:       | {comment}
    -------------------------------------
    """)
  

  def SearchByValue(Value, sortingOrder):
    #Search and display all fields with provided value
    if sortingOrder == "1":
      sortingOrder = " ORDER BY ContactID"
    elif sortingOrder == "2":
      sortingOrder = " ORDER BY FirstName"
    elif sortingOrder == "3":
      sortingOrder = " ORDER BY MobileNumber"


    if Value == "":
      sql = "SELECT * FROM ContactTable" + sortingOrder
      result = Database.Read(sql, "")
    else:
      sql = "SELECT * FROM ContactTable WHERE %s IN (FirstName, MiddleName, LastName, MobileNumber, WorkNumber, Email, webURL, Address)" + sortingOrder
      val = (Value,)
      result = Database.Read(sql, val)

    contacts = result

    #totalContacts = contacts.count

    #Display  ID | FullName | MobileNumber on each line
    print(f"----------------------------------{len(result)} Result(s) Found--------------------------------")
    print(f"{String.evenSpacing(10, 'CONTACT ID')} | {String.evenSpacing(30, 'FULL NAME')} | MOBILE NUMBER ")
    for contact in contacts:
      print(f"""-------------------------------------------------------------------------------------
{String.evenSpacing(10, str(contact[0]))} | {String.evenSpacing(30, contact[1] + "" + contact[3])} | {contact[4]}""")

    print("-----------------------------------END-----------------------------------------------")
    

  def Update(ContactID):
    print("We update contact here")

  def DeleteByID(ContactID):
    sql = "DELETE FROM ContactTable WHERE ContactID = %s"
    val = (ContactID,)
    result = Database.Delete(sql, val)

    return result
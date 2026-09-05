#                Contact Book Program

contacts = {}
contacts_length = len(contacts)

while True:
    print("=" * 30)
    print("             MENU")
    print("=" * 30)
    print("             OPTIONS")
    print("1. Add")
    print("2. Search")
    print("3. Delete")
    print("4. Print all")
    print("5. Quit")
    print("=" * 30)
    
    option = int(input("Enter option to proceed :"))

    if option == 1:
        print("1")
        print("Adding a new contact : ")
        print(contacts)
        name = input("Enter name : ")
        
        # checking if name in contacts
        if name in list(contacts.keys()):
            print(f"{name} already exists in contact list")
            check = input("Do you want to overwrite it? (yes/no) ")
            # if no overwriting, break loop
            if check != "yes":
                print("Adding contact cancelled.")
                continue
            # if overwriting, proceed to update
            else:
                phone = input("Enter phone number : ")
                contacts[name] = phone
                continue
        else:
            # if name not in contacts, create name and number
            phone = input("Enter phone number : ")
            contacts[name] = phone
            contacts_length = len(contacts)
            print(f"Total contacts : {contacts_length}")
        
        continue

    
    elif option == 2:
        print("2")
        print("Searching for contact.")
        # using placeholder search value
        search = input("Enter name : ")
        # converting search key to lower case
        search_lower = search.lower()

        for name, phone in contacts.items():
            # checking if search_lower is in dictionary
            if search_lower not in contacts.keys():
                print(f"{search} not found.")
                break
            else:
                if search_lower == name:
                    print(f"{name} : {phone}")
                else:
                    continue
        continue


    elif option == 3:
        print("3")
        print("Delete a contact")
        to_del = input("Enter name of contact to delete: ")
        # using indexes in a list since delete function changes the dictionary size
        for name in list(contacts.keys()):
            if to_del in contacts.keys():
                # deleting only where index is equal to to_del input by user
                if to_del == name:
                    print(f"{name} deleted from contact list. ")
                    del contacts[name]
                    # checking dict length after deleting 
                    contacts_length = len(contacts)
                    break
                else:
                    continue
            else:
                print(f"{to_del} not found in contacts.")
                break   
        print(contacts)
        print(f"Total contacts : {contacts_length}")

        continue
        

    elif option == 4:
        print("4")
        print("Print all")
        # breaking the contacts dict into name and phone
        for name, phone in contacts.items():
            print(f"{name} : {phone}")
        continue


    elif option == 5:
        print("Goodbye.")
        break

    else: 
        print("invalid option! Try again")


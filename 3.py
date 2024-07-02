dictionary = {}

def add(key, value):
    dictionary[key] = value

def print_dict():
    for key in dictionary:
        print(key, dictionary[key])

while(1):
    print("""Enter the operation you want to perform as given below (Enter number corresponding to symbol)
    1. Add Contact to phonebook
    2. Print phonebook
    3. Print the phone number of a contact
    4. Delete a contact
    5. Exit
    """)
    choice = input("Enter your choice : ")
    if(choice == '1'):
        key = input("Enter name : ")
        value = input("Enter phone number : ")
        add(key, value)
    elif(choice == '2'):
        if len(dictionary) == 0:
            print("Phonebook is empty")
        else:
            print_dict()
    elif(choice == '3'):
        key = input("Enter name : ")
        if key in dictionary:
            print(key, dictionary[key])
        else:
            print("Contact not found")
    elif(choice == '4'):
        key = input("Enter name : ")
        if key in dictionary:
            del dictionary[key]
            print("Contact deleted")
        else:
            print("Contact not found")
    

    elif(choice == '5'):
        break
    else:
        print("Invalid choice")



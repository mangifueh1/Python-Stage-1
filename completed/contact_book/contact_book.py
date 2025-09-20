
db = 'contacts.txt'


def get_contacts():
    with open(db, 'r') as file:
        contacts = file.readlines()
    return contacts


contacts = get_contacts()


def main():
    print("\n*****Main Menu*****")
    print("' A ' to Add a contact")
    print("' V ' to View contact book")
    print("' S ' to Search for contact")
    print("' D ' to Delete a contact")
    print("' EXIT ' to Close Program")


def add_contact(name, phone):

    with open(db, 'a') as file:
        file.write(f"\n{name} : {phone}")

    print('Successfully Added')


def view_contacts():
    contacts = get_contacts()
    print("\nCurrent Contacts: ")
    for contact in contacts:
        print(contact)


def search_contact(name):
    contacts = get_contacts()
    for line in contacts:
        if str(name) in line:
            return line


def delete_contact(line):
    contacts = get_contacts()
    if line not in contacts:
        print('COntact not FOund'.upper())
    else:
        contacts.remove(line)
        print('Delete Successful')
        with open(db, 'w') as file:
            file.writelines(contacts)


def run_app():
    while True:
        main()
        command = input("\nSelect an Option: ".upper()).lower().strip()
        if command == "a":
            name = input("\nEnter Name: ")
            phone = input("Enter Phone Number: ")
            add_contact(name=name, phone=phone)

        elif command == "v":
            view_contacts()
            continue

        elif command == "s":
            name = input("\nEnter Name: ")
            result = search_contact(name)
            if result == None:
                print('\n Contact not found\n'.upper())
            else:
                print(result)
            continue

        elif command == "d":
            name = input("\nEnter Name: ")
            for line in contacts:
                if str(name) in line:
                    delete_contact(line)
            # continue

        elif command == "exit":
            print('\nClosing program\n')
            break
        else:
            print('\nEnter a valid option'.upper())
            continue


run_app()

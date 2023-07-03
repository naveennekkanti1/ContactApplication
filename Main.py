import os

# Function to create a contact
# Function to create a contact
def create_contact():
    name = input("Enter the contact's name: ")
    phone = input("Enter the contact's phone number: ")
    email = input("Enter the contact's email address: ")
    new_contact = f"{name},{phone},{email}\n"
    with open("Data/contacts.csv", "r") as file:
        contacts = file.readlines()
        for contact in contacts:
            contact_data = contact.strip().split(",")
            if contact_data[0].lower() == name.lower():
                print("Contact already exists.")
                return
    with open("Data/contacts.csv", "a") as file:
        file.write(new_contact)
    print("Contact created successfully.")

# Function to update a contact
def update_contact():
    name = input("Enter the contact's name to update: ")
    updated_contact = ""
    with open("Data/contacts.csv", "r") as file:
        contacts = file.readlines()
        for contact in contacts:
            contact_data = contact.strip().split(",")
            if contact_data[0].lower() == name.lower():
                new_phone = input("Enter the updated phone number: ")
                new_email = input("Enter the updated email address: ")
                updated_contact = f"{name},{new_phone},{new_email}\n"
            else:
                updated_contact = contact
    with open("Data/contacts.csv", "w") as file:
        file.writelines(updated_contact)
    print("Contact updated successfully.")

# Function to delete a contact
def delete_contact():
    name = input("Enter the contact's name to delete: ")
    updated_contacts = ""
    with open("Data/contacts.csv", "r") as file:
        contacts = file.readlines()
        for contact in contacts:
            contact_data = contact.strip().split(",")
            if contact_data[0].lower() != name.lower():
                updated_contacts += contact
    with open("Data/contacts.csv", "w") as file:
        file.writelines(updated_contacts)
    print("Contact deleted successfully.")

# Function to display all contacts
def display_all_contacts():
    with open("Data/contacts.csv", "r") as file:
        contacts = file.readlines()
        if not contacts:
            print("No contacts found.")
        else:
            for contact in contacts:
                contact_data = contact.strip().split(",")
                print(f"Name: {contact_data[0]}\nPhone: {contact_data[1]}\nEmail: {contact_data[2]}\n")

# Function to display a single contact
def display_single_contact():
    name = input("Enter the contact's name to display: ")
    with open("Data/contacts.csv", "r") as file:
        contacts = file.readlines()
        for contact in contacts:
            contact_data = contact.strip().split(",")
            if contact_data[0].lower() == name.lower():
                print(f"Name: {contact_data[0]}\nPhone: {contact_data[1]}\nEmail: {contact_data[2]}\n")
                return
        print("Contact not found.")

# Main program loop
def main():
    while True:
        print("##############################   Contact Application   #################################")
        print("1. Create Contact")
        print("2. Update Contact")
        print("3. Delete Contact")
        print("4. Display All Contacts")
        print("5. Display Single Contact")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            create_contact()
        elif choice == "2":
            update_contact()
        elif choice == "3":
            delete_contact()
        elif choice == "4":
            display_all_contacts()
        elif choice == "5":
            display_single_contact()
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

# Create a contacts.csv file if it doesn't exist
if not os.path.isfile("Data/contacts.csv"):
    open("Data/contacts.csv", "w").close()

# Start the application
main()

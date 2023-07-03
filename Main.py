import os
from tkinter import Tk, Label, Entry, Button, messagebox

# Function to create a contact
def create_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    new_contact = f"{name},{phone},{email}\n"
    with open("contacts.txt", "r") as file:
        contacts = file.readlines()
        for contact in contacts:
            contact_data = contact.strip().split(",")
            if contact_data[0].lower() == name.lower():
                messagebox.showinfo("Duplicate Contact", "Contact already exists.")
                return
    with open("contacts.txt", "a") as file:
        file.write(new_contact)
    messagebox.showinfo("Success", "Contact created successfully.")
    clear_entries()

# Function to clear the entry fields
def clear_entries():
    name_entry.delete(0, 'end')
    phone_entry.delete(0, 'end')
    email_entry.delete(0, 'end')

# Create the main window
window = Tk()
window.title("Contact Application")

# Create labels
name_label = Label(window, text="Name:")
name_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
phone_label = Label(window, text="Phone:")
phone_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
email_label = Label(window, text="Email:")
email_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")

# Create entry fields
name_entry = Entry(window, width=30)
name_entry.grid(row=0, column=1, padx=5, pady=5)
phone_entry = Entry(window, width=30)
phone_entry.grid(row=1, column=1, padx=5, pady=5)
email_entry = Entry(window, width=30)
email_entry.grid(row=2, column=1, padx=5, pady=5)

# Create buttons
create_button = Button(window, text="Create", command=create_contact)
create_button.grid(row=3, column=0, padx=5, pady=5, sticky="w")
clear_button = Button(window, text="Clear", command=clear_entries)
clear_button.grid(row=3, column=1, padx=5, pady=5, sticky="w")

# Start the GUI event loop
window.mainloop()

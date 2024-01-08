import sqlite3

class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        return f"{self.name}: {self.phone} | {self.email}"

class ContactManager:
    def __init__(self):
        self.contacts = []
        self.load_contacts_from_database()

    def add_contact(self, contact):
        self.contacts.append(contact)
        self.save_contacts_to_database()
        print(f"Contact '{contact.name}' added successfully!")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts found.")
        else:
            print("Contact List:")
            for contact in self.contacts:
                print(contact)

    def edit_contact(self, name, new_phone=None, new_email=None):
        contact = self.find_contact(name)
        if contact:
            print(f"Current details for {contact.name}: {contact}")
            contact.phone = new_phone if new_phone else contact.phone
            contact.email = new_email if new_email else contact.email
            self.save_contacts_to_database()
            print(f"Contact '{contact.name}' updated successfully!")
        else:
            print(f"Contact '{name}' not found.")

    def delete_contact(self, name):
        contact = self.find_contact(name)
        if contact:
            self.contacts.remove(contact)
            self.save_contacts_to_database()
            print(f"Contact '{contact.name}' deleted successfully!")
        else:
            print(f"Contact '{name}' not found.")

    def find_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                return contact
        return None

    def load_contacts_from_database(self):
        try:
            connection = sqlite3.connect("contacts.db")
            cursor = connection.cursor()
            cursor.execute("CREATE TABLE IF NOT EXISTS contacts (name TEXT, phone TEXT, email TEXT)")
            cursor.execute("SELECT * FROM contacts")
            rows = cursor.fetchall()
            self.contacts = [Contact(*row) for row in rows]
        except sqlite3.Error as e:
            print(f"Error loading contacts from the database: {e}")
        finally:
            if connection:
                connection.close()

    def save_contacts_to_database(self):
        try:
            connection = sqlite3.connect("contacts.db")
            cursor = connection.cursor()
            cursor.execute("DROP TABLE IF EXISTS contacts")
            cursor.execute("CREATE TABLE contacts (name TEXT, phone TEXT, email TEXT)")
            for contact in self.contacts:
                cursor.execute("INSERT INTO contacts VALUES (?, ?, ?)", (contact.name, contact.phone, contact.email))
            connection.commit()
        except sqlite3.Error as e:
            print(f"Error saving contacts to the database: {e}")
        finally:
            if connection:
                connection.close()

def main():
    contact_manager = ContactManager()

    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            name = input("Enter the contact's name: ")
            phone = input("Enter the contact's phone number: ")
            email = input("Enter the contact's email address: ")
            contact_manager.add_contact(Contact(name, phone, email))
        elif choice == "2":
            contact_manager.view_contacts()
        elif choice == "3":
            name = input("Enter the name of the contact to edit: ")
            new_phone = input("Enter the new phone number (press Enter to keep the current value): ")
            new_email = input("Enter the new email address (press Enter to keep the current value): ")
            contact_manager.edit_contact(name, new_phone, new_email)
        elif choice == "4":
            name = input("Enter the name of the contact to delete: ")
            contact_manager.delete_contact(name)
        elif choice == "5":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()

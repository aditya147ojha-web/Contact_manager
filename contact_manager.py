# Contact Management System
# Name: Aditya Ojha

import json
import re
from datetime import datetime
import csv

FILE_NAME = "contacts_data.json"


# ---------- VALIDATION ----------
def validate_phone(phone):
    digits = re.sub(r'\D', '', phone)
    if 10 <= len(digits) <= 15:
        return True, digits
    return False, None


def validate_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email)


# ---------- FILE OPERATIONS ----------
def load_contacts():
    try:
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    except:
        return {}


def save_contacts(contacts):
    with open(FILE_NAME, "w") as f:
        json.dump(contacts, f, indent=4)


# ---------- CRUD OPERATIONS ----------
def add_contact(contacts):
    name = input("Enter name: ").strip()

    if name in contacts:
        print("Contact already exists!")
        return

    while True:
        phone = input("Enter phone: ")
        valid, phone = validate_phone(phone)
        if valid:
            break
        print("Invalid phone!")

    email = input("Enter email (optional): ")
    if email and not validate_email(email):
        print("Invalid email!")
        email = ""

    address = input("Enter address: ")
    group = input("Enter group (Friends/Work/Family): ") or "Other"

    contacts[name] = {
        "phone": phone,
        "email": email,
        "address": address,
        "group": group,
        "updated": datetime.now().isoformat()
    }

    print("Contact added!")


def search_contact(contacts):
    key = input("Enter name to search: ").lower()
    found = False

    for name, info in contacts.items():
        if key in name.lower():
            print(f"\n{name}")
            print("Phone:", info["phone"])
            print("Email:", info["email"])
            print("Group:", info["group"])
            found = True

    if not found:
        print("No contact found")


def update_contact(contacts):
    name = input("Enter name to update: ")

    if name not in contacts:
        print("Not found!")
        return

    print("Leave blank to keep old value")

    phone = input("New phone: ")
    if phone:
        valid, phone = validate_phone(phone)
        if valid:
            contacts[name]["phone"] = phone

    email = input("New email: ")
    if email:
        if validate_email(email):
            contacts[name]["email"] = email

    contacts[name]["updated"] = datetime.now().isoformat()
    print("Updated!")


def delete_contact(contacts):
    name = input("Enter name to delete: ")

    if name in contacts:
        confirm = input("Are you sure? (y/n): ")
        if confirm == 'y':
            del contacts[name]
            print("Deleted!")
    else:
        print("Not found!")


def display_all(contacts):
    if not contacts:
        print("No contacts")
        return

    for name, info in contacts.items():
        print("\nName:", name)
        print("Phone:", info["phone"])
        print("Email:", info["email"])
        print("Group:", info["group"])


# ---------- EXTRA FEATURES ----------
def export_csv(contacts):
    with open("contacts.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Phone", "Email", "Group"])

        for name, info in contacts.items():
            writer.writerow([name, info["phone"], info["email"], info["group"]])

    print("Exported to contacts.csv")


def stats(contacts):
    print("\nTotal Contacts:", len(contacts))

    groups = {}
    for c in contacts.values():
        g = c["group"]
        groups[g] = groups.get(g, 0) + 1

    print("By Group:")
    for g, count in groups.items():
        print(g, ":", count)


# ---------- MENU ----------
def menu():
    contacts = load_contacts()

    while True:
        print("\n===== CONTACT MANAGER =====")
        print("1. Add")
        print("2. Search")
        print("3. Update")
        print("4. Delete")
        print("5. View All")
        print("6. Export CSV")
        print("7. Stats")
        print("8. Exit")

        choice = input("Choose: ")

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            search_contact(contacts)
        elif choice == '3':
            update_contact(contacts)
        elif choice == '4':
            delete_contact(contacts)
        elif choice == '5':
            display_all(contacts)
        elif choice == '6':
            export_csv(contacts)
        elif choice == '7':
            stats(contacts)
        elif choice == '8':
            save_contacts(contacts)
            print("Saved. Bye!")
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    menu()
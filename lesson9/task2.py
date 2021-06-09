# Extend Phonebook application
# Functionality of Phonebook application:
# Add new entries
# Search by first name
# Search by last name
# Search by full name
# Search by telephone number
# Search by city or state
# Delete a record for a given telephone number
# Update a record for a given telephone number
# An option to exit the program

# The first argument to the application should be the name of the phonebook.
# Application should load JSON data, if it is present in the folder with application
# else raise an error.
# After the user exits, all data should be saved to loaded JSON.

import json
import os
import sys


def add_new_contact():     # create new contact
    print("Insert new contact!")
    new_firstname = input("First name:")
    new_lastname = input("Last name:")
    new_city = input("City:")
    new_number = input("Phone number:")

    data_phonebook["phonebook_1"].append({
        "first_name": new_firstname,
        "last_name": new_lastname,
        "city": new_city,
        "number": new_number
    })
    print("Contact is created!")


def search_by_firstname():
    search_firstname = input("Insert the first name:").capitalize()
    for object in data_phonebook["phonebook_1"]:
        if search_firstname == object["first_name"]:
            print(f"Find: {object}")
    else:
        print("Cannot find the name!")


def search_by_lastname():
    search_lastname = input("Insert the last name:").capitalize()
    for name in data_phonebook["phonebook_1"]:
        if search_lastname == name["last_name"]:
            print(f"Find: {name}")
    else:
        print("Cannot find the name!")


def search_by_fullname():
    search_fullname = input("Insert full name:").capitalize()
    for name in data_phonebook["phonebook_1"]:
        if search_fullname == name["first_name"] + ' ' + name["last_name"]:
            print(f"Find: {name}")
    else:
        print("Cannot find the name!")


def search_by_number():
    search_number = input("Insert the phone number:")
    if search_number.isdigit() is False:
        print("The phone number must contain 10 numbers")
    else:
        for object_1 in data_phonebook["phonebook_1"]:
            if search_number == object_1["number"]:
                print(f"Find: {object_1}")
                break
        else:
            print("Cannot find the phone number")


def search_by_city():
    search_city = input("Insert the city:").capitalize()
    for name in data_phonebook["phonebook_1"]:
        if search_city == name["city"]:
            print(f"Find: {name}")
    else:

        print("Cannot find the city!")


def delete_a_record():
    delete_record = input("Insert the contact you want to delete:")
    for name in data_phonebook["phonebook_1"]:
        if delete_record == name["number"]:
            data_phonebook['phonebook_1'].remove(name)
    print("Contact deleted!")
    print_phonebook()


def update_a_record():
    update_record = input("Insert the number of contact you want to update:")
    change_firstname = input('New first name:')
    change_lastname = input('New last name:')
    change_city = input('New city:')
    change_number = input('New number:')

    for name in data_phonebook["phonebook_1"]:
        if update_record == name["number"]:
            name["first_name"] = change_firstname
            name["last_name"] = change_lastname
            name["city"] = change_city
            name["number"] = change_number
    print("Contact is update!")


def exit_func():
    with open(phone_book_filename, 'w') as file_1:
        json.dump(data_phonebook, file_1, ensure_ascii=False, indent=4)


def print_phonebook():
    print(data_phonebook)


def phonebook():
    select_option = 0
    while select_option != '9':
        select_option = input("""
        Select option:
        1 - create new contact
        2 - search by first name
        3 - search by second name
        4 - search by full name
        5 - search by phone number
        6 - search by city or state
        7 - delete a record for a given telephone number
        8 - update a record for a given telephone number
        9 - exit
        10 - show phonebook
        >
        """)
        if select_option == '1':
            add_new_contact()
        elif select_option == '2':
            search_by_firstname()
        elif select_option == '3':
            search_by_lastname()
        elif select_option == '4':
            search_by_fullname()
        elif select_option == '5':
            search_by_number()
        elif select_option == '6':
            search_by_city()
        elif select_option == '7':
            delete_a_record()
        elif select_option == '8':
            update_a_record()
        elif select_option == '9':
            exit_func()
        elif select_option == '10':
            print_phonebook()
        else:
            print("Insert number from 1 to 10:")


try:
    if len(sys.argv) < 2:
        raise OSError
    else:
        phone_book_filename = sys.argv[1].lower()
        if phone_book_filename.rfind(".json") == -1:
            phone_book_filename += ".json"
    if not os.path.isfile(phone_book_filename):
        raise OSError
    with open(phone_book_filename) as file:
        data = file.read()
        data_phonebook = json.loads(data)

    print(data_phonebook)
    phonebook()

except OSError as error_text:
    print('Cannot find phonebook!')

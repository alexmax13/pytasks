import json
import os
import sys


class PhoneBook:
    def __init__(self, phonebook):
        self.phonebook = phonebook

    def add_new_contact(self, new_firstname, new_lastname, new_city, new_number):
        self.phonebook["phonebook_1"].append({
            "first_name": new_firstname,
            "last_name": new_lastname,
            "city": new_city,
            "number": new_number
        })
        print("Contact is created!")
        return self.phonebook["phonebook_1"][-1]

    def search_by_firstname(self, first_name):
        counter = 0
        for contact in self.phonebook["phonebook_1"]:
            if first_name.capitalize() == contact["first_name"]:
                counter += 1
                return f"Find: {contact}"
        if counter < 1:
            print("Cannot find the name!")

    def search_by_lastname(self, last_name):
        counter = 0
        for contact in self.phonebook["phonebook_1"]:
            if last_name.capitalize() == contact["last_name"]:
                counter += 1
                return f"Found: {contact}"
        if counter < 1:
            print("Cannot find the name!")

    def search_by_fullname(self, full_name):
        counter = 0
        for name in self.phonebook["phonebook_1"]:
            if full_name == name["first_name"] + ' ' + name["last_name"]:
                counter += 1
                return f"Find: {name}"
        if counter < 1:
            print("Cannot find the name!")

    def search_by_number(self, number):
        counter = 0
        if number.isdigit() is False:
            print("The phone number must contain 10 numbers")
        else:
            for object_1 in self.phonebook["phonebook_1"]:
                if number == object_1["number"]:
                    counter += 1
                    return f"Find: {object_1}"
            if counter < 1:
                print("Cannot find the phone number")

    def search_by_city(self, city):
        counter = 0
        for name in self.phonebook["phonebook_1"]:
            if city.capitalize() == name["city"]:
                counter += 1
                return f"Find: {name}"
        if counter < 1:
            print("Cannot find the city!")

    def delete_a_record(self, number) -> None:
        for name in self.phonebook["phonebook_1"]:
            if number == name["number"]:
                data_phonebook['phonebook_1'].remove(name)
        print("Contact deleted!")
        print_phonebook()

    def update_a_record(self, number_to_update, change_firstname, change_lastname, change_city, change_number) -> None:
        for name in self.phonebook["phonebook_1"]:
            if number_to_update == name["number"]:
                name["first_name"] = change_firstname
                name["last_name"] = change_lastname
                name["city"] = change_city
                name["number"] = change_number
        print("Contact is update!")
        print_phonebook()

    def exit_func(self) -> None:
        with open(phone_book_filename, 'w') as file_1:
            json.dump(self.phonebook, file_1, ensure_ascii=False, indent=4)

    def print_phonebook(self):
        return self.phonebook

    @staticmethod
    def phonebook() -> None:
        select_option: str = " "
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

        print_phonebook()
        phonebook()

    @staticmethod
    def init_phonebook():
        # try:
            # if len(sys.argv) < 2:
            #     raise OSError
            # else:
            #     phone_book_filename = sys.argv[1].lower()
            #     if phone_book_filename.rfind(".json") == -1:
            #         phone_book_filename += ".json"
            # if not os.path.isfile(phone_book_filename):
            #     raise OSError
        with open("phonebook_1.json", "w") as file:
            data = file.read()
            data_phonebook: dict = json.loads(data)

        print(data_phonebook)

        # except OSError:
        #     print('Cannot find phonebook!')


if __name__ == "__main__":

    PhoneBook.init_phonebook()

    PhoneBook.phonebook()

    man = PhoneBook(data_phonebook)

    man.add_new_contact(input(), input(), input(), input())

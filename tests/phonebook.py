import json


class PhoneBook:
    def __init__(self):
        self.phonebook = {}
        self.phone_book_filename = "phonebook_1.json"
        self.phonebook_name = "phonebook_1"

    def add_new_contact(self, new_firstname, new_lastname, new_city, new_number):
        contact = {
            "first_name": new_firstname,
            "last_name": new_lastname,
            "city": new_city,
            "number": new_number
        }
        self.phonebook[self.phonebook_name].append(contact)
        print("Contact is created!")
        return contact

    def search_by_firstname(self, first_name):
        counter = 0
        for contact in self.phonebook[self.phonebook_name]:
            if first_name.capitalize() == contact["first_name"]:
                counter += 1
                print(f"Find: {contact}")
                return contact
        if counter < 1:
            print("Cannot find the name!")

    def search_by_lastname(self, last_name):
        counter = 0
        for contact in self.phonebook[self.phonebook_name]:
            if last_name.capitalize() == contact["last_name"]:
                counter += 1
                print(f"Found: {contact}")
                return contact
        if counter < 1:
            print("Cannot find the name!")

    def search_by_fullname(self, full_name):
        counter = 0
        for name in self.phonebook[self.phonebook_name]:
            f_name = name["first_name"] + ' ' + name["last_name"]
            if full_name.lower() == f_name.lower():
                counter += 1
                print(f"Find: {name}")
                return name
        if counter < 1:
            print("Cannot find the name!")

    def search_by_number(self, number):
        counter = 0
        if number.isdigit() is False:
            print("The phone number must contain 10 numbers")
        else:
            for object_1 in self.phonebook[self.phonebook_name]:
                if number == object_1["number"]:
                    counter += 1
                    print(f"Find: {object_1}")
                    return object_1
            if counter < 1:
                print("Cannot find the phone number")

    def search_by_city(self, city):
        counter = 0
        names = []
        for name in self.phonebook[self.phonebook_name]:
            if city.capitalize() == name["city"]:
                counter += 1
                names.append(name)
                print(f"Find: {name}")
        if counter < 1:
            print("Cannot find the city!")
        return names

    def delete_a_record(self, number) -> None:
        for name in self.phonebook[self.phonebook_name]:
            if number == name["number"]:
                self.phonebook[self.phonebook_name].remove(name)
        print("Contact deleted!")
        self.print_phonebook()

    def update_a_record(self, number_to_update, change_firstname, change_lastname, change_city, change_number) -> None:
        for name in self.phonebook[self.phonebook_name]:
            if number_to_update == name["number"]:
                name["first_name"] = change_firstname
                name["last_name"] = change_lastname
                name["city"] = change_city
                name["number"] = change_number
        print("Contact is update!")
        self.print_phonebook()

    def exit_func(self) -> None:
        with open(self.phone_book_filename, 'w') as file_1:
            json.dump(self.phonebook, file_1, ensure_ascii=False, indent=4)

    def print_phonebook(self):
        print(self.phonebook)

    def interface_phonebook(self) -> None:
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
                first_name = input("Insert first name:")
                last_name = input("Insert last name:")
                city = input("Insert city:")
                number = input("Insert number:")
                self.add_new_contact(first_name, last_name, city, number)

            elif select_option == '2':
                first_name = input("Insert first name:")
                self.search_by_firstname(first_name)

            elif select_option == '3':
                last_name = input("Insert last name:")
                self.search_by_lastname(last_name)

            elif select_option == '4':
                full_name = input("Insert full name:")
                self.search_by_fullname(full_name)

            elif select_option == '5':
                number = input("Insert number:")
                self.search_by_number(number)

            elif select_option == '6':
                city = input("Insert city:")
                self.search_by_city(city)

            elif select_option == '7':
                number = input("Insert number of contact you want to delete:")
                self.delete_a_record(number)

            elif select_option == '8':
                number_to_update = input("Insert number of contact you want to update:")
                first_name = input("Insert first name:")
                last_name = input("Insert last name:")
                city = input("Insert city:")
                number = input("Insert number:")
                self.update_a_record(number_to_update, first_name, last_name, city, number)

            elif select_option == '9':
                self.exit_func()
            elif select_option == '10':
                self.print_phonebook()
            else:
                print("Insert number from 1 to 10:")

    def init_phonebook(self):
        try:
            with open(self.phone_book_filename, "r") as file:
                data = file.read()
                self.phonebook: dict = json.loads(data)

            print(self.phonebook)

        except OSError as error:
            print(error)


if __name__ == "__main__":

    phonebook_1 = PhoneBook()

    phonebook_1.init_phonebook()

    phonebook_1.interface_phonebook()

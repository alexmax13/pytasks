from phonebook import PhoneBook
import json


class TestPhonebook:
    def setup(self):
        self.pb = PhoneBook()
        self.pb.init_phonebook()

    def test_add_new_contact(self):

        assert self.pb.add_new_contact("san", "maks", "rivne", "0456759087") == {
            "first_name": "san",
            "last_name": "maks",
            "city": "rivne",
            "number": "0456759087"
            }

    def test_search_by_city(self):

        city_to_test = "rivne"
        names = []
        for name in self.pb.phonebook[self.pb.phonebook_name]:
            if city_to_test.capitalize() == name["city"]:
                names.append(name)
        assert self.pb.search_by_city(city_to_test) == names

    def test_search_by_firstname(self):

        firstname_to_test = "san"
        names = []
        for name in self.pb.phonebook[self.pb.phonebook_name]:
            if firstname_to_test.capitalize() == name["first_name"]:
                names.append(name)

        assert [self.pb.search_by_firstname(firstname_to_test)] == names

    def test_search_by_number(self):
        number_to_test = "0932040787"
        assert self.pb.search_by_number(number_to_test) == {
            "first_name": "Karina",
            "last_name": "Alimi",
            "city": "Kyiv",
            "number": "0932040787"
            }

    def test_init_phonebook(self):

        with open("testphonebook.json", "r") as file:
            data = file.read()
            test_dict = json.loads(data)
        assert self.pb.init_phonebook() == test_dict

    def test_exit_func(self):
        with open("testphonebook.json", 'w') as file_write:
            json.dump(self.pb.phonebook, file_write, ensure_ascii=False, indent=4)

        with open("testphonebook.json", "r") as file_read:
            data = file_read.read()
            test_dict = json.loads(data)
        assert self.pb.exit_func() == test_dict

import phonebook

def generator():
    yield "name"
    yield "surname"
    yield "rivne"
    yield "+380694201337"
    return "fake text"


g = generator()


def fake_input(*args, **kwargs):
    return next(g)


def test_add_new_contact():

   # pb = phonebook()
   # pb.add("; drop table user", "surname", "rv", "102")
   # assert pb.search_by_name('test').number == 102

    #phonebook.input = fake_input_10

    phonebook.init_phonebook()

    phonebook.input = fake_input

    phonebook.add_new_contact()

    print(phonebook.data_phonebook)

    assert phonebook.data_phonebook["phonebook_1"][-1]['city'] == "rivne"

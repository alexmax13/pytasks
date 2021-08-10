def count_lines(filename):
    count = len(open(filename).readlines())
    print(f'Numbers of lines:{count}')


def count_chars(filename):
    count = len(open(filename).read())
    print(f'Numbers of chars:{count}')


def test(name):
    count_chars(name)
    count_lines(name)


# test('filename.txt')

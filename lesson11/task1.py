# Task 2

# Make a class structure in python representing people at school.
# Make a base class called Person, a class called Student, and another one called Teacher.
# Try to find as many methods and attributes as you can which belong to different classes,
# and keep in mind which are common and which are not.

class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def say_hello(self):
        print(f"Hello, my name is {self.name} and I’m {self.age} years old")

    def my_city(self):
        print(f'Hi, my name is {self.name} and i live in {self.city}')


class Teacher(Person):
    def __init__(self, name, age, city, work_experience):
        Person.__init__(self, name, age, city)
        self.work_experience = work_experience

    def experience_of_work(self):
        print(f'Teacher with name {self.name} has {self.work_experience} years of work experience.')

    def teach(self):
        print(f'{self.name} teaches student.')


class Student(Person):
    def __init__(self, name, age, city, study_year, average_grade):
        Person.__init__(self, name, age, city, )
        self.study_year = study_year
        self.average_grade = average_grade

    def stud_year(self):
        print(f'{self.name} is a {self.study_year}-year student')

    def study(self):
        print(f'{self.name} is student and he want higher grade!')

    def av_grade(self):
        print(f'Student {self.name} has average grade - {self.average_grade}')


# People
teach_1 = Teacher("Robert", 50, "Berlin", 10)
teach_2 = Teacher("Karl", 49, "Washington", 15)
stud_1 = Student("Daniel", 22, "London", 3, 3.8)
stud_2 = Student("Mark", 20, "Kiev", 2, 2.1)


# Person class
teach_2.say_hello()
teach_1.my_city()
stud_1.say_hello()
stud_2.my_city()

# Teacher class
teach_2.teach()
teach_1.experience_of_work()

# Student class
stud_1.av_grade()
stud_2.study()
stud_1.stud_year()

# Worker has a property 'boss', and its value must be an instance of Boss.
#
# You can reassign this value, but you should check whether the new value is Boss.
# Each Boss has a list of his own workers.
# You should implement a method that allows you to add workers to a Boss.
# You're not allowed to add instances of Boss class
# to workers list directly via access to attribute, use getters and setters instead!

class Boss:

    def __init__(self, id_: int, name: str, company: str):
        self.id = id_

        self.name = name

        self.company = company

        self.workers = []

    def get_workers(self):
        return self.workers

    def set_workers(self, worker):
        self.workers.append(worker)


class Worker:

    def __init__(self, id_: int, name: str, company: str, boss: Boss):
        self.id = id_

        self.name = name

        self.company = company

        self.boss = boss


Eugene = Boss(69, 'Eugene', 'GameDev')
Karina = Boss(9, 'Karina', 'Medicine')

San = Worker(8, 'San', 'Etsy', Eugene)
Val = Worker(1, 'Val', 'Etsy', Eugene)
Naz = Worker(1, 'Naz', 'BuildFactory', Karina)
Bob = Worker(1, 'Bob', 'Etsy', Karina)


Eugene.set_workers(San.name)
Eugene.set_workers(Val.name)
print(Eugene.get_workers())

Karina.set_workers(Naz.name)
Karina.set_workers(Bob.name)
print(Karina.get_workers())

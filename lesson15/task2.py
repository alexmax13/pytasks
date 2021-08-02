# Worker has a property 'boss', and its value must be an instance of Boss.
# You can reassign this value, but you should check whether the new value is Boss.
#
# Each Boss has a list of his own workers.
# You should implement a method that allows you to add workers to a Boss.
# You're not allowed to add instances of Boss class
# to workers list directly via access to attribute, use getters and setters instead!

class Boss:
    def __init__(self, id_: int, name: str, company: str):
        self.__id = id_
        self.name = name
        self.company = company
        self.__workers = []

    def add_new_worker(self, new_worker):
        if type(new_worker) == Worker and new_worker not in self.__workers:
            self.__workers.append(new_worker)

    @property
    def list_workers(self):
        return [worker.name for worker in self.__workers]

    def __str__(self):
        return self.name


class Worker:
    def __init__(self, id_: int, name: str, company: str, init_boss: Boss):
        self.id = id_
        self.name = name
        self.company = company
        self.boss = init_boss    # same as self.boss(boss) (setter)

    @property
    def boss(self):
        return self.__boss

    @boss.setter
    def boss(self, new_value):
        if type(new_value) == Boss:
            self.__boss = new_value
            self.__boss.add_new_worker(self)
        else:
            print("Not Boss")

    def __str__(self):
        return self.name


Eugene = Boss(69, 'Eugene', 'GameDev')
Karina = Boss(9, 'Karina', 'Medicine')

San = Worker(8, 'San', 'Etsy', Eugene)
Val = Worker(1, 'Val', 'Etsy', Eugene)
Naz = Worker(1, 'Naz', 'BuildFactory', Karina)
Bob = Worker(1, 'Bob', 'Etsy', Karina)


San.boss = Eugene
Val.boss = Eugene
print(Eugene.list_workers)

print(San.boss)

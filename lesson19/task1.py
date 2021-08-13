# Create your own class, which can behave like a built-in function `open`.
# Also, you need to extend its functionality with counter and logging.
# Pay special attention to the implementation of `__exit__` method,
# which has to cover all the requirements to context managers.
import datetime


class ContManager:
    counter = 1

    @staticmethod
    def now_time():
        return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    def __init__(self, file_name, mode):
        self.obj = open(file_name, mode)
        self.log = open("log.txt", mode='a')
        self.log.write(f"{ContManager.counter}. "
                       f"Open file {file_name} - {ContManager.now_time()}\n")
        ContManager.counter += 1

    def __enter__(self):
        return self.obj

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.obj.close()
        self.log.write(f"File {self.obj.name} closed"
                       f" - {ContManager.now_time()}\n")
        self.log.close()


with ContManager("file_1.txt", "a") as f_1:
    f_1.write('hello\n')

with ContManager("file_2.txt", "a") as f_2:
    f_2.write('world\n')

with ContManager("file_3.txt", "a") as f_3:
    file.write('hello world\n')


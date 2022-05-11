from abc import ABC, abstractmethod


class DownloadCommentsInterFace(ABC):
    def __init__(self):
        self.number = None

    @abstractmethod
    def launch(self, subreddits_list, folder):
        pass

    def get_name(self) -> str:
        return f'{type(self).__name__}{self.number}'

    def set_number(self, number):
        self.number = number


if __name__ == "__main__":
    print("Only for import")

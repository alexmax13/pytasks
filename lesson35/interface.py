from abc import ABC, abstractmethod


class DownloadCommentsInterFace(ABC):
    @abstractmethod
    def launch(self, subreddits_list, folder):
        pass


if __name__ == "__main__":
    print("Only for import")

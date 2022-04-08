from interface import DownloadCommentsInterFace
from thread import ThreadDownloader
from multiproc import MultiprocDownloader
from acyncio import AsyncDownloader
import os
import datetime


class ConcurrencyContest:

    def __init__(self) -> None:
        self.downloaders: list[DownloadCommentsInterFace] = []

    def add_downloader(self, downloader: DownloadCommentsInterFace) -> None:
        if issubclass(type(downloader), DownloadCommentsInterFace):
            self.downloaders.append(downloader)
        else:
            print("Wrong type instance")

    def run(self) -> None:

        cwd = os.getcwd()

        with open(f'{cwd}/subreddits.txt', 'r') as f:
            subreddits_list = f.read().splitlines()
        # subreddits_list = subreddits_list[:4]
        date = datetime.datetime.now().strftime('%d-%m-%y (%H-%M-%S)')
        folder = os.path.join(cwd, f'{date}')
        if not os.path.exists(folder):
            os.mkdir(folder)

        print("\u001b[31m[ 🏁 READY! STEADY! GO! 🏆 ]\u001b[0m")
        participant_list = {}
        for downloader in self.downloaders:
            participant_name = type(downloader).__name__
            downloader_folder = os.path.join(folder, f'{participant_name}')

            if not os.path.exists(downloader_folder):
                os.mkdir(downloader_folder)

            start = datetime.datetime.now()

            downloader.launch(subreddits_list, downloader_folder)

            total_time = (datetime.datetime.now() - start).total_seconds()
            participant_list[participant_name] = total_time

        for name, duration in participant_list.items():
            print(f"{name} finished for {duration}s")
        winner = min(participant_list, key=participant_list.get)
        print(f'{winner} is winner')


if __name__ == "__main__":

    contest = ConcurrencyContest()
    contest.add_downloader(ThreadDownloader())
    contest.add_downloader(MultiprocDownloader())
    contest.add_downloader(AsyncDownloader())

    contest.run()

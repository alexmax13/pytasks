import time
from interface import DownloadCommentsInterFace


class TestDownloader(DownloadCommentsInterFace):
    def __init__(self, duration):
        super().__init__()
        self.duration = duration

    def launch(self, subreddits_list, folder):
        time.sleep(self.duration)

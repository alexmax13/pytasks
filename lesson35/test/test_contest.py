from contest import ConcurrencyContest
from thread import ThreadDownloader
from multiproc import MultiprocDownloader
from acyncio import AsyncDownloader
from interface import DownloadCommentsInterFace
from test_class_downloader import TestDownloader


class TestContest:
    def setup(self):
        self.conts = ConcurrencyContest()
        self.test_acync = AsyncDownloader()
        self.test_thread = ThreadDownloader()
        self.test_multproc = MultiprocDownloader()
        self.test_downloader_2 = TestDownloader(1)
        self.test_downloader_5 = TestDownloader(2)
        self.test_downloader_10 = TestDownloader(3)
        self.downloaders_list = [self.test_downloader_2, self.test_downloader_5, self.test_downloader_10]
        self.subreddits_list = ["toyota", "ukraine", "Antiwork", "AmItheAsshole", "explainlikeimfive"]

    def test_add_downloader(self):

        for item in self.downloaders_list:
            self.conts.add_downloader(item)

        assert len(self.conts.downloaders) == len(self.downloaders_list)

        for downloader in self.conts.downloaders:
            assert issubclass(type(downloader), DownloadCommentsInterFace)

    def test_run(self):
        for downloader in self.downloaders_list:
            self.conts.add_downloader(downloader)

        winner = self.conts.run()
        assert winner == self.test_downloader_2


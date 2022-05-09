from contest import ConcurrencyContest
from thread import ThreadDownloader
from multiproc import MultiprocDownloader
from acyncio import AsyncDownloader
from interface import DownloadCommentsInterFace


class TestContest:
    def setup(self):
        self.conts = ConcurrencyContest()
        self.test_acync = AsyncDownloader()
        self.test_thread = ThreadDownloader()
        self.test_multproc = MultiprocDownloader()

    def test_add_downloader(self):

        downloaders_list = [self.test_acync, self.test_multproc, self.test_thread]
        for item in downloaders_list:
            self.conts.add_downloader(item)

        assert len(self.conts.downloaders) == len(downloaders_list)

        for downloader in self.conts.downloaders:
            assert issubclass(type(downloader), DownloadCommentsInterFace)

    def test_run(self):
        pass


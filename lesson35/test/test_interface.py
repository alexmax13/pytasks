import pytest
from thread import ThreadDownloader
from multiproc import MultiprocDownloader
from acyncio import AsyncDownloader
from interface import DownloadCommentsInterFace
import os


@pytest.mark.parametrize("downloader", [AsyncDownloader(), ThreadDownloader(), MultiprocDownloader()])
def test_downloader_launch(downloader: DownloadCommentsInterFace):

    cwd = os.getcwd()

    subreddits_list = ["toyota", "ukraine", "Antiwork", "AmItheAsshole", "explainlikeimfive"]

    folder = os.path.join(cwd, 'test_reddits')
    if not os.path.exists(folder):
        os.mkdir(folder)

    participant_name = type(downloader).__name__
    downloader_folder = os.path.join(folder, participant_name)
    if not os.path.exists(downloader_folder):
        os.mkdir(downloader_folder)

    downloader.launch(subreddits_list, downloader_folder)

    # folder exists
    assert os.path.exists(downloader_folder)

    # files not empty
    for sr in subreddits_list:
        with open(f'{downloader_folder}/{sr}.txt', 'r') as f:
            lines = f.read()
            assert "Author" in lines and "Comment" in lines and "Date" in lines

import threading
import requests
import concurrent.futures
import os
import datetime
import time
from interface import DownloadCommentsInterFace


class ThreadDownloader(DownloadCommentsInterFace):

    def __init__(self, session: requests.Session = None, timeout=.0):
        super().__init__()
        if not session:
            self.session = requests.Session()
            self.timeout = timeout
            self.folder = ''

    def get_data(self, url_, params):
        start_loop = datetime.datetime.now()
        while True:
            response = self.session.get(url_, params=params)
            if (datetime.datetime.now() - start_loop).total_seconds() > self.timeout:
                print(f"Timeout connection: {params['subreddit']}")
                return {}
            print(f"{threading.current_thread().name}: {params['subreddit']}-{response.status_code}")
            if response.status_code == 200:
                return response.json()
            time.sleep(2)

    def worker(self, subreddit):
        base_url = 'https://api.pushshift.io/reddit/comment/search/'
        params = {'subreddit': subreddit, "sort": "desc", "sort_type": "created_utc", "size": 5}
        data = self.get_data(base_url, params)

        with open(f"{self.folder}/{subreddit}.txt", "w", encoding='utf-8') as file:
            for i in data['data']:
                comment = 'Author: ' + i['author'] + '\n' \
                          + 'Comment: ' + i['body'] + '\n' \
                          + 'Date: ' + datetime.datetime.fromtimestamp(i['created_utc']).strftime(
                    '%Y-%m-%d %H:%M:%S') + '\n'
                file.write(comment + '\n')

    def launch(self, subreddits, folder):

        with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:
            self.timeout = len(subreddits) * 3
            self.folder = folder
            executor.map(self.worker, subreddits)


if __name__ == '__main__':
    cwd = os.getcwd()

    with open(f'{cwd}/subreddits.txt', 'r') as f:
        subreddits_list = f.read().splitlines()

    date = datetime.datetime.now().strftime('%d-%m-%y (%H-%M-%S)')
    folder_ = os.path.join(cwd, f'{date}')
    if not os.path.exists(folder_):
        os.mkdir(folder_)

    start = datetime.datetime.now()

    downloader = ThreadDownloader()
    downloader.launch(subreddits_list, folder_)

    print(datetime.datetime.now() - start)


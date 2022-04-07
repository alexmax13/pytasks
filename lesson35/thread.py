import threading
import requests
import concurrent.futures
import os
import datetime
import time


class ThreadDownloader:

    def __init__(self, session: requests.Session = None, cwd=os.getcwd(), folder=None, timeout=.0):
        if not session:
            self.session = requests.Session()
        self.cwd = cwd
        self.folder_ = folder
        self.timeout = timeout

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

        with open(f"{self.folder_}/{subreddit}.txt", "w", encoding='utf-8') as file:
            for i in data['data']:
                comment = 'Author: ' + i['author'] + '\n' \
                          + 'Comment: ' + i['body'] + '\n' \
                          + 'Date: ' + datetime.datetime.fromtimestamp(i['created_utc']).strftime(
                    '%Y-%m-%d %H:%M:%S') + '\n'
                file.write(comment + '\n')

    def launch(self):
        start = datetime.datetime.now()

        with open(f'{self.cwd}/subreddits.txt', 'r') as f:
            subreddits_list = f.read().splitlines()

        self.timeout = len(subreddits_list) * 3

        date = datetime.datetime.now().strftime('%d-%m-%y %H-%M-%S')
        self.folder_ = os.path.join(self.cwd, f'{date}')
        if not os.path.exists(self.folder_):
            os.mkdir(self.folder_)

        with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:
            executor.map(self.worker, subreddits_list)

        print(datetime.datetime.now() - start)


if __name__ == '__main__':

    downloader = ThreadDownloader()
    downloader.launch()

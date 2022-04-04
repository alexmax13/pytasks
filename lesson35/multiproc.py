import multiprocessing
import requests
import datetime
from multiprocessing import Pool
import os
import time

mp_session: requests.Session = None
mp_folder = None
mp_timeout = .0


class MultiprocDownloader:

    @staticmethod
    def init_process(folder, timeout_):
        global mp_session
        global mp_folder
        global mp_timeout
        mp_folder = folder
        mp_timeout = timeout_
        if not mp_session:
            mp_session = requests.Session()

    @staticmethod
    def get_data(url_, params):
        start_loop = datetime.datetime.now()
        while True:
            response = mp_session.get(url_, params=params)
            if (datetime.datetime.now() - start_loop).total_seconds() > mp_timeout:
                print(f"Timeout connection: {params['subreddit']}")
                return {}
            print(f"{multiprocessing.current_process().name}: {params['subreddit']}-{response.status_code}")
            if response.status_code == 200:
                return response.json()
            time.sleep(2)

    @staticmethod
    def worker(subreddit):
        base_url = 'https://api.pushshift.io/reddit/comment/search/'
        params = {'subreddit': subreddit, "sort": "desc", "sort_type": "created_utc", "size": 5}
        data = MultiprocDownloader.get_data(base_url, params)
        if 'data' not in data:
            print('Empty data')
            return
        with open(f"{mp_folder}/{subreddit}.txt", "w", encoding='utf-8') as file:
            for i in data['data']:
                comment = 'Author: ' + i['author'] + '\n' \
                          + 'Comment: ' + i['body'] + '\n' \
                          + 'Date: ' + datetime.datetime.fromtimestamp(i['created_utc']).strftime(
                    '%Y-%m-%d %H:%M:%S') + '\n'
                file.write(comment + '\n')

    def launch(self):
        start = datetime.datetime.now()
        cwd = os.getcwd()
        with open(f'{cwd}/subreddits.txt', 'r') as f:
            subreddits_list = f.read().splitlines()

        timeout = len(subreddits_list) * 3

        date = datetime.datetime.now().strftime('%d-%m-%y %H-%M-%S')
        folder_ = os.path.join(cwd, f'{date}')
        if not os.path.exists(folder_):
            os.mkdir(folder_)

        with Pool(initializer=MultiprocDownloader.init_process, initargs=(folder_, timeout)) as pool:
            pool.map(MultiprocDownloader.worker, subreddits_list)

        print(datetime.datetime.now() - start)


if __name__ == '__main__':

    l = MultiprocDownloader()
    l.launch()



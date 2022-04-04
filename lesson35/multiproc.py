import multiprocessing
import requests
import datetime
from multiprocessing import Pool
import os
import time

session: requests.Session = None
cwd = os.getcwd()


def set_session():
    global session
    if not session:
        session = requests.Session()


with open(f'{cwd}/subreddits.txt', 'r') as f:
    subreddits_list = f.read().splitlines()

timeout = len(subreddits_list) * 3

date = datetime.datetime.now().strftime('%d-%m-%y %H-%M-%S')
folder_ = os.path.join(cwd, f'{date}')
if not os.path.exists(folder_):
    os.mkdir(folder_)


def get_data(url_, params):
    start_loop = datetime.datetime.now()
    while True:
        response = session.get(url_, params=params)
        if (datetime.datetime.now() - start_loop).total_seconds() > timeout:
            print(f"Timeout connection: {params['subreddit']}")
            return {}
        print(f"{multiprocessing.current_process().name}: {params['subreddit']}-{response.status_code}")
        if response.status_code == 200:
            return response.json()
        time.sleep(2)


def worker(subreddit):
    base_url = 'https://api.pushshift.io/reddit/comment/search/'
    params = {'subreddit': subreddit, "sort": "desc", "sort_type": "created_utc", "size": 5}
    data = get_data(base_url, params)
    if 'data' not in data:
        print('Empty data')
        return
    with open(f"{folder_}/{subreddit}.txt", "w", encoding='utf-8') as file:
        for i in data['data']:
            comment = 'Author: ' + i['author'] + '\n' \
                      + 'Comment: ' + i['body'] + '\n' \
                      + 'Date: ' + datetime.datetime.fromtimestamp(i['created_utc']).strftime(
                '%Y-%m-%d %H:%M:%S') + '\n'
            file.write(comment + '\n')


if __name__ == '__main__':

    start = datetime.datetime.now()

    with Pool(initializer=set_session) as pool:
        pool.map(worker, subreddits_list)

    print(datetime.datetime.now() - start)
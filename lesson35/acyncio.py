import asyncio
import aiohttp
import aiofiles
import os
import datetime
from interface import DownloadCommentsInterFace


class AsyncDownloader(DownloadCommentsInterFace):

    def __init__(self):
        super().__init__()
        self.timeout = .0
        self.folder = ''

    async def get_data(self, url_, params, session):
        start_loop = datetime.datetime.now()
        while True:
            try:
                response = await session.get(url_, params=params, ssl=False)
            except:
                print(f"async GET error occurred: {params['subreddit']}")
            if (datetime.datetime.now() - start_loop).total_seconds() > self.timeout:
                print(f"Timeout connection: {params['subreddit']}")
                return {}
            if response.status == 200:
                print(f"{params['subreddit']}: {response.status}")
                return await response.json()
            await asyncio.sleep(2)

    async def worker(self, subreddit, session):
        base_url = 'https://api.pushshift.io/reddit/comment/search/'
        params = {'subreddit': subreddit, "sort": "desc", "sort_type": "created_utc", "size": 5}
        data = await self.get_data(base_url, params, session)

        async with aiofiles.open(f"{self.folder}/{subreddit}.txt", "w", encoding='utf-8') as file:
            for i in data['data']:
                comment = 'Author: ' + i['author'] + '\n' \
                          + 'Comment: ' + i['body'] + '\n' \
                          + 'Date: ' + datetime.datetime.fromtimestamp(i['created_utc']).strftime(
                    '%Y-%m-%d %H:%M:%S') + '\n'
                await file.write(comment + '\n')

    def launch(self, subreddits, folder):
        self.timeout = len(subreddits) * 3
        self.folder = folder
        asyncio.run(self.main(subreddits))

    async def main(self, subreddits):
        async with aiohttp.ClientSession() as session:
            tasks = []
            for subreddit in subreddits:
                tasks.append(self.worker(subreddit, session))
            await asyncio.gather(*tasks)


if __name__ == '__main__':

    cwd = os.getcwd()

    date = datetime.datetime.now().strftime('%d-%m-%y (%H-%M-%S)')
    folder_ = os.path.join(cwd, f'{date}')
    if not os.path.exists(folder_):
        os.mkdir(folder_)

    with open(f'{cwd}/subreddits.txt', 'r') as f:
        subreddits_list = f.read().splitlines()

    start = datetime.datetime.now()

    downloader = AsyncDownloader()
    downloader.launch(subreddits_list, folder_)

    print(datetime.datetime.now() - start)


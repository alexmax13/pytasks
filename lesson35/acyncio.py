import asyncio
import aiohttp
import aiofiles
import os
import datetime


class AsyncDownloader:

    def __init__(self, cwd=os.getcwd(), folder=None, timeout=.0):
        self.cwd = cwd
        self.folder_ = folder
        self.timeout = timeout

    async def get_data(self, url_, params, session):
        start_loop = datetime.datetime.now()
        while True:
            response = await session.get(url_, params=params, ssl=False)
            if (datetime.datetime.now() - start_loop).total_seconds() > self.timeout:
                print(f"Timeout connection: {params['subreddit']}")
                return {}
            if response.status == 200:
                return await response.json()
            await asyncio.sleep(2)

    async def worker(self, subreddit, session):
        base_url = 'https://api.pushshift.io/reddit/comment/search/'
        params = {'subreddit': subreddit, "sort": "desc", "sort_type": "created_utc", "size": 5}
        data = await self.get_data(base_url, params, session)

        async with aiofiles.open(f"{self.folder_}/{subreddit}.txt", "w", encoding='utf-8') as file:
            for i in data['data']:
                comment = 'Author: ' + i['author'] + '\n' \
                          + 'Comment: ' + i['body'] + '\n' \
                          + 'Date: ' + datetime.datetime.fromtimestamp(i['created_utc']).strftime(
                    '%Y-%m-%d %H:%M:%S') + '\n'
                await file.write(comment + '\n')

    def launch(self):
        start = datetime.datetime.now()

        date = datetime.datetime.now().strftime('%d-%m-%y %H-%M-%S')
        self.folder_ = os.path.join(self.cwd, f'{date}')
        if not os.path.exists(self.folder_):
            os.mkdir(self.folder_)

        # asyncio.get_event_loop().run_until_complete(self.main())
        asyncio.run(self.main())

        print(datetime.datetime.now() - start)

    async def main(self):
        with open(f'{self.cwd}/subreddits.txt', 'r') as f:
            subreddits_list = f.read().splitlines()

        self.timeout = len(subreddits_list) * 3

        async with aiohttp.ClientSession() as session:
            tasks = []
            for subreddit in subreddits_list:
                tasks.append(self.worker(subreddit, session))
            await asyncio.gather(*tasks)


if __name__ == '__main__':

    downloader = AsyncDownloader()
    downloader.launch()


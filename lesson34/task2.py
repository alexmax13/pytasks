import requests
import datetime


def get_data(url_, parameter):
    response = requests.get(url_, parameter)
    print(response.url)
    return response.json()


base_url = 'https://api.pushshift.io/reddit/comment/search/'
params = {"subreddit": "cockatiel", "sort": "desc",
          "sort_type": "created_utc", "size": 5}

data = get_data(base_url, params)


with open("comments.txt", "w") as file:
    for i in data['data']:
        comment = 'Author: ' + i['author'] + '\n'\
                    + 'Comment: ' + i['body'] + '\n'\
                    + 'Date: ' + datetime.datetime.fromtimestamp(i['created_utc']).strftime('%Y-%m-%d %H:%M:%S') + '\n'
        file.write(comment + '\n')

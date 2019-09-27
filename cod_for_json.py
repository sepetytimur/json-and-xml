import json
from pprint import pprint
import operator

with open('jsonbase.json', encoding='utf-8') as date:
    json_news = json.load(date)

    dict = {}
    for news in json_news['rss']['channel']['items']:
        words = news['description'].split(' ')

        for word in words:
            if len(word) <= 6:
                continue

            if word in dict:
                dict[word] += 1
            else:
                dict[word] = 1
    sorted_x = sorted(dict.items(), key=operator.itemgetter(1))
    print(sorted_x[-10:])

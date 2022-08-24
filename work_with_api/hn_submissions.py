from operator import itemgetter

import requests
import json

# Make an api call, and store the response.
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print("Status code: {}".format(r.status_code))

# Process information about each submission
submission_ids = r.json()
print("\nNumber of Top Stories: {}".format(len(submission_ids)))
submission_dicts = []
for submission_id in submission_ids[:30]:
    url = 'https://hacker-news.firebaseio.com/v0/item/{}.json' \
        .format(submission_id)
    r = requests.get(url)
    print("ID: {}\tStatus code: {}".format(submission_id, r.status_code))
    response_dict = r.json()

    # try block for Error handling for no comments on an article
    # descendants key is added with value of 0
    try:
        response_dict['descendants']
    except KeyError:
        response_dict['descendants'] = 0

    # Build a dictionary for each article.
    submission_dict = {
        'title': response_dict['title'],
        'hn_link': "http://news.ycombinator.com/item?id={}"
            .format(submission_id),
        'comments': response_dict['descendants']
,
    }
    submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key=itemgetter('comments'),
                          reverse=True)

for submission_dict in submission_dicts:
    print("\nTitle: {}".format(submission_dict['title']))
    print("Discussion link: {}".format(submission_dict['hn_link']))
    print("Comments: {}".format(submission_dict['comments']))


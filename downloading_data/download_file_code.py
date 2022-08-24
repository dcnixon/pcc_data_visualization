import requests


def is_downloadable(url):
    rs = requests.get(url, allow_redirects=True)
    content_length = rs.headers.get('content-length', None)
    if content_length and content_length > 2e8: # 200 mb approx
        return False
    else:
        return True

# Get the link or url
url = 'https://www.facebook.com/favicon.ico'
r = requests.get(url, allow_redirects=True)

print(r.headers.get('content-type'))
print(is_downloadable(url))
# save the file as facebook.ico in the data folder
# open('data/facebook.ico', 'wb').write(r.content)


print(is_downloadable('https://www.youtube.com/watch?v=xCglV_dqFGI'))
print(is_downloadable('https://www.facebook.com/favicon.ico'))



import requests
import re


def getFilename_fromCd(cd):
    """
    Get filename from content-disposition
    """
    if not cd:
        return None
    fname = re.findall('filename=(.+)', cd)
    if len(fname) == 0:
        return None
    return fname[0]


url = 'http://google.com/favicon.ico'
r = requests.get(url, allow_redirects=True)
filename = getFilename_fromCd(r.headers.get('content-encoding'))
print(r.headers.get('content-type'))
print()
print(filename)
for i in r.headers:
    print(i)


url = "http://www.computersolution.tech/wp-content/uploads/2016/05/tutorialspoint-logo.png"
if url.find('/'):
    print(url.rsplit('/', 1)[1])

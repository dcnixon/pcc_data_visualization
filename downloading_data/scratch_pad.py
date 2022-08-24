import requests
import json

url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_hour.geojson"

r = requests.get(url, allow_redirects=True)
my_bytes = r.content
print(my_bytes)

print('- ' * 20)

for chunk in r.iter_content(chunk_size=128):
    print(chunk)

print('- ' * 20)
my_json = my_bytes.decode('utf8').replace("'", '"')
print(my_json)
print('- ' * 20)

data = json.loads(my_json)
s = json.dumps(data, indent=4, sort_keys=True)
print(s)

def bytes_to_json(bytes):
    my_json = bytes.decode('utf8').replace("'", '"')
    pretty_json = json.dumps(json.loads(my_json), indent=4, sort_keys=True)
    return pretty_json

print('*' * 40)
print(bytes_to_json(my_bytes) == s)

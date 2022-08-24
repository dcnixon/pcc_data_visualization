import json
import datetime
from eq_get_data import RecentQuakes

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

# filename = 'data/eq_data_20210129_1_month.json'
# with open(filename) as f:
#     all_eq_data = json.load(f)

# Use the class RecentQuakes to access the data without needing to save a file
all_eq_data = RecentQuakes('1.0', 'day').feed_data()

all_eq_dicts = all_eq_data['features']
file_title = all_eq_data['metadata']['title']
raw_date = all_eq_data['metadata']['generated'] / 1000
print(raw_date)
print_date = datetime.datetime.fromtimestamp(raw_date).strftime('%Y-%B-%d %H:%M')
print(print_date)

mags, lons, lats, hover_texts = [], [], [], []
for eq_dict in all_eq_dicts:
    mags.append(eq_dict['properties']['mag'])
    lons.append(eq_dict['geometry']['coordinates'][0])
    lats.append(eq_dict['geometry']['coordinates'][1])
    hover_texts.append(eq_dict['properties']['title'])

# Map the earthquakes
data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': hover_texts,
    'marker': {
        'size': [5 * mag for mag in mags],
        'color': mags,
        'colorscale': 'Viridis',
        'reversescale': True,
        'colorbar': {'title': 'Magnitude'}
    },
}]

my_layout = Layout(title="{} \t Data from: {}".format(file_title, print_date))

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_earthquakes.html')

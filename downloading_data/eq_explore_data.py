from eq_get_data import RecentQuakes
import json

# Explore the structure of the data
# filename = 'data/eq_data_20210129_1_month.json'
# with open(filename) as f:
#     all_eq_data = json.load(f)
#
# readable_file = 'data/readable_eq_20210129_data.json'
# with open(readable_file, 'w') as write_file:
#     json.dump(all_eq_data, write_file, indent=4)

# all_eq_dicts = all_eq_data['features']
# print(len(all_eq_dicts))
eq_data = RecentQuakes('all', 'day').feed_data()
# print(eq_data)
print(len(eq_data))
all_eq_dicts = eq_data['features']
print(len(all_eq_dicts))

mags, lons, lats = [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag'],
    lon = eq_dict['geometry']['coordinates'][0],
    lat = eq_dict['geometry']['coordinates'][1],
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)

if __name__ == '__main__':
    print(mags[:10])
    print(lons[:5])
    print(lats[:5])
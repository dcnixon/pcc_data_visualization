import csv
import matplotlib.pyplot as plt
from datetime import datetime

# filename = 'data/sitka_weather_2018_simple.csv'
filename = 'data/death_valley_2018_simple.csv'
with open(filename) as f:

    reader = csv.reader(f)
    header_row = next(reader)

    # show the header positions
    headers = [(index, column_header) for index, column_header in enumerate(header_row)]
    for index, column_header in headers:
        print(index, column_header)
        if column_header == "TMAX":
            high_index = index
        if column_header == "TMIN":
            low_index = index
        if column_header == "NAME":
            name_index = index


    # Get high temperatures from this file
    dates, highs, lows = [], [], []

    for row in reader:
        row_date = datetime.strptime(row[2], '%Y-%m-%d')

        station_names = []
        if len(station_names) == 0:
            station_name = row[name_index]
        try:
            high = int(row[high_index])
            low = int(row[low_index])
        except ValueError:
            print("Missing data for {}".format(row_date))
        else:
            dates.append(row_date)
            station_names.append(station_name)
            highs.append(high)
            lows.append(low)
print((station_names))


# Plot the high and low temperatures.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Format plot.
title = "Daily high and low temperatures - 2018\n {}".format(station_names[0])
plt.title(title, fontsize=20)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel('Temperature (F)', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()

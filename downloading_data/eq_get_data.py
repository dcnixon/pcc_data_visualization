# Instead of downloading the data to a json file  and move it into our directory
# feed_data method reads directly from the website without saving to a file
# TODO use an API query to access the data instead of referencing webpage feeds
# main site is https://earthquake.usgs.gov/earthquakes/feed/v1.0/geojson.php
# 1 month feed is https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/1.0_month.geojson

import json
import requests
from datetime import datetime

today = datetime.today().strftime('%Y%m%d')
timestamp = datetime.today().strftime('%Y-%m-%d-%H:%M:%S')


class RecentQuakes:
    """Simple class to define the timeframe and magnitude of recent
    contain recent data on earthquakes in the format to get data from
    https://earthquake.usgs.gov/earthquakes/feed/v1.0/geojson.php"""

    def __init__(self, magnitude='1.0', timeframe='month'):

        self.magnitude = magnitude
        self.timeframe = timeframe
        self.url = 'https://earthquake.usgs.gov/earthquakes' \
                   '/feed/v1.0/summary/{0}_{1}.geojson' \
            .format(magnitude, timeframe)
        # TODO eq_data folder must already exist for the code to work
        self.filename = 'eq_data/{0}_{1}_{2}.json' \
            .format(magnitude, timeframe, today)
        self.log = 'eq_data/eq_dl_log.txt' \
            .format(magnitude, timeframe, today)
        self.r = requests.get(self.url, allow_redirects=True)
        self.content_length = self.r.headers.get('content-length')

    def log_dl(self, args):
        """Method to write steps of download attempts to a log file
        prints used during testing/dev were shifted to this method"""
        with open(self.log, 'a') as log:
            print(timestamp, self.magnitude, self.timeframe, args,
                  sep='\t', file=log)

    def error_checks(self):
        """Check the response content length to determine request was good
        The headers.get('content-length') proved unreliable as larger data
        was sometimes missing this header

        Using len(self.r.content) we see that:
        a bad request (poor mag/timeframe values) returns 18,
        an empty response (no data for time and magnitude is approx 260
        and a response with one record is 1719
        """
        # print("checking for errors")                        # testing print
        # print( self.filename, len(self.r.content), self.content_length, sep='\t')     # testing print
        if len(self.r.content) > 275:
            # print("len(self.r.content) is greater than 250")    # testing print
            return True
        elif not self.content_length:
            # print("content length is none")                     # testing print
            self.log_dl("{} - check that the timeframe and magnitude is valid"
                        .format(self.r.content.decode('ascii', 'ignore')))
            return False
        # Check the response content length -
        # feeds with no data return length of approx 260
        elif 275 > len(self.r.content):
            # print("len(self.r.content) is less than 250")       # testing print
            self.log_dl("No earthquake data for magnitude '{0}' "
                        "and timeframe '{1}', "
                        "try a lower magnitude or longer timeframe"
                        .format(self.magnitude, self.timeframe))
            return False
        else:
            return True

    def download_data(self):
        """Method to download Earthquake data from the USGS site and
        save as json file"""
        self.log_dl("Attempting to download from {}".format(self.url))
        # print("self.error_checks() returns: ", self.error_checks())
        if self.error_checks():
            self.log_dl("Download successful, saving data as {}"
                        .format(self.filename))
            with open(self.filename, 'wb') as fd:
                for chunk in self.r.iter_content(chunk_size=128):
                    fd.write(chunk)

    def feed_data(self):
        """Method to access Earthquake data without saving the data to file"""
        if self.error_checks():
            self.log_dl("Feed data accessed from {}".format(self.url))
            content = self.r.content
            # print("content type is", type(content))     # diagnostic print
            # print("content length is", len(content))    # diagnostic print
            for chunk in self.r.iter_content(chunk_size=len(content)):
                # print("chunk prints as: ", chunk)       # diagnostic print
                data = bytes_to_json(chunk)
                # print("data prints as: ", data)       # diagnostic print
            loaded_data = json.loads(data)
            self.log_dl("Data feed load successful")
            return loaded_data


def bytes_to_json(bytes):
    """A function to convert objects from bytes to neatly formatted json"""
    my_json = bytes.decode('utf8', 'ignore')
    pretty_json = json.dumps(json.loads(my_json), indent=4, sort_keys=True)
    return pretty_json


# The magnitudes and times used by earthquake.usgs.gov/earthquakes/feed
valid_magnitudes = ['significant', '1.0', '2.5', '4.5', 'all']
valid_timeframes = ['hour', 'day', 'month']

# Download the data for all the valid earthquake instances
# for magnitude in valid_magnitudes:
#     for timeframe in valid_timeframes:
#         current_eq = Recent_Earthquakes(magnitude, timeframe)
#         current_eq.download_data()


# Testing
if __name__ == '__main__':
    RecentQuakes('2.0', 'friday').download_data() # test no page
    RecentQuakes('significant', 'hour').download_data() # test no data - currently passing to print
    RecentQuakes('2.5', 'hour').download_data()         # test
    RecentQuakes('4.5', 'hour').download_data()         # test
    RecentQuakes('4.5', 'day').download_data()          # test one record
    RecentQuakes('1.0', 'month').feed_data()            # test larger data
    # print("month_1.0 data: ",
    #       RecentQuakes('1.0', 'month').feed_data())     # test larger data

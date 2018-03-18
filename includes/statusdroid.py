import json
import urllib.request
import logging


class statusdroid:

    def __init__(self, link):
        self.regions = ['global', 'asia', 'europe', 'usa']
        self.link = link
        self.region = 'europe'
        self.get_guid()

    def get_guid(self):
        self.guid = self.link.split('/')[-1]

    def get_average_response_time(self):
        tmp_reg = self.regions
        tmp_reg.remove(self.region)
        for i in [self.region] + tmp_reg:
            data = urllib.request.urlopen(
                'https://www.statusdroid.com/api/statistics/response-time/' +
                '?range_hours=24&user_website_guid=' +
                self.guid + '&region=' + i
            ).read().decode('utf-8')
            if len(data) != 2:
                break
            else:
                logging.warning('No results in ' + i + ', switching regions!')
                self.region = i
        data = json.loads(data)
        return sum([i[1] for i in data]) / len(data)

    def get_intensity_to_minute(self):
        return (60 * 1000) / self.get_average_response_time()

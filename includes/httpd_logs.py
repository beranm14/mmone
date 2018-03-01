import re
import time


class httpd_logs:

    def __init__(self, path_to_log):
        self.path_to_log = path_to_log

    def get_hour_to_minute_count(self):
        regex = re.compile(
            time.strftime("%d") +
            '/' +
            time.strftime("%b") +
            '/' +
            time.strftime("%Y") +
            ':' +
            time.strftime("%H")
        )
        results = []
        with open(self.path_to_log) as f:
            for line in f:
                results.append(
                    regex.search(line)
                )
        return len(results) / 60

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
        results_count = 0
        with open(self.path_to_log) as f:
            for line in f:
                match_reg = regex.search(line)
                if match_reg is not None:
                    results_count += 1
        return results_count / 60

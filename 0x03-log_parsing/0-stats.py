#!/usr/bin/python3
""" reads stdin line by line and computes metrics
"""
import sys
import re

fsize = 0
stats = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}


def output_stats():
    """ Displays the stats gattered from the stdin
    """
    print(f"File size: {fsize}")
    for key in stats.keys():
        print(f"{key}: {stats[key]}")


if __name__ == "__main__":
    line_num = 0

    try:
        for line in sys.stdin:
            print(line)
            fp = (
                r'\s*(?P<ip>\S+)\s*',
                r'\s*\[(?P<date>\d+\-\d+\-\d+ \d+:\d+:\d+\.\d+)\]',
                r'\s*"(?P<request>[^"]*)"\s*',
                r'\s*(?P<status_code>\S+)',
                r'\s*(?P<file_size>\d+)'
            )
            info = {
                'status_code': 0,
                'file_size': 0,
            }
            log_fmt = '{}\\-{}{}{}{}\\s*'.format(
                    fp[0], fp[1], fp[2], fp[3], fp[4])
            resp_match = re.fullmatch(log_fmt, line)
            if resp_match is not None:
                status_code = resp_match.group('status_code')
                file_size = int(resp_match.group('file_size'))
                info['status_code'] = status_code
                info['file_size'] = file_size

                fsize += file_size
                stats[f'{status_code}'] += 1

            line_num += 1
            if line_num % 10 == 0:
                output_stats()
    except (KeyboardInterrupt, EOFError):
        output_stats()

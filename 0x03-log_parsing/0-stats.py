#!/usr/bin/python3
"""This module contains the solution to the log_parsing interview.
"""
import sys

if __name__ == '__main__':
    try:
        count = 0
        store = {
            'File size': 0
        }
        while True:
            for line in sys.stdin:
                if count == 10:
                    count = 0
                    line_to_print = ''
                    for key, value in sorted(store.items()):
                        line_to_print += key + ': ' + str(value) + '\n'
                    print(line_to_print, end="")
                # strip line
                parsed = line.split()
                store['File size'] += int(parsed[-1])
                if parsed[-2] in store:
                    store[parsed[-2]] += 1
                else:
                    store[parsed[-2]] = 1
                count += 1
    except KeyboardInterrupt:
        line_to_print = ''
        for key, value in sorted(store.items()):
            line_to_print += key + ': ' + str(value) + '\n'
        print(line_to_print, end="")

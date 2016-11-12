#python 2.7 and python 3.5

import sys
import time

def progressbar(it, size):
    count = len(it) + start

    def _show(_i):
        x = int(size * (_i + start) / count)
        sys.stdout.write("[%s%s] %i %s\r" % ("#" * x, " " * (size - x), _i + start, '%'))
        sys.stdout.flush()

    _show(0)
    for i, item in enumerate(it):
        yield item
        _show(i + 1)
    sys.stdout.write("\n")
    sys.stdout.flush()

input_start = input("Enter State: ")
start = int(input_start)

for i in progressbar(range(100-start), 10):
    time.sleep(0.1)
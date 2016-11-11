import sys
import time

def progressbar(it, size=10):
    count = len(it)

    def _show(_i):
        x = int(size * _i / count)
        sys.stdout.write("[%s%s] %i %s\r" % ("#" * x, " " * (size - x), _i, '%'))
        sys.stdout.flush()

    _show(0)
    for i, item in enumerate(it):
        yield item
        _show(i + 1)
    sys.stdout.write("\n")
    sys.stdout.flush()

for i in progressbar(range(100), 10):
    time.sleep(0.1)
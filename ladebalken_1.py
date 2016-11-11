import time
import sys

def ladebalken():
    steps = 10
    for i in range(100):
        time.sleep(0.1)
        if i % steps == 0:
            print '\b#',
            sys.stdout.flush()
    print '\b] 100 %',

print '[          ]',
print '\b'*12,
sys.stdout.flush()
ladebalken()

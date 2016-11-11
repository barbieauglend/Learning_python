import random

bereich = input("Enter MAX: ")
coord = int (bereich)

zuf_x = random.randint(0,coord)
zuf_y = random.randint(0,coord)

final=""

for x in range(coord):
    if x != zuf_x:
        print("#"*coord)
    else:
        for y in range(coord):
            if y != zuf_y:
                final = final + "#"
            else:
                final = final + "*"
        print(final)

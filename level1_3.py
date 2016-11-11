import random

input_y = input("Enter WIDTH: ")
input_x = input("Enter HEIGHT: ")
input_rand = input("Enter RANDOM: ")

coord_x = int(input_x)
coord_y = int(input_y)
input_random = int(input_rand)

if input_random > coord_x*coord_y:
    raise Exception("I can't do that, Dave! Du Wurst!")

positions = {}

#positions["cat"] = "mau"
#print(positions["cat"])

#if "cat" in positions:
#    print("yes")

for i in range(input_random):
    zuf_x = random.randint(1,coord_x)-1
    zuf_y = random.randint(1,coord_y)-1
    poskey = str(zuf_x) + ":" + str(zuf_y)
#    print(poskey)   

    while poskey in positions:
        zuf_x = random.randint(1,coord_x)-1
        zuf_y = random.randint(1,coord_y)-1
        poskey = str(zuf_x)  + ":" + str(zuf_y)
#        print(poskey)
    positions[poskey] = 1

final=""

for x in range(coord_x):
    for y in range(coord_y):
        poskey = str(x) + ":" + str(y)
        if poskey in positions:
            final += "*"
        else:
            final += "#"
    final += "\n"

print(final.strip())


exit()


#falsch!!!!
for poskey,posvalue in positions.items():
    str_x, str_y = poskey.split(":")
    zuf_x = int(str_x)
    zuf_y = int(str_y)
    for x in range(coord_x):
        if x != zuf_x:
            print("#"*coord_x)
        else:
            for y in range(coord_y):
                if y != zuf_y:
                    final = final + "#"
                else:
                    final = final + "*"
            print(final)
            final = ""

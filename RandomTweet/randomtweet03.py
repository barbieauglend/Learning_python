#python 2.7 and python 3.5

import os
from os import listdir
from random import shuffle, choice

filetype = {"txt": "Text",
            "doc": "Text-Word"}

def isText(filename):
    filename = filename.lower()
    return filename[filename.rfind(".")+1:] in filetype

def random_file():
    filename = [f for f in listdir(os.getcwd()) if isText(f)]
    return choice(filename)

filename = random_file()
example = open(filename).read().split()
tweetList = []
tweet = " "
i = 0

while len(tweet) < 140:
    shuffle(example)
    tweetListBP = tweetList
    tweetList = example[:i+1]
    tweet = ' '.join(tweetList)
    i += 1

if len(tweet) == 140:
    print(tweet)

else:
    tweetList = tweetListBP
    tweet = ' '.join(tweetList)
    print(tweet)
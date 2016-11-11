from random import shuffle

example = open("GPL.txt").read().split()
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
from random import shuffle

def tweeting(n):
    tweetList = example[:n]
    tweet =  ' '.join(tweetList)

example = open("GPL.txt").read().split()
shuffle(example)

nwords = input("enter how many words you want: ")
tweeting(nwords)

while len(tweet) > 140:
    tweeting(nwords)

print(tweet)
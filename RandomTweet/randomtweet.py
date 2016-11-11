from random import shuffle

example = open("GPL.txt").read().split()
shuffle(example)

nwords = input("enter how many words you want: ")
tweetList = example[:nwords]
tweet = ' '.join(tweetList)

print(tweet)
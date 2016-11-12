#python 2.7

# from random import shuffle
#
# example = open("GPL.txt").read().split()
# shuffle(example)
#
# nwords = input("enter how many words you want: ")
# tweetList = example[:nwords]
# tweet = ' '.join(tweetList)
#
# print(tweet)

#python 3.5

from random import shuffle

example = open("GPL.txt").read().split()
shuffle(example)

nwords = input("enter how many words you want: ")
n = int(nwords)
tweetList = example[:n]
tweet = ' '.join(tweetList)

print(tweet)
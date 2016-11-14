# python 3.5

import getpass
import wikipedia
from random import shuffle


def player_one():
    articles = wikipedia.random(1)
    article = wikipedia.page(articles, True).content
    f = open('wiki.txt', "w")
    f.write(article)
    f.close()
    docs = open('wiki.txt').read().split()
    shuffle(docs)
    wort = docs[1]
    return wort


def word_test():
    wort = ''
    if lvl == 1:
        while len(wort) < 4:
            wort = player_one()
            while len(wort) > 6:
                wort = player_one()
        return wort
    if lvl == 2:
        while len(wort) < 6:
            wort = player_one()
            while len(wort) > 11:
                wort = player_one()
        return wort
    if lvl == 3:
        while len(wort) < 11:
            wort = player_one()
            while len(wort) > 20:
                wort = player_one()
        return wort
    if lvl == 4:
        while len(wort) < 20:
            wort = player_one()
        return wort
    else:
        word_test()


def level():
    dif_input = input('1. Easy: \n2. Medium \n3. Hard \n4. Academic \nChoose: ')
    option = int(dif_input)
    return option


player_input = input('1. Singleplayer \n2. Multiplayer \nChoose: ')
player = int(player_input)
word = ''

while word == '':
    if player == 1:
        lvl = 0
        while lvl not in {1,2,3,4}:
            lvl = level()
        word = word_test()

    elif player == 2:
        word = getpass.getpass('Word: ')

    else:
        player_input = input('1. Singleplayer \n2. Multiplayer \nChoose: ')
        player = int(player_input)

tries = 3
guessed_letters = []
playing = True
hidden_word = word
for letter in word[1:len(word) - 1]:
    hidden_word = hidden_word.replace(letter, ' __ ')
print (hidden_word)

while playing:
    gamer_input = input('Your guess: ')
    hidden_word = word

    if not gamer_input:
        print ('Choose a letter to guess!')

    elif len(gamer_input) == 1 and gamer_input in 'qwertzuiopasdfghjklyxcvbnm':
        if gamer_input not in guessed_letters:
            guessed_letters.append(gamer_input)
            for letter in word[1:len(word) - 1]:
                if letter not in guessed_letters:
                    hidden_word = hidden_word.replace(letter, ' __ ')
            print (hidden_word)
            if gamer_input not in word:
                tries -= 1
                print('Wrong! You have ', tries, 'more tries/try.')
                if tries == 0:
                    print('Game Over!')
                    print('The word was ', word)
                    playing = False
            else:
                print('Good job!')
            if word == hidden_word:
                print('You won!')
                break
        else:
            print('Choose another letter: ')

# python 3.5

import getpass
from random import shuffle


def player_one():
    docs = open('GPL.txt').read().split()
    shuffle(docs)
    wort = docs[1]
    return wort


player_input = input('1 or 2 players?: ')
player = int(player_input)
word = ''

while word == '':
    if player == 1:
        while len(word) < 3:
            word = player_one()

    elif player == 2:
        word = getpass.getpass('Word: ')

    else:
        player_input = input('1 or 2 players?: ')
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
                    playing = False
            else:
                print('Good job!')
            if word == hidden_word:
                print('You won!')
                break
        else:
            print('Choose another letter: ')

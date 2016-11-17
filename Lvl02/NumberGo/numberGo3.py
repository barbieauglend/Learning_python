# python 3.5

import getpass
import random


def highscore_manager():
    re_scores = open("highscore.txt", "r").read().split(',')
    score = int(str(re_scores[1]))
    name = str(re_scores[0])
    if won > score:
        wr_scores = open("highscore.txt", "w")
        name_new = input('New Highscore! Type your name: ')
        new_score = name_new + ' , ' + str(won)
        wr_scores.write(str(new_score))
        wr_scores.close()

    repeat_option = 0
    while repeat_option not in range(1, 3):
        repeat_option = int(input('Do you want to play again?\n1. Yes\n2. No\n Your Option: '))
    if repeat_option == 2:
        repeat = False

    return name, score

repeat = True
lost = 0
won = 0

score = highscore_manager()
highscore = print('The actual highscore is from ', score)

while repeat:

    option = 0
    nr = 0
    while option not in range(1,3):
        option = int(input('1. Singleplayer \n2. Multiplayer: \nYou Option: '))

    if option == 1:
        nr = int(random.randint(1, 10))

    elif option == 2:
        while nr not in range(1,10):
            number = getpass.getpass('Nr Player One: ')
            nr = int(number)

    tries = 3
    guessed_numbers = []
    playing = True

    while playing:

        guess = input('Your guess: ')
        gamer_input = int(guess)
        print('You have ', tries, 'tries / try left')

        while not gamer_input:
            print ('Choose a number to guess!')

        if gamer_input != nr and gamer_input in range(1,10):
            if gamer_input not in guessed_numbers:
                tries -= 1
                guessed_numbers.append(gamer_input)
                if tries == 0:
                    print('Game Over!')
                    playing = False
                    lost += 1
                    highscore_manager()
                elif gamer_input < nr:
                    print('Not really! The Number you are searching for is bigger than ', gamer_input)
                elif gamer_input > nr:
                    print('Not really! The Number you are searching for is smaller than ', gamer_input)
            else:
                print('Choose another number: ')

        elif gamer_input == nr:
            print('You won!')
            won += 1
            playing = False
            highscore_manager()
        print('You have won ', won, ' times and lost ', lost, 'times.')

repeat_option = 0
while repeat_option not in range(1, 3):
    repeat_option = int(input('Do you want to play again?\n1. Yes\n2. No\n Your Option: '))
    if repeat_option == 2:
        repeat = False

exit()
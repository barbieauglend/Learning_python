# python 3.5

import getpass
import random

nr = int(random.randint(1,10))

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
            elif gamer_input < nr:
                print('Not really! The Number you are searching for is bigger than ', gamer_input)
            elif gamer_input > nr:
                print('Not really! The Number you are searching for is smaller than ', gamer_input)
        else:
            print('Choose another number: ')

    elif gamer_input == nr:
        print('You won!')
        exit()
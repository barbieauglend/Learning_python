# python 3.5

import getpass

nr = 0

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

    if not gamer_input:
        print ('Choose a number to guess!')

    elif gamer_input != nr and gamer_input in range(1,10):
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
            elif gamer_input == nr:
                print('You won!')
                break
        else:
            print('Choose another number: ')

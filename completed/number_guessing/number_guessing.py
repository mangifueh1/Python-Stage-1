import random

print('Number Guessing Program')
print('\nGuess my number between 1 - 100')

random_guess = random.randint(0, 100)
try:
    player_input = int(input("\nGuess: "))
    for x in range(0, 4):
        try:
            if player_input == random_guess:
                print(f'You guessed Correct. My number was {random_guess}')
                print('\nYou Win')
                break

            elif player_input > random_guess:
                print(f'{4 - x} attempts left')
                print('Go a little lower')
                player_input = int(input("\nGuess again: "))

            elif player_input < random_guess:
                print(f'{4 - x} attempts left')
                print('Go a little higher')
                player_input = int(input("\nGuess again: "))
        except:
            print('\nError please try again\n')
    else:
        print('\nYou Lose')
except:
    print('\nError please try again\n')

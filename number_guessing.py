import random

print('Number Guessing Program')
print('\nGuess my number between 1 - 100')

random_guess = random.randint(0, 100)

print(random_guess)
player_input = int(input("\nGuess: "))
result = False

# attempts = 5

for x in range(0, 4):
    if player_input == random_guess:
        print(f'You guessed Correct. My number was {random_guess}')
        result = True
        break

    elif player_input > random_guess:
        print(f'{4 - x} attempts left')
        print('Go a little lower')
        player_input = int(input("\nGuess again: "))
        # attempts -= 1

    elif player_input < random_guess:
        print(f'{4 - x} attempts left')
        print('Go a little higher')
        player_input = int(input("\nGuess again: "))
        # attempts -= 1

if result:
    print('\nYou Win')
else:
    print('\nYou Lose')

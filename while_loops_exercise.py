#guessing game

#repeat - guesses
#change - guess number
#repeat until guess is correct or runs out of guesses

num = 76
guess = 0 
guess_limit = 5
guess_number = 0

while guess_number < guess_limit:
    guess = int(input('Guess a number 1-100: '))
    if guess != num:
        guess_number += 1
        if guess > num:
            guess = int(input(f'{guess} is too high. Guess again: '))
        else:
            guess < num
            guess = int(input(f'{guess} is too low. Guess again: '))
    if guess == num:
        print(f'You win! You guessed it: {num}')
        break
    
if guess != num:
        print(f'Sorry, you ran out of guesses! It was {num}')
        

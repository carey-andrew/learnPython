import random

bag = ('black', 'green', 'green', 'green', 'green', 'green', 'red', 'red', 'red', 'white')

start_purse = 1000
purse = start_purse

result = 0
rounds = 3

marble = 'none'
print(f'Hi, you start the game with {start_purse} dollars. You will play {rounds} rounds.')

for draw in range(1, rounds + 1):
    print(f'Round {draw}')
    bet = int(input(f' You have {purse} dollars. Last draw: {marble} \nround. How much would you like to bet?: '))
    marble = random.choice(bag)
    if marble == 'green':
        result = bet
    elif marble == 'black':
        result = 10 * bet
    elif marble == 'white':
        result = -5 * bet
    else:
        result = -bet
        
    purse += result
    
    if purse < 0.5 * start_purse:
        print(f'Game over! You played {draw} rounds.')
        break   
    print(f'You drew a {marble} marble. You now have {purse} dollars.')
print('starting/ ending purse: ', start_purse, '/',purse)
print('gain/loss: ',(purse - start_purse)/start_purse * 100, '%')


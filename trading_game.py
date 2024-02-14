# random draw of marble from bag
import random as r

# bag contains 10 marbles, 6 green and 4 red
bag = ['green', 'green', 'green', 'green', 'green', 'green', 'red', 'red', 'red', 'red']

user_money = 1000
rounds = 0

# if green you win the same amount that you bet e.g. 10 returns 20
user_bet = int(input(f"You have {user_money} dollars. How much would you like to bet?: "))
# if red you lose the amount you bet
# all marbles are reset after each draw
draw = r.choice(bag)
if draw == 'green':
        user_money += user_bet
        print(f"You drew a {draw} marble. You now have {user_money} dollars.")
else:
        user_money -= user_bet
        print(f"You drew a {draw} marble. You now have {user_money} dollars.")
rounds += 1
if user_money <= 500:
    print(f"Game over! You played {rounds} rounds.")
else:
    print(input(f"You have {user_money} dollars. How much would you like to bet?: "))
#before each draw the user is asked how much they want to bet
#start with 1000 dollars
# the number of rounds should be variable
# if you lose half money then game over

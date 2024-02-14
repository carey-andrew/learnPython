#import modules
import random, random as r

# ask how many questions user wants
num_questions = int(input("How many questions would you like to answer?: "))
#set score to 0
user_score = 0
# loop for the number of questions
for q in range(num_questions):
    # create 2 randoms numbers and calculate the answer
    num_1 = r.randint(1,11)
    num_2 = r.randint(1,11)
    answer = num_1 * num_2
    #show user the question and ask for the answer
    user_answer = int(input(f"What is {num_1} * {num_2}?: "))
    #capture answer and check if correct
    if user_answer == answer:
        print("Correct!")
        #modify score
        user_score += 1
    else:
        print("Incorrect!")
        
print(f'Thank you for playing! Your final score is {user_score} out of {num_questions} {round(user_score/num_questions*100)}%')
# create 2 randoms numbers and calculate the answer
#show user the question and ask for the answer
#capture answer and check if correct
#modify score
#show final score
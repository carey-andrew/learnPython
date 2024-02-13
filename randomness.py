#import module randomness

#pseudo-random number generator

import random, string

print(random.random()) #random float between 0 and 1    
for i in range(5):
    print(random.random()*6) #random integer between 1 and 6
    
for i in range(5):
    print(random.randint(1,10)) 
# prints 5 random numbers between 1-10  

for i in range(5):
    print(random.uniform(1,6))
    #generates floats

for i in range(4):
    print(random.randrange(2,100,2)) 
    #step, range, start
    
friends_list = ['John', 'Martha', 'Peter', 'Samantha', 'Sandra']
print(random.choice(friends_list)) #randomly selects a name from the list
print(random.sample(friends_list, 2)) #randomly selects 2 names from the list   no duplicates
print(random.choices(friends_list, k=2)) #randomly selects 2 names from the list   duplicates allowed
print(random.shuffle(friends_list)) #shuffles the list  
print(friends_list) #shuffled list

smallcaps = 'abcdefghijklmnopqrstuvwxyz'
largecaps = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
digits = '0123456789'
letters_numbers = string.ascii_letters + string.digits
print(letters_numbers)

word= ''
for i in range(7):
    word += random.choice(letters_numbers)

word1 = ''.join(random.sample(letters_numbers, k=7))   #avoids duplicates
print(word)
print(word1)


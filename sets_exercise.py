# sets exercise
"""1.check if 'Eric' and 'John' exist in friends
2. combine the two sets
3. find all the names that are in both sets
4. find names that are only in friends
5. show only the names who only appear in one of the lists
6. create a new cars-list without duplicates
"""
friends = {'John','Michael','Terry','Eric','Graham'}
my_friends = {'Reg','Loretta','Colin','John','Graham'}
cars = ['900','420','V70','911','996','V90','911','911','S','328','900']

#1
if "Eric" in friends and "John" in friends:
    print("Eric and John are friends")
print('Eric' in friends and 'John' in friends)
#2
print(friends.union(my_friends))
print(friends | my_friends)
#3
print(friends.intersection(my_friends))
print(friends & my_friends)
#4 
print(friends.difference(my_friends))
print(friends - my_friends)
#5
print(friends.symmetric_difference(my_friends))
print(friends ^ my_friends)
#6
cars_no_dupl = list(set(cars))
print(cars_no_dupl)

friends = ['John','Michael','Terry','Eric','Graham']
friends_tuple = ('John','Michael','Terry','Eric','Graham')
friends_set = {'John','Michael','Terry','Eric','Graham','Eric'} #faster to search through and removes duplicates
print(friends)
print(friends_tuple)
print(friends_set)

my_friends_set = {'Reg','Loretta','Colin','Eric','Graham'}
print(friends_set.intersection(my_friends_set)) # print ones that are in both
print(friends_set.difference(my_friends_set)) # print ones that are in friends_set but not in my_friends_set
print(friends_set.union(my_friends_set)) # print all of them

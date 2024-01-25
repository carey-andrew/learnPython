friends = ['John','Michael','Ollie','Eric']
cars = [911,130,535,328,740,308]

print(friends)
print(friends[0])
print(friends[1],friends[3])
print(friends[2:3])

#sorting lists
friends.sort()
print(friends)
friends.sort(reverse=True)
print(friends)
friends.reverse()
print(friends)  

#lowest number in list
print(min(cars))
#highest number in list
print(max(cars))

#sum of all numbers in list
print(sum(cars))

#adding to list - append adds to end of list
friends.append('Terry')
print(friends)

#insert adds to specific position in list
friends.insert(2,'Graham')
print(friends)
#changing value in list
friends[2] = 'Eric'
print(friends)

#removing from list
del friends[2]
friends.remove('Eric')
friends.pop() #removes last item in list
friends.pop(-1)
print(friends)

friends.clear() #removes all items from list


#extending list
friends.extend(['Graham','Terry'])
print(friends)

#new list
new_friends = friends[:]
print(friends)
print(new_friends)

new_friends = friends.copy()
print(friends)

new_friends = list(friends)
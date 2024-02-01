for number in range(1,15,3):#range(start,stop,step)
    print(number)
print('done')


friends = ['John','Sarah','Sam','Mary']
for name in friends:
    print(name)

for index in range(len(friends)):
    print(friends[index]) #prints every element in the list

friends_list = ['Peter','Paul','Mary']
for friend in friends_list:
    for number in [1,2,3]:
        print(friend,number)
    
    
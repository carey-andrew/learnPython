
csv = 'Eric,John,Michael,Graham:Terry,Graham'
friends_list = ['Eric','John','Michael','Terry','Graham']
print(msg.split())
print(msg.split(' '))
print(csv.split(','))#split on comma

print('-'.join(friends_list))#join list with hyphen
print(''.join(friends_list))#join list with nothing inbetween
print(' '.join(friends_list))#join list with space inbetween

print(' '.join(msg.split()))
print(msg.replace(' ',''))

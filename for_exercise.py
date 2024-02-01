names = ['john ClEEse','Eric IDLE','michael']
names1 = ['graHam chapman', 'TERRY', 'terry jones']
msg = 'You are invitied to the party on Saturday.'
names.extend(names1)

for index in range(2):
    names.append(input('Enter a new name:'))

for name in names:
    msg1 = f'{name}! {msg}'
    print(msg1.title())

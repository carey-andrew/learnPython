#print a new string then reverse it
msg='Welcome to Python 101: Strings'
msg1=msg[18]+' '+msg[:8]+msg[25:29]+msg[7:11]+msg[13]+msg[12]+msg[2]+msg[1]+msg[-5]
print(msg1.title()) #capitalize first letter of each word
print(msg1[::-1].title())#reverse string

print(msg.find('Python'))
msg1=msg.replace('Python','Java')
print(msg)
print(msg1)

print('Python' in msg)
print('Python' not in msg)

name='JOHN'
color='Green'
msg3='['+name+'] loves the color '+color.lower()+'!'
msg4=f'{name.capitalize()} loves the color {color.lower()}!'
print(msg3)
print(msg4)
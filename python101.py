#print a new string then reverse it
msg='Welcome to Python 101: Strings'
msg1=msg[18]+' '+msg[:8]+msg[25:29]+msg[7:11]+msg[13]+msg[12]+msg[2]+msg[1]+msg[-5]
print(msg1.title()) #capitalize first letter of each word
print(msg1[::-1].title())#reverse string
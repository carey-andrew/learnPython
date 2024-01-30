def greeting(name,age=28,color='red'):
    print('Hello ' + name.capitalize() + ', you will be ' + str(age+1) + ' next birthday!')
    print(f'Hello {name.capitalize()}, you will be {age+1} next birthday!')
    print(f'We hear you like the color {color.lower()}!') 

name = input('What is your name? ')
age = input('What is your age? ')
color = input('What is your favorite color? ')
greeting(name,int(age),color)

'''
1. add new print statement - we hear you like the color xxx! xxx is a string with color
2. extend the function to use parameter color that defaults to 'red'
3. capture the color from the user
4. change the you are text to say you will be xx
+1 years old next birthday, adding one to inputted age
5. capitalize the first letter name
6. favourite color in lower case
'''


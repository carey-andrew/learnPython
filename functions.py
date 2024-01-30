#parameters, arguments and defaults
def greeting(name,age=28):
    print('Hello ' + name + ', you are ' + str(age) + '!')
    print(f'Hello {name}, you are {age}!')

name = input('What is your name? ')
greeting('Brian',32)
greeting(name)

#formatted strings are easier!




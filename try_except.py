#try:
    #code you want to run
#except:
    #code you want to run if an error occurs
#else:
    #code you want to run if no error occurs
#finally:
    #always executed

try:
    num = int(input('Enter a number between 1 and 30: '))
    num1= 30/num
    if num > 30:
        raise ValueError(num)
except ZeroDivisionError as err:
    print(err, 'You cannot divide by zero.')
except ValueError as err:
    print(err, 'You did not enter a number.')
except:
    print('Incorrect input.')
else:
    print('30 divided by', num, 'is ', 30/num)
finally:
    print("**Thank you for playing!**")
 
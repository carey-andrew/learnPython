#calculator exercise
#create a calc that handles +,-,*,/ and outputs the resultbased on the mode / operator used 
# use 3 seperate inputs
# bonus to include a celsius to fahrenheit converter
# formula is (c * 9/5) + 32 = f

first_number = float(input('Enter first number: '))
operator = input('Enter operator (+,-,*,/): ')
second_number = float(input('Enter second number: '))

if operator == '+':
    print(first_number + second_number)
elif operator == '-':
    print(first_number - second_number)
elif operator == '*':
    print(first_number * second_number)
elif operator == '/':
    print(first_number / second_number)
else:
    print('Invalid operator')

celsius = float(input('Enter temperature in celsius: ')) 
fahrenheit = (celsius * 9/5) + 32
print(f'{celsius} is equivalent to {fahrenheit} fahrenheit')


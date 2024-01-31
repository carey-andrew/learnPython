#print('If Statements')

is_raining = True
is_cold = True
print('Good Morning')
if is_raining or is_cold:
    print('Take an umbrella or coat or both')
else:
    print('Leave the umbrella at home')
#will run as long as one is true

print('Good Morning')
if is_raining and is_cold:#will only run if both are true
    print('Take an umbrella and coat')
elif is_raining and not(is_cold):
    print('Take an umbrella')
elif not(is_raining) and is_cold:
    print('Bring a coat')
else:
    print('Nothing needed today')
    
amount = 10
if amount <=50:
    print('Purchase approved')
else:
    print('Please enter a pin')
    

    

    

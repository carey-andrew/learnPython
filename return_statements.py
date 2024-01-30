def value_added_tax(amount):
    tax = amount * 0.25
print(value_added_tax(100))
#returns none as needs to be returned

def value_added_tax(amount):
    tax = amount * 0.25
    total_amount = amount * 1.25
    return [amount, tax, total_amount]
    #return (amount, tax, total_amount) gives a set
    #return f'(amount, tax, total_amount)' gives a string

price = value_added_tax(100)
print(price, type(price))
#print part of list
print(price[0])



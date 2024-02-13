# lambda is a small anonymous function

def square(x):
    return x * x

print(square(5))
# 25

#def square(x): return x * x
#square1 = lambda x: x * x
#print (square1(3))

def name_and_alias(name, alias):
    return name.strip().title() + " is also known as " + alias.strip().title()
# strip() removes leading and trailing whitespace
# title() returns a string with the first character of each word capitalized
name_and_alias1 = lambda name,alias: name.strip().title() + " is also known as " + alias.strip().title()

def name_and_alias2(name, alias):
    return name.strip().title() + " is also known as " + alias.strip().title()
#written as a one line lambda
print(name_and_alias("  john smith  ", "  johnny  "))

monty_python = ["John Cleese", "Eric Idle", "Michael Palin", "Terry Gilliam", "Terry Jones", "Graham Chapman"]

monty_python.sort(key=lambda name: name.split(" ")[-1].lower())
# sort by last name
print(monty_python)

def func(n):
    return lambda a : a * n
# lambda function to multiply a number by n
doubler = func(2)
print (doubler(11)) # 22
quadruple = func(4)
print(quadruple(11)) # 44
print(type(func(2)))
#receives a function and returns a function

def price_calc(start,hourly_rate):
    return lambda hours: start + hourly_rate * hours
walk_in_cost = price_calc(10, 30)
premium_cost = price_calc(1,25)
print(walk_in_cost(2)) # 70
# 10 + 30 * 2 = 70
print(premium_cost(2)) # 51
# 1 + 25 * 2 = 51
print(price_calc(1,25)(2)) # 51

print(lambda a,b,c: a+b+c)(2,3,4) # 9
#using default arguments
print((lambda a,b,c=4: a+b+c)(2,c=3,b=4)) # 9
#using named arguments
#unpacking
print((lambda *args: sum(args))(1,2,3,4)) # 10  




a = 7
b = 3

print(a == b)
print(a != b)
print(a > b)
print(a < b)

print('o' in 'John')
print('o' not in 'John')

#identity operators
a = [1, 2, 3]
b = [1, 2, 3]
print(a == b ) # returns true as the values are the same
print(a is b) # returns false as the objects are not the same

print(id(a), id(b))

print(int(True))# returns 1
print(int(False))# returns 0

print(bool)('Parrot') # returns true
print(bool)('') # returns false
print(bool)(42) # returns true
print(bool)(0) # returns false

print(bool)([1,2]) # returns true
print(bool)([]) # returns false

print(42 + True) # returns 43
print(42 + False) # returns 42


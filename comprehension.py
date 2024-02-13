numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#square each number
new_list = []
for num in numbers:
    new_list.append(num * num)
print(new_list)

#using list comprehension
new_list = [num * num for num in numbers]
print(new_list)

#only give me a num if number is even
new_list = []
for num in numbers:
    if num % 2 == 0:
        new_list.append(num)
        
print(new_list)
#as comprehension
new_list = [num for num in numbers if num % 2 == 0]

# letter and number pairs for each letter in spam and each number in '0123'
new_list = []
for letter in 'spam':
    for num in range(4):
        new_list.append((letter,num))
print(new_list) 
#as comprehension
new_list = [(letter,num) for letter in 'spam' for num in range(4)]

#comprehension is like destructuring in JS

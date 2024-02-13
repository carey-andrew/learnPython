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

#dictionary comprehension
movies = ["And Now for Something Completely Different", "Monty Python and the Holy Grail", "Monty Python's Life of Brian", "Monty Python Live at the Hollywood Bowl", "Monty Python's The Meaning of Life", "Monty Python Live (Mostly)"]
year = [1971, 1975, 1979, 1982, 1983, 2014]
names = ['John', 'Eric', 'Michael', 'Terry G', 'Terry J', 'Graham']

print(list(zip(movies,year)))

new_dict = dict()
for movie, yr in zip(movies,year):
    new_dict[movie] = yr
print(new_dict)

#as comprehension
new_dict = {movie:yr for movie,yr in zip(movies,year)}
print(new_dict)
#year needed to be changed to yr because year is a built-in function and int was not iterable
#can add if statements
new_dict = {movie:yr for movie,yr in zip(movies,year) if yr > 1980}
print(new_dict)
#startswith() is a string method
new_dict = {movie:yr for movie,yr in zip(movies,year) if movie.startswith('Monty')}
print(new_dict)

n1 = [(name,movie,yr) for name in names for movie,yr in zip(movies,year) if yr < 1981]
print(n1)

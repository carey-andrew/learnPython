#dictionary is a key value pair - word is key and def is value
#dictionary is mutable
movie ={
    'title':'Life of Brian',
    'year':1979,
    'cast':['John','Eric','Michael','George','Terry'],
}
print(movie)
print(movie['title'])
print(movie.get('title')) #returns none if key does not exist
print(movie.get('budget', 'not available'))

#update a dictionary
movie.update({'title' : 'The Holy Grail','year':1975,'cast':['John','Eric','Michael','George','Terry']})

#add a new key value pair
movie['budget'] = 250000
#del movie['year']#delete a key value pair
year = movie.pop('year')#pop a key value pair
print(movie.get('budget'))

print(movie)
print(year) #prints the value of the key that was popped
print(len(movie)) #prints the number of key value pairs in the dictionary

print(movie.keys())
print(movie.values())
print(movie.items())

#looping through a dictionary
for key, value in movie.items():
    print(key, value)#remember year was popped out

people = {}
people1= {}
people2 = {}
#method 1 update dict
people.update(movie)

print(sorted(people))
#method 2 comprehension
for groups in movie: people1.update(groups)
print(people1)
#method 3 - unpacking
people2 = {**movie}#unpacking key
print(sorted(people2))

#unpacking doesn't sort in the order of the keys
#finding the sum of all the values in a dictionary
print(sum(movie.values()))
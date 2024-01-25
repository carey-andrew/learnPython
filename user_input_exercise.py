#take 2 inputs from user 
#1. first name
#2. distance in km

# greet user by name show km and miles 

# 1 mile = 1.609 km

name = input('What is your name?: ')
distance = input('What is the distance in km?: ')
distance = float(distance)
distance_miles = distance / 1.609
print(f'Hello {name.title()}! You are {distance} km and {round(distance_miles,2)} miles away from me.')
# Exercise: Split and Join
# take csv and turn into list, removing ; and :
csv = 'Eric,John,Michael,Terry,Graham:TerryG;Brian'
#print(','.join(csv.split(';')))
#print(','.join(csv.split(';')).split(':'))
#print((','.join(','.join(csv.split(';')).split(':'))).split(','))
                                  
friends_list = (','.join(','.join(csv.split(';')).split(':'))).split(',')
print(friends_list)
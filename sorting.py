my_list = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]
my_dict = {'car':4, 'dog':2, 'add':3, 'bee':1}
my_tuple = (1, 3, 5, 7, 9, 2, 4, 6, 8, 10)
my_string = 'python'

#list and dict are mutable, tuple and string are immutable

#sort() #sorts the list in place but does not return anything
#sorted() #returns a sorted list but does not change the original list
#reverse() #has similar effect - reverses but does not return

#sorting a tuple returns a list
#sorting a dictionary returns a list of the keys
#print(sorted(my_dict.values(),reverse=True))

#print(my_list[::-1])#reverse a list

my_new_list = [1,5,-3,7,-2]
my_other_list = [['car',4,65],['dog',2,3],['add',3,4],['bee',1,2]]
print(sorted(my_new_list))
#sorts by the first element in the list
print(sorted(my_new_list, key=abs)) #sorts by the absolute value

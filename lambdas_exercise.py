#def f(x): return x + 5
f = lambda x: x + 5
print(f(2))

#def strip_spaces(str):
#    return str.strip()
strip_spaces = lambda str:''.join(str.strip())
print(strip_spaces("  hello  "))

def join_list_no_duplicates(list_a,list_b):
    return list(set(list_a + list_b))

list_a = [1,2,3,4]
list_b = [3,4,5,6,7]

join_list_no_duplicates1 = lambda list_a,list_b: list(set(list_a + list_b))

print(join_list_no_duplicates1(list_a,list_b))

def create_quad_function(a,b,c):
    return lambda x: a*x**2 + b*x + c
f = create_quad_function(2,4,6)
g = create_quad_function(1,2,3)
print(f(2)) # 16
print(g(2)) # 11

signups = ['MPF104', 'MPF20', 'MPF2', 'MPF17', 'MPF3', 'MPF45']
#print(sorted(signups)) # ['MPF104', 'MPF17', 'MPF2', 'MPF20', 'MPF3', 'MPF45']
print(sorted(signups, key=lambda id: int(id[3:]))) # ['MPF2', 'MPF3', 'MPF17', 'MPF20', 'MPF45', 'MPF104']

class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score

Eric = Player('Eric', 116700)
John = Player('John', 24327)
Terry = Player('Terry', 150000)
player_list = [Eric, John, Terry]

player_list.sort(key=lambda player: player.score reverse=True)

print([player.name for player in player_list]) # ['Eric', 'John', 'Terry']

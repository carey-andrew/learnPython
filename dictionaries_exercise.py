freelancers = {'name':'freelancing shop','brian':70, 'black knight':20, 'biccus diccus;':100, 'grim reaper':500, 'minstrel':-15}
antiques = {'name': 'Antique Shop','french castle':400, 'wooden grail':3, 'scythe':150, 'catapult':75, 'german joke':5}
pet_shop = {'name':'Pet Shop','blue parrot':10, 'white rabbit':5, 'newt': 2}

cart = {}

for shop in (freelancers, antiques,pet_shop):
    buy_item = input(f'welcome to {shop['name']}, what do you want to buy? {shop}').lower()
    cart.update({buy_item:shop.pop(buy_item)})
    bought = ", ".join(list(cart.keys()))
    print(f'You have bought {bought}. Today they are all free!')
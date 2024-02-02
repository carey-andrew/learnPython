freelancers = {'name':'freelancing shop','brian':70, 'black knight':20, 'biccus diccus;':100, 'grim reaper':500, 'minstrel':-15}
antiques = {'name': 'Antique Shop','french castle':400, 'wooden grail':3, 'scythe':150, 'catapult':75, 'german joke':5}
pet_shop = {'name':'Pet Shop','blue parrot':10, 'white rabbit':5, 'newt': 2}

department_store = {}
for department in (freelancers, antiques, pet_shop) :department_store.update(department)
department_store.pop
print('Morning inventory', sorted(department_store.items()))
print()


cart = {}
#create purse with money
purse = 1000
buy_items1 = ''

for shop in (freelancers, antiques,pet_shop):
    buy_item = input(f'welcome to {shop['name']}, what do you want to buy? {shop}').lower()
    if buy_item == 'exit':
        continue
    if buy_item not in shop:
        print(f'we don\'t have a {buy_item} in the {shop["name"]}')
        continue
    
    buy_items1 = buy_items1 + f'{buy_item} :{shop[buy_item]}GP, '
    cart.update({buy_item:shop.pop(buy_item)})
    bought = ", ".join(list(cart.keys()))
    total_sum = sum(cart.values())
    print(f'You have bought {buy_items1}. Your total is {total_sum}. Your change is {purse - sum(cart.values())}. Have a nice day.')
    
    department_store_after_purchase = {**freelancers, **antiques, **pet_shop}
    department_store_after_purchase.pop('name')
    print('Evening inventory', sorted(department_store_after_purchase.items()))
    print()
    
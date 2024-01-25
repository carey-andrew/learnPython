#sell lemonade over 2 weeks. profit for each day is 1.5$
#add another day to week 2 by capturing a number as input
#combine the two lists into 'sales'
#calculate totals for
#best day
#worst day
#separately for each week and in total

sales_w1 = [7,3,42,19,15,35,9]
sales_w2 = [12,4,26,10,7,28] 
new_day = input('Enter sales for day 7: ')
sales_w2.append(int(new_day))
   
sales = sales_w1 + sales_w2
#sales.sort()
print(max(sales))
worst_day = min(sales) * 1.5
best_day = max(sales) * 1.5
print(f'Best day: {best_day}')
print(f'Worst day: {worst_day}')
print(f'combined: {worst_day + best_day}')
#print(sum(sales_w1),sum(sales_w2))



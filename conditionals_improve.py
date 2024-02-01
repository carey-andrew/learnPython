def num_days(month):
    days = 31
    if month in ['Apr','Jun','Sep','Nov']:
        days = 30
    elif month == 'Feb':
        days =28
    print('number of days in', month, 'is', days)
    
num_days('trump')
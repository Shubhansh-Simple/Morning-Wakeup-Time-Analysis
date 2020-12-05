from datetime import datetime as dt
from  datetime import timedelta as delta
from time import sleep

'''
Created at 29-11-2020,Sun,Nov  
Insert starting and ending dates
and get all the between dates with
day-name,month-name in dates.csv file 
'''

print('Starting....')
sleep(1)

print('\nComputer Program To Generate Day-Date-Month\n')
print('Date format exactly same as below.')
print('For Eg. 1-9-2020\n')
sleep(2)

def days_btw_dates(start_date, end_date ,its_format):
    '''Gives total days b/w dates'''
    try:
        start_dt = dt.strptime(start_date,its_format)
        end_dt   = dt.strptime(end_date,its_format)
        try:
            total_day = (end_dt - start_dt).days
            if total_day > 0:
                return [total_day + 1,start_dt]
            else:
                raise Exception
        except:
            print('Error - Make sure ending date is after the starting date.')
            return [ None,None ]
    except ValueError:
        print('Error - Please enter a valid date')
        return [ None,None ]

def file_check():
    '''Check if file exists or not'''
    try:
        f = open(file_name,'r')
        f.close()
        return False
    except FileNotFoundError:
        return True

# Variables,Clean code
date_format = '%d-%m-%Y'
date_mon_format = date_format + ',%a,%b'
file_name = 'dates_june.csv'
no_of_days = None

print(file_name)
input('Kindly check the filename')

# Inputs
if file_check():
    start_date = input('Starting Date - ')
    end_date   = input('Ending Date - ')
    
    # Days b/w them
    no_of_days,start_date = days_btw_dates(start_date, end_date , date_format)
else:
    print('Error - Kindly delete dates.csv file.')



if no_of_days:
    f_opener = open(file_name,'w')
    f_opener.write("dates,days,month\n")
    
    for x in range(0,no_of_days):
        current_date = start_date + delta(x)
        f_opener.write( current_date.strftime(date_mon_format) )
        f_opener.write('\n')
    
    f_opener.close()
    sleep(1)
    if not file_check():
        print('Data saved into ',file_name)
    


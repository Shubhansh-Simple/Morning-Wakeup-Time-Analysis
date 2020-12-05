from datetime import timedelta as td
from datetime import datetime as dt

'''
Created at 29-11-2020,Sun,Nov
Taking time input b/w starting-ending dates
and save it to a file 
Enter time without colon i.e.':'
'''

# starting date 
starting_date = dt(2020,6,1)
ending_date = dt(2020,6,30)
date_format = '%d-%m-%Y'
file_name = 'wake_up_times_may.txt'

total_days = (ending_date - starting_date).days + 1
print('Total no of days - ',total_days)

print(file_name)
input('Kindly check the filename - ')

with open(file_name,'w') as time_writer:
    time_writer.write('wake_up_time\n')
    for x in range(0,total_days):
        # Showing dates 
        print( '\nDates - ', (starting_date + td(x)).strftime(date_format)  )

        wake_time = input("Enter wake-up time (without ':') {}. - ".format(x+1))
        time_writer.write(wake_time+'\n')

print('Checkout file - ',file_name)
time_writer.close()




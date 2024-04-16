# first_name = 'Fadila'
# last_name = 'Afiani'
# # full_name = first_name + ' ' + last_name
# full_name = f'My name is {first_name} {last_name}'
# print(full_name)

from datetime import datetime

today = datetime.now()

date_time = today.strftime('%Y-%m-%d %H:%M:%S')
print(date_time)
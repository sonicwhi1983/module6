#Wite the current date as a string to the text file today.txt#
from datetime import date 
now = date.today() 
now_str = now.isoformat() 
with open('2024-02-12', 'wt') as output: 
    print(now_str, file=output) 

#Read the text file today.txt into the string into the today_string. 

with open('2024-02-12', 'rt') as input:
    today_string = input.read() 

today_string 
'2024-12-02\n' 

#Parse the date from today_string. 
fmt = '%aY-%m-%d\n' 
datetime.strptime(today_string, fmt) 
datetime.datetime(2024, 12, 2, 0, 0)


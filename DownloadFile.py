import requests
from datetime import datetime as dt
import time

ticker = input("Enter the ticker symbol: ")
from_date = input('Enter start date in yyyy/mm/dd format: ')
to_date = input('Ener end date in yyyy/mm/dd format: ')

from_datetime = dt.strptime(from_date, '%Y/%m/%d')
to_datetime = dt.strptime(to_date, '%Y/%m/%d')

# converting the datetime in int
from_epoch = int(time.mktime(from_datetime.timetuple()))
to_epoch = int(time.mktime(to_datetime.timetuple()))

url = f"https://query1.finance.yahoo.com/v7/finance/download/{ticker}?period1={from_epoch}&period2={to_epoch}&interval=1d&events=history&includeAdjustedClose=true"

#This simulates a browser
headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"}

content = requests.get(url, headers=headers).content
#print(content)

with open('data_finances.csv', 'wb') as file:
    file.write(content)
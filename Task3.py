# Check which day on the next week  in Bangkok is going to be the hottest one.
# Use pprint, requests, datetime.

import requests
from  pprint import  pprint
from collections import Counter
from datetime import datetime

url = 'https://api.open-meteo.com/v1/forecast?latitude=13.754&longitude=100.5014&hourly=temperature_2m,relativehumidity_2m&timezone=Asia%2FBangkok&forecast_days=14'


res = requests.get(url)
# pprint(res.json())
values = res.json()

list_temperature_2m = values['hourly']['temperature_2m']
list_time = values['hourly']['time']
dict_dt_temp = {} #{time:temp,time:temp}

def most_frequent_item_count(collection):
    if not collection:
        return 0
    counter = Counter(collection)
    most_common = counter.most_common(1)[0]
    return most_common

for i in range(len(list_time)):
    datei = list_time[i]
    tempi = list_temperature_2m[i]

    if datei not in dict_dt_temp:
        dict_dt_temp[datei] = tempi

    elif dict_dt_temp[datei] < tempi:
        dict_dt_temp[datei] = tempi


hotday = most_frequent_item_count(dict_dt_temp)
print(hotday)
print('hottest day: ', datetime.fromisoformat(hotday[0]), '- temp: ', hotday[1])

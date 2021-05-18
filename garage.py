import json
import datetime
import matplotlib.pyplot as plt
import pytz

with open('/Users/decarlo/conda/steelyards/camera_garage.jsonl', 'r') as json_file:
    json_list = list(json_file)

car_list = []
person_list = []
bike_list = []
t_list = []
tp_list = []
tb_list = []

for json_str in json_list:   
    result = json.loads(json_str)
    obj = result['value'][0]['object']
    if obj == 'car':
        car_list.append(result['value'][0]['object'])
        # car_list.append(1)
        date = datetime.datetime.fromtimestamp(float(result['timestamp']), pytz.timezone("America/Denver"))
        t_list.append(date)
        print(date, result['value'][0]['object'])
    if obj == 'person':
        person_list.append(result['value'][0]['object'])
        date = datetime.datetime.fromtimestamp(float(result['timestamp']), pytz.timezone("America/Denver"))
        tp_list.append(date)
        print(date, result['value'][0]['object'])
    if obj == 'bike':
        bike_list.append(result['value'][0]['object'])
        date = datetime.datetime.fromtimestamp(float(result['timestamp']), pytz.timezone("America/Denver"))
        tb_list.append(date)
        print(date, result['value'][0]['object'])

n = 1

cars    = plt.plot(t_list[::n], car_list[::n], 'bo')
persons = plt.plot(tp_list[::n], person_list[::n], 'bo')
bikes   = plt.plot(tb_list[::n], bike_list[::n], 'bo')
plt.title('Average garage door Open/Close = 3.71 times/day')
plt.ylabel('Garage access')
plt.show()

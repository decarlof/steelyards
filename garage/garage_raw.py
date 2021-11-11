import datetime
import pytz
import time
import json
import datetime
import matplotlib.pyplot as plt
import pytz

import jsonlines

def time_to_epoch(*args):

    event = datetime.datetime(*args)
    moutain_time = pytz.timezone("America/Denver")
    event = moutain_time.localize(event)
    return(time.mktime(event.timetuple()) + event.microsecond * 1e-6)


items = [
{"timestamp":time_to_epoch(2021, 5, 16, 14, 35),"value":[{'object':'car'}, {'direction':'in'}]},
{"timestamp":time_to_epoch(2021, 5, 16, 14, 18),"value":[{'object':'car'}, {'direction':'in'}]},
{"timestamp":time_to_epoch(2021, 5, 16, 13, 52),"value":[{'object':'car'}, {'direction':'in'}]},
{"timestamp":time_to_epoch(2021, 5, 16, 13, 32),"value":[{'object':'person'}, {'direction':'in'}]},
{"timestamp":time_to_epoch(2021, 5, 16, 12, 48),"value":[{'object':'person'}, {'direction':'in'}]},
{"timestamp":time_to_epoch(2021, 5, 16, 10, 59),"value":[{'object':'car'}, {'direction':'in'}]},
{"timestamp":time_to_epoch(2021, 5, 16, 10, 36),"value":[{'object':'car'}, {'direction':'in'}]},
{"timestamp":time_to_epoch(2021, 5, 16, 20, 28),"value":[{'object':'car'}, {'direction':'in'}]},
{"timestamp":time_to_epoch(2021, 5, 16, 19, 50),"value":[{'object':'car'}, {'direction':'in'}]},
{"timestamp":time_to_epoch(2021, 5, 16, 17, 25),"value":[{'object':'car'}, {'direction':'out'}]},
{"timestamp":time_to_epoch(2021, 5, 16, 16, 23),"value":[{'object':'car'}, {'direction':'in'}]},
{"timestamp":time_to_epoch(2021, 5, 16, 14, 44),"value":[{'object':'person'}, {'direction':'in'}]},
{"timestamp":time_to_epoch(2021, 5, 16, 12, 53),"value":[{'object':'car'}, {'direction':'in'}]},
{"timestamp":time_to_epoch(2021, 5, 16, 12, 36),"value":[{'object':'person'}, {'direction':'out'}]},
{"timestamp":time_to_epoch(2021, 5, 16, 11, 40),"value":[{'object':'person'}, {'direction':'in'}]},
{"timestamp":time_to_epoch(2021, 5, 16,  8, 35),"value":[{'object':'person'}, {'direction':'in'}]},
{"timestamp":time_to_epoch(2021, 5, 15, 21, 40),"value":[{'object':'person'}, {'direction':'out'}]},
{"timestamp":time_to_epoch(2021, 5, 15, 21, 31),"value":[{'object':'car'}, {'direction':'in'}]},
{"timestamp":time_to_epoch(2021, 5, 15, 21, 23),"value":[{'object':'car'}, {'direction':'out'}]},
{"timestamp":time_to_epoch(2021, 5, 15, 14, 21),"value":[{'object':'car'}, {'direction':'in'}]},
{"timestamp":time_to_epoch(2021, 5, 15, 13, 42),"value":[{'object':'car'}, {'direction':'in'}]},
{"timestamp":time_to_epoch(2021, 5, 15, 13, 24),"value":[{'object':'person'}, {'direction':'in'}]},
{"timestamp":time_to_epoch(2021, 5, 15, 12, 19),"value":[{'object':'car'}, {'direction':'in'}]},
{"timestamp":time_to_epoch(2021, 5, 15, 11, 56),"value":[{'object':'bike'}, {'direction':'in'}]},
{"timestamp":time_to_epoch(2021, 5, 14, 23, 43),"value":[{'object':'person'}, {'direction':'out'}]},
{"timestamp":time_to_epoch(2021, 5, 14, 22,  3),"value":[{'object':'person'}, {'direction':'in'}]},
{"timestamp":time_to_epoch(2021, 5, 14, 19, 34),"value":[{'object':'person'}, {'direction':'in'}]},
{"timestamp":time_to_epoch(2021, 5, 14, 19, 17),"value":[{'object':'car'}, {'direction':'in'}]},
{"timestamp":time_to_epoch(2021, 5, 14, 16,  2),"value":[{'object':'car'}, {'direction':'in'}]},
{"timestamp":time_to_epoch(2021, 5, 14, 15, 39),"value":[{'object':'person'}, {'direction':'out'}]},
{"timestamp":time_to_epoch(2021, 5, 14, 15,  9),"value":[{'object':'car'}, {'direction':'out'}]},
{"timestamp":time_to_epoch(2021, 5, 14, 14, 57),"value":[{'object':'car'}, {'direction':'in'}]},
{"timestamp":time_to_epoch(2021, 5, 14, 14,  9),"value":[{'object':'person'}, {'direction':'in'}]},
{"timestamp":time_to_epoch(2021, 5, 14, 12, 12),"value":[{'object':'car'}, {'direction':'in'}]},
{"timestamp":time_to_epoch(2021, 5, 14, 11, 37),"value":[{'object':'person'}, {'direction':'in'}]},
{"timestamp":time_to_epoch(2021, 5, 14, 11, 29),"value":[{'object':'car'}, {'direction':'in'}]},
{"timestamp":time_to_epoch(2021, 5, 14, 10, 39),"value":[{'object':'person'}, {'direction':'in'}]},
{"timestamp":time_to_epoch(2021, 5, 14, 10, 33),"value":[{'object':'person'}, {'direction':'in'}]},
{"timestamp":time_to_epoch(2021, 5, 14,  9,  3),"value":[{'object':'person'}, {'direction':'in'}]},
{"timestamp":time_to_epoch(2021, 5, 14,  6, 23),"value":[{'object':'person'}, {'direction':'out'}]},
{"timestamp":time_to_epoch(2021, 5, 14,  5, 25),"value":[{'object':'person'}, {'direction':'out'}]},
{"timestamp":time_to_epoch(2021, 5, 14,  4, 16),"value":[{'object':'person'}, {'direction':'out'}]},
{"timestamp":time_to_epoch(2021, 5, 14,  2, 28),"value":[{'object':'person'}, {'direction':'out'}]},
{"timestamp":time_to_epoch(2021, 5, 13, 20, 48),"value":[{'object':'car'}, {'direction':'in'}]},
{"timestamp":time_to_epoch(2021, 5, 13, 19, 54),"value":[{'object':'person'}, {'direction':'in'}]},
{"timestamp":time_to_epoch(2021, 5, 13, 19, 23),"value":[{'object':'person'}, {'direction':'in'}]},
{"timestamp":time_to_epoch(2021, 5, 13, 19, 10),"value":[{'object':'person'}, {'direction':'in'}]},
{"timestamp":time_to_epoch(2021, 5, 13, 19,  4),"value":[{'object':'person'}, {'direction':'out'}]},
{"timestamp":time_to_epoch(2021, 5, 13, 18, 56),"value":[{'object':'person'}, {'direction':'in'}]},
{"timestamp":time_to_epoch(2021, 5, 13, 18, 45),"value":[{'object':'person'}, {'direction':'in'}]},
{"timestamp":time_to_epoch(2021, 5, 13, 18, 20),"value":[{'object':'person'}, {'direction':'out'}]},
{"timestamp":time_to_epoch(2021, 5, 13, 18, 13),"value":[{'object':'person'}, {'direction':'in'}]},
{"timestamp":time_to_epoch(2021, 5, 13, 16, 19),"value":[{'object':'person'}, {'direction':'in'}]},
{"timestamp":time_to_epoch(2021, 5, 13, 16,  1),"value":[{'object':'car'}, {'direction':'in'}]},
{"timestamp":time_to_epoch(2021, 5, 13, 14, 43),"value":[{'object':'car'}, {'direction':'out'}]},
{"timestamp":time_to_epoch(2021, 5, 13, 14,  9),"value":[{'object':'person'}, {'direction':'in'}]},
{"timestamp":time_to_epoch(2021, 5, 13, 14,  4),"value":[{'object':'person'}, {'direction':'in'}]},
{"timestamp":time_to_epoch(2021, 5, 13, 13, 45),"value":[{'object':'person'}, {'direction':'in'}]},
{"timestamp":time_to_epoch(2021, 5, 13, 13,  9),"value":[{'object':'person'}, {'direction':'out'}]},
{"timestamp":time_to_epoch(2021, 5, 13, 13,  1),"value":[{'object':'person'}, {'direction':'in'}]},
{"timestamp":time_to_epoch(2021, 5, 13, 12, 51),"value":[{'object':'person'}, {'direction':'in'}]},
{"timestamp":time_to_epoch(2021, 5, 13, 12, 42),"value":[{'object':'car'}, {'direction':'in'}]},
{"timestamp":time_to_epoch(2021, 5, 13, 11, 55),"value":[{'object':'person'}, {'direction':'in'}]},
{"timestamp":time_to_epoch(2021, 5, 13, 11, 19),"value":[{'object':'car'}, {'direction':'in'}]},
{"timestamp":time_to_epoch(2021, 5, 13, 8,  43),"value":[{'object':'person'}, {'direction':'in'}]},
{"timestamp":time_to_epoch(2021, 5, 13, 6,  21),"value":[{'object':'person'}, {'direction':'out'}]},
{"timestamp":time_to_epoch(2021, 5, 13, 5,  28),"value":[{'object':'person'}, {'direction':'out'}]},
]

with jsonlines.open('/Users/decarlo/conda/steelyards/camera_garage.jsonl', 'w') as writer:
    writer.write_all(items)






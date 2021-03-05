import requests
import json
from gpiozero import Button
from time import sleep
import datetime
import random


t = datetime.datetime.now()
        
t_log = "{0}-{1}-{2}.log".format(t.strftime("%Y"), t.strftime("%m"), t.strftime("%d"))
t_json = "{0}-{1}-{2}T{3}:{4}:{5}".format(t.strftime("%Y"), t.strftime("%m"), t.strftime("%d"), t.strftime("%H"), t.strftime("%M"), t.strftime("%S"))

loc_id = random.randint(1, 3)
filename="{t_log}"


def log():
    # create a new event - replace with your API
    url = 'https://modas-jsg.azurewebsites.net/api/event/'
    headers = { 'Content-Type': 'application/json'}
    payload = { 'timestamp': t_json, 'flagged': False, 'locationId': loc_id }
    # post the event
    r = requests.post(url, headers=headers, data=json.dumps(payload))
    print(r.status_code)
    print(r.json())
    f = open(t_log, "a")
    f.write("{0},False,{1},{2}\n".format(t_json, loc_id, r.status_code))
    f.close
    
# init button
button = Button(12)
button.when_released = log

try:
    # program loop
    while True:
        sleep(.001)
# detect Ctlr+C
except KeyboardInterrupt:
    print("goodbye")



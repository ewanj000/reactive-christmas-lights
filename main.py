from tuyapy import TuyaAPI
import time
import json
with open("./config.json","r") as f:
    data = json.load(f)
    username = data("username")
    password = data("password")
    device_id = data("device_id")

# email to discord code goes above so i dont have to spend ages writing the get email code again

# login to api
TuyaAPI.login(username, password)

if mail.subject == "Front Door Camera Line Crossing":
    TuyaAPI.get_device_by_id(device_id).turn_on()
    time.sleep(600)
    TuyaAPI.get_device_by_id(device_id).turn_off()
from tuyapy import TuyaAPI
import time
import json


with open("./config.json","r") as f:
    data = json.load(f)
    username = data["username"]
    password = data["password"]
    device_id = data["device_id"]

# imap code goes here i cba doing it

# login to api
TuyaAPI.login(username, password)

if mail.subject == "Front Door Camera Line Crossing":
    TuyaAPI.get_device_by_id(device_id).turn_on()
    time.sleep(600)
    TuyaAPI.get_device_by_id(device_id).turn_off()
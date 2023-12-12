from tuyapy import TuyaAPI
import time

# login to api
TuyaAPI.login(username, password)

if mail.subject = "Front Door Camera Line Crossing":
    TuyaAPI.get_device_by_id(device_id).turn_on
    time.sleep(600)
    TuyaAPI.get_device_by_id(device_id).turn_off
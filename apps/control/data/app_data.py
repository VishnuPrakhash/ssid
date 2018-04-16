DEVICE_URL = "http://10.28.3.33"

options = ["open_door", "close_door", "switch_on_light", "switch_off_light", "switch_on_ac",
           "switch_off_ac"]
options2 = ["switch_on_vending", "refill_bin", "cleanse_bin", "switch_off_vending"]


actions_living = [{
    "action": "open_door",
    "description": "Open Door"
}, {
    "action": "close_door",
    "description": "Close Door"
}, {
    "action": "switch_on_ac",
    "description": "Switch On AC"
}, {
    "action": "switch_off_ac",
    "description": "Switch Off AC"
}, {
    "action": "switch_on_light",
    "description": "Switch On Light"
}, {
    "action": "switch_off_light",
    "description": "Switch Off Light"
}]


actions_pantry = [{
    "action": "turn_on_vending",
    "description": "Turn On Vending"
}, {
    "action": "refill_bin",
    "description": "Refill Bin"
}, {
    "action": "cleanse_bin",
    "description": "Cleanse Bin"
}, {
    "action": "turn_off_vending",
    "description": "Turn Off Vending"
}]


client_data = {"ap_mac": "94b40fc9bb1e", "client_ip": "172.31.99.161", "ssid": "Guest12"}
SSID_LIVING = "Guest12"
SSID_PANTRY = "Guest21"
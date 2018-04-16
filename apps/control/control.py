import json
import requests
import re
import psycopg2
import logging
from flask import Flask, render_template, request
from flask_cors import CORS

app = Flask("Control")
CORS(app)

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


sample_client_data = {"ap_mac": "94b40fc9bb1e", "client_ip": "172.31.99.161", "ssid": "Guest12"}

SSID_LIVING = "Guest12"
SSID_PANTRY = "Guest21"


@app.route("/", methods=['POST', 'GET'])
def hello():
    # logging.info("PRINTING THE REQUEST HEADERS : {}".format(request.headers))
    return "<h1 style='color:blue'>Hello There!</h1>"


@app.route("/preference.html", methods=['POST', 'GET'])
def preference():
    return render_template("preference.html")


@app.route('/options', methods=['POST', 'GET'])
def options():
    if get_last_entry_from_pg()["ssid"] == SSID_LIVING:
        return json.dumps(actions_living)
    elif get_last_entry_from_pg()["ssid"] == SSID_PANTRY:
        return json.dumps(actions_pantry)
    else:
        return json.dumps([])


def get_last_entry_from_pg():
    data = []
    try:
        conn = psycopg2.connect(
            "dbname='radius' user='radius' password='radpass' host='localhost'")
        cur = conn.cursor()
        cur.execute("""SELECT * from radpostauth""")
        rows = cur.fetchall()
        logging.info("\nShow me the databases: \n")
        data = rows[-1]
    except Exception:
        logging.info("Unable to connect to the database")
    return {"ap_mac": re.search("(.*):", data[4]).group(1),
            "ssid": re.search(":(.*)", data[4]).group(1), "client_ip": data[5]}


@app.route("/action/<action>", methods=['POST', 'GET'])
def invoke_action(action):
    # print requests.header
    url = "{}:1800/actions/{}".format(DEVICE_URL, action)
    data = {"user_name": "Aruba"}
    device_resp = requests.post(url, data=json.dumps(data))
    resp = json.loads(device_resp.content)
    return json.dumps(resp)


if __name__ == "__main__":
    app.debug = True
    app.run(port=5001, debug=True)

import am2302
import json
import network
from umqtt.simple import MQTTClient
import ubinascii
import machine
import time

def read_conf():
    with open("meteo.conf") as f:
        data = json.load(f)
    for k, v in data.items():
        print(k, ": ", v)
    return data

def connect(conf):
    nic = network.WLAN(network.STA_IF)
    nic.active(True)
    nic.connect(conf["WIFI_SSID"], conf["WIFI_PASSWORD"])

    while not nic.isconnected():
        machine.idle()
    print("Connected to Wifi\n")

def main(conf):
    for sensor in conf["SENSORS"]:

        data = am2302.get_measure(pin=sensor["PIN"])
        if data:
            c = MQTTClient(
                client_id=conf["CLIENT_ID"],
                user=conf["ADAFRUIT_IO_USERNAME"],
                server=conf["ADAFRUIT_IO_URL"],
                password=conf["ADAFRUIT_IO_KEY"],
                port=1883
            )
            c.connect()
            for topic in sensor["TOPICS"]:
                top = str(topic["NAME"])
                mes = str(data[topic["TYPE"]])
                c.publish(str.encode(top), str.encode(mes))
                time.sleep(conf["PERIOD"])
            c.disconnect()

        time.sleep(conf["PERIOD"])

if __name__ == "__main__":
    conf = read_conf()
    conf["CLIENT_ID"] = ubinascii.hexlify(machine.unique_id())

    connect(conf)
    while True:
        main(conf)

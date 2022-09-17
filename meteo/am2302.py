# Complete project details at https://RandomNerdTutorials.com

from machine import Pin
from time import sleep
import dht

def start_measure(data={}, period=10):
    while True:
        sleep(period)
        data = get_measure()
        for k, v in data.items():
            print(k, ": ", v)

def get_measure():
    try:
        sensor = dht.DHT22(Pin(14))
        sensor.measure()
        temp = sensor.temperature()
        hum = sensor.humidity()
        return {"hum": hum, "temp": temp}
    except OSError as e:
        print('Failed to read sensor.')
        return {}

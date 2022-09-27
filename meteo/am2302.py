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

def get_measure(pin=14):
    try:
        sensor = dht.DHT22(Pin(pin))
        sensor.measure()
        temperature = sensor.temperature()
        humidity = sensor.humidity()
        return {"humidity": humidity, "temperature": temperature}
    except OSError as e:
        print('Failed to read sensor.')
        return {}

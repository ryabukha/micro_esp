import time
import ubinascii
import machine
from umqtt.simple import MQTTClient
from machine import Pin
import network

c = None
button = Pin(5, Pin.IN)
start = time.ticks_ms()

server = "10.0.0.200"
client_id = ubinascii.hexlify(machine.unique_id())
topic = b"led/lampa1/pub"
msg = b"switch"


def do_connect():
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect('organhall', 'filarmonia')
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ifconfig())


def do_connect_mqtt(server, client_id):
    global c
    c = MQTTClient(client_id, server)
    c.connect()
    print("Connected to %s, waiting for button presses" % server)


def do_publish(topic, msg):
    global c
    c.publish(topic, msg)


def do_slip():
    global start
    delta = time.ticks_diff(time.ticks_ms(), start)  # compute time difference
    if delta > 20000:
        network.WLAN(0).active(0)
        network.WLAN(1).active(0)
        print('wifi off')
        return 1
    return 0


def main():
    do_connect_mqtt(server, client_id)
    global start
    # s = 0
    while True:
        while True:
            if button.value() == 1:
                break
            time.sleep_ms(20)
            s = do_slip()
        print("Button pressed " + str(button.value()))
        start = time.ticks_ms()
        # s = do_slip()
        print('s: ', s)
        if s:
            do_connect()
            do_connect_mqtt(server, client_id)

        do_publish(topic, msg)
        time.sleep_ms(200)
    c.disconnect()


do_connect()
main()

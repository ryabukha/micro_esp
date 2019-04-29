import time
import ubinascii
import machine
from umqtt.simple import MQTTClient
import network
import sbtn

c = None

b = sbtn.Button()

start = time.ticks_ms()  # current tick activity
timeout = 20000  # time out before to disable wifi

server = "10.0.0.200"
client_id = ubinascii.hexlify(machine.unique_id())
topic1 = b"led/lampa1/pub"
topic2 = b"led/lampa2/pub"
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


def do_disable_wifi():
    network.WLAN(0).active(0)
    network.WLAN(1).active(0)
    print('wifi is disabled')
    machine.freq(80000000)
    print(machine.freq())
    return False


def main():
    do_connect_mqtt(server, client_id)
    # do_publish(topic2, msg)
    flags_modem_isOn = True
    global start
    while True:
        b.tick()

        if b.isPress():
            start = time.ticks_ms()
        elif flags_modem_isOn and time.ticks_diff(time.ticks_ms(), start) > timeout:
            flags_modem_isOn = machine.deepsleep()

        if b.isDouble():
            print("Button pressed double ")
            if not flags_modem_isOn:
                do_connect()
                do_connect_mqtt(server, client_id)
                flags_modem_isOn = True
            do_publish(topic2, msg)

        if b.isSingle():
            print("Button pressed Single ")
            if not flags_modem_isOn:
                do_connect()
                do_connect_mqtt(server, client_id)
                flags_modem_isOn = True
            do_publish(topic1, msg)
    c.disconnect()


# do_connect()
# main()

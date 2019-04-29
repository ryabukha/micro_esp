import app

def do_connect():
    import network
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect('organhall', 'filarmonia')
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ifconfig())


# do_connect()
app.do_connect()
app.main()

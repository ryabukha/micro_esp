# micro_esp
about micropython in esp8266

for start:
http://docs.micropython.org/en/latest/esp8266/quickref.html

env:
```
sudo apt install python3.10-venv

python3 -m venv venv

source venv/bin/activate
```

driver: https://learn.sparkfun.com/tutorials/how-to-install-ch340-drivers/linux


issues:
https://github.com/juliagoda/CH341SER/issues/18

```
for f in /usr/lib/udev/rules.d/*brltty*.rules; do
    sudo ln -s /dev/null "/etc/udev/rules.d/$(basename "$f")"
done
sudo udevadm control --reload-rules
```
```
sudo systemctl mask brltty.path
```

esp8266-pro
- EN -> 10kOm -> 3.3v
- GPIO 15 -> 10kOm -> GND
- GPIO 0 -> GND for flash
- GPIO 16 -> RST for deepsleep

meteo.conf:
```
{
"ADAFRUIT_IO_USERNAME": "name",
"ADAFRUIT_IO_URL": "io.adafruit.com",
"ADAFRUIT_IO_KEY": "key",
"WIFI_SSID": "ssid_name",
"WIFI_PASSWORD": "password",
"PERIOD": 1,  # in minutes
"SENSORS": [
    {
        "NAME" : "ONE",
        "PIN"  : 13,
        "TOPICS": [
            {
                "NAME" : "adafruit_io_username/path/to/topic",
                "TYPE" : "temperature"
            },
            {
                "NAME" : "adafruit_io_username/path/to/topic",
                "TYPE" : "humidity"
            }
        ]
    }
]
}
```

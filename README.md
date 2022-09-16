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

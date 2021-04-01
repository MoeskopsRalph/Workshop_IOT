#!/bin/su root
apt-get update -y 
apt install python3-pip -y 
apt install python3-cffi -y 
pip3 install discord.py[voice]
python3 -m pip install -U discord.py[voice]
apt-get install build-essential python-dev -y
git clone https://github.com/adafruit/Adafruit_Python_DHT.git
cd Adafruit_Python_DHT
python setup.py install
python3 setup.py install
#apt-get autoremove -y
#apt-get autoclean -y
systemctl enable ssh
systemctl start ssh
raspi-config nonint do_camera 0
reboot

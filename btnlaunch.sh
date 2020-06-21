#!/bin/sh
# btnlaunch.sh
# navigate to home directory, then to this directory, then execute python script, then back home


cd /
cd home/pi/pi-power-buttons
sudo python3 resetbutton.py
cd /

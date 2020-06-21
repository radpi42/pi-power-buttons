# pi-power-buttons
power and reset buttons for raspberry pi with leds


making it run at start with cron

make cron logs


Navigate back to your home directory:

###############################
cd /home/pi/pi-power-buttons
###########################

Create a logs directory:

##############################
mkdir logs
#############################


set up crontab:

##################################
crontab -e
#################################

@reboot sh /home/pi/pi-power-buttons/btnlaunch.sh >/home/pi/pi-power-buttons/logs/cronlog 2>&1

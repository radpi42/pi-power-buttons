from gpiozero import Button, LED
from subprocess import check_call
from signal import pause
from time import sleep
import os
import sys

#define stuff

#LEDS
#set led GPIO pins
blue = LED(21)
red = LED(20)



#Button
#set button gpio pins

Button.was_held = False
shutdown_btn = Button(2, hold_time=1.25)
restart_btn = Button(16, hold_time=1.25)

#functions for shutdown


def SDpressed():
    red.on()
    print("Shutdown Command Primed")
#    print("Hold to proceed")
    
    
# button held

def SDheld(shutdown_btn):
    red.off()
    shutdown_btn.was_held = True
    red.on()
    sleep(1.25)
#    print("Shutdown Process Armed")
    red.blink(.25, .25)
    pause()
        
#button released

def shutdown():
    if shutdown_btn.was_held:
  #      print("Shutdown Process Intialized")
        sleep(1)
        red.off()
        sleep(1.25)
        red.on()
   #     print("Shutting Down")
        sleep(1)
    #    print("Until Next Time!")
        red.off()
        shutdown_btn.was_held = False
        print("success")
        check_call(['sudo', 'poweroff'])
    else:
        red.off()
     #   print("Cancled")
        
        
        



#reboot functions:

def RBpressed():
    blue.on()
    print("Reboot Command Primed")
 #   print("Hold to proceed")

def RBheld(reboot_btn):
    reboot_btn.was_held = True
    blue.off()
    blue.on()
    sleep(1)
  #  print("Reboot Process Armed")
    blue.blink(.25, .25)
           

def reboot():
    if restart_btn.was_held:
   #     print("Reboot Process Intialized")
        sleep(1)
        blue.off()
        sleep(1.5)
        blue.on()
    #    print("Rebooting")
        sleep(1.25)
     #   print("See you soon!")
        blue.off()
        restart_btn.was_held = False
        print("success")
        check_call(['sudo', 'reboot'])    
    else:
        blue.off()
        sleep(0.5)
        restart_btn.was_held = False
      #  print("Cancled")
        
      
        
  
# THE CODE 


while True:
    shutdown_btn.when_pressed = SDpressed
    shutdown_btn.when_held = SDheld
    shutdown_btn.when_released = shutdown

    restart_btn.when_pressed = RBpressed
    restart_btn.when_held = RBheld
    restart_btn.when_released = reboot

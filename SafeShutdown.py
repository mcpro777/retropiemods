#!/usr/bin/env python3
from gpiozero import Button, LED
import os 
from signal import pause

powerPin = 3 
resetPin = 16 
ledPin = 21
hold = 1
led = LED(ledPin)
led.on()

#functions that handle button events
def powerdown():
  led.blink(.2,.2)
  os.system("sudo killall emulationstation && sleep 5s && sudo shutdown -h now")
def reboot(): 
  os.system("sudo killall emulationstation && sleep 5s && sudo reboot")
  
#pin number is the GPIO number, ex GPIO14
btn = Button(powerPin, hold_time=hold)
rebootBtn = Button(resetPin)
rebootBtn.when_pressed = reboot 
btn.when_pressed = powerdown
pause()
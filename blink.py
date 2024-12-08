from machine import Pin
from time import sleep

led = Pin(2, Pin.OUT)
led_status=1
while True:
    led_status = not led_status   #to toggle between HIGH and LOW
    led.value(led_status)
    sleep(1)
    
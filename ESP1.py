from machine import Pin, PWM
from time import sleep

# Initialize PWM on GPIO pin 2 (commonly the onboard LED)
led = PWM(Pin(2))
led.freq(1000)  # Set PWM frequency to 1 kHz

while True:
    # Gradually increase brightness
    for duty in range(0, 1024,5):  # Duty cycle: 0 (off) to 1023 (full brightness)
        led.duty(duty)  # Set the duty cycle
        sleep(0.01)     # Small delay for smooth transition

    # Gradually decrease brightness
    for duty in range(1023, -1, -5):  # Decrease duty cycle
        led.duty(duty)
        sleep(0.01)

""" This example uses the motion sensor to detect shaking """

from adafruit_circuitplayground import cp
import time

while True:
    if cp.shake():
        print("Device has been shaken!")
        time.sleep(60.0)
"""This example uses the slide switch to control the LEDs."""
from adafruit_circuitplayground import cp
import time

while True:
    if cp.switch:
        cp.pixels[0] = (137, 52, 184)
        time.sleep(0.5)
        cp.pixels[1] = (10, 83, 222)
        time.sleep(0.5)
        cp.pixels[2] = (36, 208, 36)
        time.sleep(0.5)
        cp.pixels[3] = (251, 242, 26)
        time.sleep(0.5)
        cp.pixels[4] = (251, 111, 36)
        time.sleep(0.5)
        cp.pixels[5] = (234, 13, 13)
        time.sleep(0.5)
        cp.pixels[6] = (137, 52, 184)
        time.sleep(0.5)
        cp.pixels[7] = (10, 83, 222)
        time.sleep(0.5)
        cp.pixels[8] = (36, 208, 36)
        time.sleep(0.5)
        cp.pixels[9] = (251, 242, 26)
        time.sleep(2.0)
        cp.pixels.fill((0, 0, 0))
        time.sleep(1)

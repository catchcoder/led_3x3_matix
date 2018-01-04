"""
Flash LEDS with a Raspberry PI
Parts needed:
    1 x Raspberry PI
   27 x LEDS
    2 x switch non-latching
"""

try:
    """ Try and import GPIO for Raspberry Pi,
    if it fails import fake GPIO for CI """
    import RPi.GPIO as GPIO
except ImportError:
    """ import fake GPIO
    https://pypi.python.org/pypi/fakeRPiGPIO/0.2a0"""
    from RPi import GPIO

import time
import sys


LEDS = [17, 27, 22, 10, 9, 11, 5, 6, 13]
LEVELS = [2, 3, 4]
PATTERN = [
    [9, 2, 9, 3, 9, 4],
    [17, 2, 17, 3, 17, 4, 22, 2, 22, 3, 22, 4, 13, 2, 13, 3, 13, 4, 5, 2, 5, 3,
     5, 4],
    [27, 2, 27, 3, 27, 4, 11, 2, 11, 3, 11, 4, 6, 2, 6, 3, 6, 4, 10, 2, 10, 3,
     10, 4]]

RUN = True
BTNSTARTSTOP = 19
BTNPLAY = 26
DELAY = 0.05
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


def setupbuttons():
    """ Setup Start/Stop button on GPIO12
    """
    GPIO.setup(BTNSTARTSTOP, GPIO.IN, pull_up_down=GPIO.PUD_UP)


def setupleds():
    """ Setup GPIOs for LEDS
    """
    for led in LEDS:
        GPIO.setup(led, GPIO.OUT)


def setuplevels():
    """ Setup negitive for LEDS
    """
    for level in LEVELS:
        GPIO.setup(level, GPIO.OUT)


def alloff():
    """ Turn off all LEDS and set ground voltage to high
    """
    checkifbuttonpressed()

    for led in LEDS:
        GPIO.output(led, GPIO.LOW)
    for level in LEVELS:
        GPIO.output(level, GPIO.HIGH)


def checkifbuttonpressed():
    """ Check if Button pressed
    """
    global RUN
    if not GPIO.input(BTNSTARTSTOP):
        RUN = False


setupbuttons()
setupleds()
setuplevels()


def main():
    """ Basic light up
    """
    try:
        while RUN:
            for LEDS in PATTERN:
                alloff()

                if not RUN:
                    break
                i = 0
                while i < len(LEDS):
                    alloff()
                    GPIO.output(LEDS[i], GPIO.HIGH)
                    GPIO.output(LEDS[i + 1], GPIO.LOW)
                    time.sleep(0.05)
                    i += 2
                time.sleep(DELAY)

    except KeyboardInterrupt:
        GPIO.cleanup()

    GPIO.cleanup()
    sys.exit(0)


if __name__ == '__main__':
    main()

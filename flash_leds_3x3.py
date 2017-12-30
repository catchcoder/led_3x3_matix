
"""
Flash LEDs with a Raspberry PI
Parts needed:
    1 x Raspberry PI
    9 x LEDS
    1 x switch non-latching
"""

import time
import RPi.GPIO as GPIO

leds = [14, 15, 18, 17, 27, 22, 10, 9, 11]
levels = [2, 3, 4]
btnstartstop = 12
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


def setupbuttons():
    """ Setup Start/Stop button on GPIO12
    """
    GPIO.setup(btnstartstop, GPIO.IN, pull_up_down=GPIO.PUD_UP)


def setupleds():
    """ Setup GPIOs for LEDS
    """
    for led in leds:
        GPIO.setup(led, GPIO.OUT)


def setuplevels():
    """ Setup negitive for LEDs
    """
    for level in levels:
        GPIO.setup(level, GPIO.OUT)


def alloff():
    """ Turn off all LEDs and set ground voltage to high
    """
    global leds
    global levels
    for led in leds:
        GPIO.output(led, GPIO.LOW)
    for level in levels:
        GPIO.output(level, GPIO.HIGH)


setupbuttons()
setupleds()
setuplevels()

""" Basic light up
"""


def main():
    try:
        while True:
            if not GPIO.input(btnstartstop):
                break
            for level in levels:
                for led in leds:
                    alloff()
                    GPIO.output(led, GPIO.HIGH)
                    GPIO.output(level, GPIO.LOW)
                    # time.sleep(0.01)
    except KeyboardInterrupt:
        GPIO.cleanup()

    GPIO.cleanup()


if __name__ == '__main__':
    main()

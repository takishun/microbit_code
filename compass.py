# Add your Python code here. E.g.
from microbit import *
compass.calibrate()

while True:
    bearing = compass.heading()
    if bearing < 45 or bearing >= 315:
        display.show('N')
        sleep(100)
    elif bearing < 135 and bearing >= 45:
        display.show('E')
        sleep(100)
    elif bearing < 225 and bearing >= 135:
        display.show('S')
        sleep(100)
    elif bearing < 315 and bearing >= 225:
        display.show('W')
        sleep(100)
    else:
        display.show('!')
        sleep(100)

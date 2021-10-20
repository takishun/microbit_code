# Add your Python code here. E.g.
from microbit import *

def judge_critical():
    import random as r
    gen = r.randint(0,1)
    
    if gen == 0:
        critical_hit_animation(0)
    if gen == 1:
        critical_hit_animation(1)

def critical_hit_animation(sw):
    sleep(1000)
    display.show(Image.SURPRISED)
    sleep(1000)
    
    if sw == 0:
        display.scroll("NOT CRITICAL HIT!!")
        sleep(250)
        display.show(Image.SAD)
        sleep(1000)
    elif sw == 1:
        display.scroll("CRITICAL HIT!!")
        sleep(250)
        display.show(Image.HAPPY)
        sleep(1000)
    

def allow_animation():
    boat0 = Image("00000:"
              "90000:"
              "99000:"
              "90000:"
              "00000") 
              
    boat1 = Image("0000:"
              "09000:"
              "99900:"
              "09000:"
              "00000")

    boat2 = Image("00000:"
              "00900:"
              "99990:"
              "00900:"
              "00000")

    boat3 = Image("00000:"
              "00090:"
              "99999:"
              "00090:"
              "00000")
    
    all_boats = [boat0,boat1,boat2,boat3]
    display.show(all_boats, delay=500)

def first_animation():
    display.show(Image.HEART)
    sleep(500)
    display.show(Image.HEART_SMALL)
    sleep(500)
    display.show(Image.HEART)
    sleep(500)
    display.show(Image.HEART_SMALL)
    sleep(500)
    display.show(Image.HEART)
    sleep(500)
    display.show(Image.HEART_SMALL)
    sleep(250)
    display.show(Image.HEART)
    sleep(250)
    display.show(Image.HEART_SMALL)
    sleep(250)
    display.show(Image.HEART)
    sleep(500)

while True:
    if button_a.is_pressed():
        first_animation()
        allow_animation()
        judge_critical()
        sleep(2500)
        display.clear()

    
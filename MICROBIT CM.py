from microbit import *
import random

names = ["Cassidy", "Annabelle", "Julia", "Campbell", "Emily" ]
name = random.choice(names)

while True:
    if button_a.is_pressed():
        if name == "Cassidy":
            display.scroll(name)
            display.show(Image.HAPPY)
        elif name == "Emily":
            display.scroll(name)
            display.show(Image.HEART)
        elif name == "Campbell":
            display.scroll(name)
            display.show(Image.DIAMOND)
            sleep(2000)
        elif name == "Annabelle"
            display.scroll(name)
            display.show(Image.HAPPY)
    elif button_b.is_pressed():
        display.show(Image.FABULOUS)
    else:
        display.show(Image.MEH)
        
display.clear()
import webbrowser as wb
import pyautogui as pg
import time as t

name = pg.prompt("What's your name? ")
if name == "Campbell":
    pg.alert("What a pretty name!")
elif name == "campbell":
    pg.alert("What a pretty name!")
elif name == "Julia":
    pg.alert("What a pretty name!")
elif name == "julia":
    pg.alert("What a pretty name!")
else:
    pg.alert("You're my new best friend " + name + "!")

fruit = pg.prompt("What is your favorite fruit? ")
if fruit == "watermelon":
    pg.alert("Refreshing!")
elif fruit == "Watermelon":
    pg.alert("Refreshing")
elif fruit == "apple":
    pg.alert("An apple a day keeps the doctor away!")
elif fruit == "Apple":
    pg.alert("An apple a day keeps the doctor away!")
elif fruit == "strawberry":
    pg.alert("Strawberrylicious!")
elif fruit == "Strawberry":
    pg.alert("Strawberrylicious!")
elif fruit == "strawberries":
    pg.alert("Strawberrylicious!")
elif fruit == "Strawberries":
    pg.alert("Strawberrylicious!")
else:
    pg.alert("Yum! I love " + fruit + "s" )
    wb.open("")

boardgame = pg.prompt("What's your favorite boardgame? ")
if boardgame == "monopoly":
    pg.alert("I'm a beast at monopoly")
elif boardgame == "Monopoly":
    pg.alert("I'm a beast at monopoly")
elif boardgame == "life":
    pg.alert("Do you like the cereal too?")
elif boardgame == "Life":
    pg.alert("Do you like the cereal too?")
else:
    pg.alert("Cool beans! I love " + boardgame + "!!")
    wb.open("")

birthday = pg.prompt("What month is your birthday? ")
wb.open("https://www.google.com/search?q=" + birthday + " birthstone")

pup_kit = pg.prompt("Do you like puppies or kittens better? ")
if pup_kit == "puppies":
    wb.open("https://www.youtube.com/watch?v=p079QtWvf7o")
elif pup_kit == "Puppies":
    wb.open("https://www.youtube.com/watch?v=p079QtWvf7o")
elif pup_kit == "kittens":
    wb.open("https://www.youtube.com/watch?v=8HVWitAW-Qg")
elif pup_kit == "Kittens":
    wb.open("https://www.youtube.com/watch?v=8HVWitAW-Qg")

age = pg.prompt("What year were you born?")
pg.alert("You are "  + str(2018 - int(age)) + " years old!")



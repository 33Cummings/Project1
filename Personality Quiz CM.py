import webbrowser as wb
import pyautogui as pg

name = input("What's your name? ")
if name == "Campbell":
    print("What a pretty name!")
elif name == "campbell":
    print("What a pretty name!")
elif name == "Julia":
    print("What a pretty name!")
elif name == "julia":
    print("What a pretty name!")
else:
    print("You're my new best friend " + name + "!")

fruit = input("What is your favorite fruit? ")
if fruit == "watermelon":
    print("Refreshing!")
elif fruit == "Watermelon":
    print("Refreshing")
elif fruit == "apple":
    print("An apple a day keeps the doctor away!")
elif fruit == "Apple":
    print("An apple a day keeps the doctor away!")
elif fruit == "strawberry":
    print("Strawberrylicious!")
elif fruit == "Strawberry":
    print("Strawberrylicious!")
else:
    print("Yum! I love " + fruit + "s" )
    wb.open("")

boardgame = input("What's your favorite boardgame? ")
if boardgame == "monopoly":
    print("I'm a beast at monopoly")
elif boardgame == "Monopoly":
    print("I'm a beast at monopoly")
elif boardgame == "life":
    print("Do you like the cereal too?")
elif boardgame == "Life":
    print("Do you like the cereal too?")
else:
    print("Cool beans! I love " + boardgame + "!!")
    wb.open("")

birthday = input("What month is your birthday? ")
wb.open("https://www.google.com/search?q=" + birthday + " birthstone")

pup_kit = input("Do you like puppies or kittens better? ")
if pup_kit == "puppies":
    wb.open("https://www.youtube.com/watch?v=p079QtWvf7o")
elif pup_kit == "Puppies":
    wb.open("https://www.youtube.com/watch?v=p079QtWvf7o")
elif pup_kit == "kittens":
    wb.open("https://www.youtube.com/watch?v=8HVWitAW-Qg")
elif pup_kit == "Kittens":
    wb.open("https://www.youtube.com/watch?v=8HVWitAW-Qg")

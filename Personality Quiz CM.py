import webbrowser as wb
import pyautogui as pg
import time as t

points = 0

name = pg.prompt("What's your name? ").title()

name = name.title()
if name == "Campbell":
    pg.alert("What a pretty name!")
    points =+5
elif name == "Julia":
    pg.alert("What a pretty name!")
    points =+5
elif name == "Annabelle":
    pg.alert("Can I call you belly?")
    points =+5
elif name == "Emily":
    pg.alert("Do you go by Emi?")
    points =+5
else:
    pg.alert("Too bad")
    point =-5
t.sleep(3)

fruit = pg.prompt("What is your favorite fruit? Please write it in singular!").title()

if fruit == "Watermelon":
    pg.alert("Refreshing")
    points =+5
elif fruit == "Apple":
    pg.alert("An apple a day keeps the doctor away!")
    points =+5
elif fruit == "Strawberry":
    pg.alert("Strawberrylicious!")
    points =+5
else:
    pg.alert("Yum! I love " + fruit + "s" )
    wb.open("")
    points =+2
t.sleep(3)

boardgame = pg.prompt("What's your favorite boardgame? ").title()

if boardgame == "Monopoly":
    pg.alert("I'm a beast at monopoly")
    points =+5
elif boardgame == "Life":
    pg.alert("Do you like the cereal too?")
    points =+5
else:
    pg.alert("Cool beans! I love " + boardgame + "!!")
    wb.open("")
    points =+3
t.sleep(3)

birthday = pg.prompt("What month is your birthday? ").title()
wb.open("https://www.google.com/search?q=" + birthday + " birthstone")
t.sleep(3)

pup_kit = pg.prompt("Do you like puppies or kittens better? ")

if pup_kit == "Puppies":
    wb.open("https://www.youtube.com/watch?v=p079QtWvf7o")
    points =+5
elif pup_kit == "Kittens":
    wb.open("https://www.youtube.com/watch?v=8HVWitAW-Qg")
    points =+4

age = pg.prompt("What year were you born?")
pg.alert("According to my caluculations you are "  + str(2018 - int(age)) + " years old!")
t.sleep(3)

scale = pg.prompt("On a scale from 1 to 10, how much did you like this Personality Quiz?")
if scale == "1":
    wb.open("https://www.redbubble.com/people/jrlele/works/21517674-dont-worry-i-hate-you-too?p=canvas-pg.alert")
elif scale == "2":
    wb.open("https://www.redbubble.com/people/jrlele/works/21517674-dont-worry-i-hate-you-too?p=canvas-pg.alert")
elif scale == "3":
    wb.open("https://www.redbubble.com/people/jrlele/works/21517674-dont-worry-i-hate-you-too?p=canvas-pg.alert")
elif scale == "4":
    wb.open("https://www.teepublic.com/kids-t-shirt/1992089-meh-emoticon")
elif scale == "5":
    wb.open("https://www.teepublic.com/kids-t-shirt/1992089-meh-emoticon")
elif scale == "6":
    wb.open("https://www.teepublic.com/kids-t-shirt/1992089-meh-emoticon")
elif scale == "7":
    wb.open("https://tenor.com/view/ok-okay-gif-8046320")
elif scale == "8":
    wb.open("https://tenor.com/view/ok-okay-gif-8046320")
elif scale == "9":
    wb.open("https://www.amazon.com/Funny-Retro-Poster-Awesome-Youre/dp/B077SBWJYR")
elif scale == "10":
    wb.open("https://www.amazon.com/Funny-Retro-Poster-Awesome-Youre/dp/B077SBWJYR")
t.sleep(3)

book = pg.prompt("What's you favorite series of a books").title()
if "Harry Potter" in book:
    pg.alert("I love Hermione!")
    house = pg.prompt("What house are you in?").title()
    if house == "Griffindor":
        pg.alert("Just like Harry!")
    elif house == "Hufflepuff":
        pg.alert("So...like Cedric Diggory?")
    elif house == "Slytherin":
        pg.alert("Like Snape!")
        evil = pg.prompt("Are you evil?").title()
        if evil == "Yes":
            pg.alert("Oh no!")
        elif evil == "No":
            pg.alert("Okay, good")
            
elif book == "Hunger Games":
    pg.alert("I love the Hunger Games!")
    favcharacter = pg.prompt("Who's your favorite character?").title()
    if favcharacter == "Catniss":
        pg.alert("She's awesome!")
    elif favcharacter == "Rue":
        pg.alert("She was so sweet")
    elif favcharacter == "Peeta":
        pg.alert("Oooooh...")
    else:
        pg.alert("Cool!")


        
genre = pg.confirm("Which genre books do you like to read?",
                   "Choose one",['Romance','Sci-Fi','Fantasy','Fiction', 'Non-fiction','Historical Fiction','Mystery', 'Horror','Poetry','Comic'])
if genre in ["Fiction","Fantasy"]:
    pg.alert("Mysterious..")
    dragons = pg.confirm("Do you like dragons?","Yes or No?",['Yes','No'])
    if dragons == "Yes":
        pg.alert("Cool beans!")
        wb.open("https://giphy.com/gifs/animated-dragon-WSVh9JdYhTRLO")
    elif dragons == "No":
        pg.alert("Too bad!")
elif genre == "Romance":
    pg.alert("Oooh la la..")
    wb.open("https://tenor.com/search/heart-gifs")
elif genre == "Comic":
    draw = pg.confirm("Do you like to draw?","Choose one",['Yes', 'No'])
    

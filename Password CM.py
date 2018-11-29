import pyautogui as pg

f = open('harrypottersecretcodeCMfile.txt',"w")

house = pg.confirm ("Which house are you in?","Choose one",['Gryffindor','Slytherin','Ravenclaw','Hufflepuff'])

# Graphics of the game
# Author : Théo Läderach
# Date : 05.02.2026
# Version : 1.0
import core

from tkinter import *
import json

number = {
    "1": "2",
    "2": "4",
    "3": "8",
    "4": "16",
    "5": "32",
    "6": "64",
    "7": "128",
    "8": "256",
    "9": "512",
    "10": "1024",
    "11": "2048",
    "12": "4096",
    "13": "8192"
}

main=Tk()
main.title("titre de la fenêtre")
main.geometry("500x600")
left_fr = Frame(main)
left_fr.pack(side=LEFT, fill=X)

title_lbl = Label(left_fr, text="2048")
title_lbl.pack()


right_fr = Frame(main)
right_fr.pack(side=RIGHT, fill=X)

score_lbl = Label(right_fr,text="Score : xxx")
score_lbl.pack()

new_btn = Button(right_fr,text="New Game")
new_btn.pack()

game_fr = Frame(main)
game_fr.pack(fill=Y, side=BOTTOM)

for y in core.grid:
    for x in y:
        Label(text=str(x)).grid(row = y, column=x)

main.mainloop()
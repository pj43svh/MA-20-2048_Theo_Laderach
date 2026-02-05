# Graphics of the game
# Author : Théo Läderach
# Date : 05.02.2026
# Version : 1.0
import core
core.start_game()

from tkinter import *
import json

# Dictionnary for the text
txt_dict = { 
    "0":"",
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

# Dictionnary for the color
color_dict = {
    "0": "#C4CBCB",
    "1": "#48B64B",
    "2": "#4CC89C",
    "3": "#58C9DA",
    "4": "#4261C2",
    "5": "#964ED4",
    "6": "#DD45CF",
    "7": "#E52222",
    "8": "#FF6308",
    "9": "#FFC408",
    "10": "#FFFA08",
    "11": "#B2FF08",
    "12": "#43FF08",
    "13": "#08FBFF"
}


def render_grid_txt():
    global visualGridTxt
    for y in range(len(core.grid)):
        for x in range(len(core.grid[y])):
            visualGridTxt[y][x] = txt_dict.get(str(core.grid[y][x]))

def render_grid_color():
    global visualGridColor
    for y in range(len(core.grid)):
        for x in range(len(core.grid[y])):
            visualGridColor[y][x] = color_dict.get(str(core.grid[y][x]), "#FFFFFF")

visualGridColor = core.create_grid(core.side)
visualGridTxt = core.create_grid(core.side)
render_grid_txt()
render_grid_color()

dx=10 # horizontal distance between labels
dy=10 # vertical distance between labels

labels = core.create_grid(core.side)

main=Tk()
main.title("titre de la fenêtre")
main.geometry("500x600")

top_fr =Frame(main)
top_fr.pack(side=TOP, fill=X)
left_fr = Frame(top_fr)
left_fr.pack(side=LEFT, fill=X)

title_lbl = Label(left_fr, text="2048")
title_lbl.pack()


right_fr = Frame(top_fr)
right_fr.pack(side=RIGHT, fill=X)

score_lbl = Label(right_fr,text="Score : xxx")
score_lbl.pack()

new_btn = Button(right_fr,text="New Game")
new_btn.pack()

game_fr = Frame(main)
game_fr.pack(fill=Y, side=BOTTOM)

for line in range(len(visualGridTxt)):
    for col in range(len(visualGridTxt[line])):
        labels[line][col] = Label (game_fr, text =visualGridTxt[line][col], width=6, height=3, borderwidth=1, relief="solid", font=("Arial", 15), bg=visualGridColor[line][col])
        labels[line][col].grid (row=line+1,column=col,padx=dx,pady=dy)

main.mainloop()
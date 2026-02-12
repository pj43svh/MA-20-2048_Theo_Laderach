# Graphics of the game
# Author : Théo Läderach
# Date : 05.02.2026
# Version : 1.2
import core
core.start_game()

from tkinter import *
import json

dictionnary_file_path = "dictionnary.json"

# Json code come from another project (MA-24)
try:
    with open(dictionnary_file_path, 'r') as json_file:
            dictionnary = json.load(json_file)
except:
    print("Error with open the dictionnary json file")
    exit()

# Dictionnary for the text
txt_dict = dictionnary.get("txt_dict")

# Dictionnary for the color.
# the first is the background color and the second the border color
color_dict = dictionnary.get("color_dict")

# Set the font of the game.
# If the user haven't the font minecraft, it use the font Arial
try:
    DEFAULT_FONT = "Minecraft"
except:
    DEFAULT_FONT = "Arial"

# Function who place the text on the front-end grid 
# by using the back-end grid and the dictionnary.
def render_grid_txt():
    global visualGridTxt
    for y in range(len(core.grid)):
        for x in range(len(core.grid[y])):
            # replace every item in the list using the disctionnary
            visualGridTxt[y][x] = txt_dict.get(str(core.grid[y][x]))

# Function who place the color on the front-end grid 
# by using the back-end grid and the dictionnary.
def render_grid_color():
    global visualGridColor
    for y in range(len(core.grid)):
        for x in range(len(core.grid[y])):
            # replace every item in the list using the disctionnary
            visualGridColor[y][x] = color_dict.get(str(core.grid[y][x]), "#FFFFFF")

# Create the Front-end grid referring to the back-end grid
visualGridColor = core.create_grid(core.side)
visualGridTxt = core.create_grid(core.side)


render_grid_txt() # Initialise the text front-end grid
render_grid_color() # Initialise the color front-end grid

dx=5 # horizontal distance between labels
dy=5 # vertical distance between labels

labels = core.create_grid(core.side)

main=Tk()
main.title(txt_dict.get("title","2048"))
main.geometry("450x550")


top_fr =Frame(main)
top_fr.pack(side=TOP, fill=X)

left_fr = Frame(top_fr)
left_fr.pack(side=LEFT,padx=30,pady=30,ipady=0,ipadx=0)

title_lbl = Label(left_fr, text=txt_dict.get("title","2048"),font=(DEFAULT_FONT,52,"bold"),fg=color_dict.get("title","#df0000"))
title_lbl.pack()


right_fr = Frame(top_fr)
right_fr.pack(side=RIGHT, fill=X,padx=30,pady=20,ipady=0)

score_fr = Frame(right_fr)
score_fr.pack()

score_txt_lbl = Label(score_fr,text="Score : ",font=(DEFAULT_FONT,18))
score_txt_lbl.pack(side=LEFT)

score_num_lbl = Label(score_fr,text="xxx",font=(DEFAULT_FONT,18,"bold"))
score_num_lbl.pack(side=RIGHT)

new_btn = Button(right_fr,text="New Game",font=(DEFAULT_FONT,12))
new_btn.pack()

game_fr = Frame(main, bg="#D0D4D4")
game_fr.pack(fill=Y, side=BOTTOM, padx=10,pady=10)

# Create the pawn on the windows using the grid
for line in range(len(visualGridTxt)):
    for col in range(len(visualGridTxt[line])):
        background_color,border_color=visualGridColor[line][col]
        case = Frame(game_fr,bg=border_color)
        case.grid (row=line+1,column=col,padx=dx,pady=dy)
        labels[line][col] = Label (case,
                                    text =visualGridTxt[line][col],
                                    width=6,
                                    height=3,
                                    font=(DEFAULT_FONT, 15),
                                    bg=background_color)
        labels[line][col].pack(padx=3,pady=3)


main.mainloop()
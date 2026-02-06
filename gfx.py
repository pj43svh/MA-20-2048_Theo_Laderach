# Graphics of the game
# Author : Théo Läderach
# Date : 05.02.2026
# Version : 1.0
import core
core.start_game()

from tkinter import *



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

# Dictionnary for the color.
# the first is the background color and the second the border color
color_dict = {
    "0": ("#C4CBCB","#C4CBCB"),
    "1": ("#48B64B","#3D9B41"),
    "2": ("#4CC89C","#41AC86"),
    "3": ("#58C9DA","#4EB2C2"),
    "4": ("#4261C2","#3D59AD"),
    "5": ("#964ED4","#8B4AC4"),
    "6": ("#DD45CF","#C43EB6"),
    "7": ("#E52222","#D12121"),
    "8": ("#FF6308","#E25808"),
    "9": ("#FFC408","#E7B40A"),
    "10": ("#FFFA08","#E0DD0A"),
    "11": ("#B2FF08","#9FE40A"),
    "12": ("#43FF08","#3FE60D"),
    "13": ("#08FBFF","#0FE2E6")
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

dx=5 # horizontal distance between labels
dy=5 # vertical distance between labels

labels = core.create_grid(core.side)

main=Tk()
main.title("titre de la fenêtre")
main.geometry("450x550")

top_fr =Frame(main)
top_fr.pack(side=TOP, fill=X)
left_fr = Frame(top_fr)
left_fr.pack(side=LEFT,padx=30,pady=30,ipady=0,ipadx=0)

title_lbl = Label(left_fr, text="2048",font=("Minecraft",52,"bold"),fg="#df0000")
title_lbl.pack()


right_fr = Frame(top_fr)
right_fr.pack(side=RIGHT, fill=X,padx=30,pady=20,ipady=0)

score_fr = Frame(right_fr)
score_fr.pack()

score_txt_lbl = Label(score_fr,text="Score : ",font=("Minecraft",18))
score_txt_lbl.pack(side=LEFT)

score_num_lbl = Label(score_fr,text="xxx",font=("Minecraft",18,"bold"))
score_num_lbl.pack(side=RIGHT)

new_btn = Button(right_fr,text="New Game",font=("Minecraft",12))
new_btn.pack()

game_fr = Frame(main, bg="#D0D4D4")
game_fr.pack(fill=Y, side=BOTTOM, padx=10,pady=10)

for line in range(len(visualGridTxt)):
    for col in range(len(visualGridTxt[line])):
        background_color,border_color=visualGridColor[line][col]
        case = Frame(game_fr,bg=border_color)
        case.grid (row=line+1,column=col,padx=dx,pady=dy)
        labels[line][col] = Label (case,
                                    text =visualGridTxt[line][col],
                                    width=6,
                                    height=3,
                                    font=("Minecraft", 15),
                                    bg=background_color)
        labels[line][col].pack(padx=3,pady=3)

main.mainloop()
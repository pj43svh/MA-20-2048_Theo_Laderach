# Graphics of the game
# Author : Théo Läderach
# Date : 12.02.2026
# Version : 1.3
import core

from tkinter import *
import json
import os
from PIL import ImageTk, Image
from tkinter import filedialog

# code to get the current directory to retrieve the dictionary.json file
# Search: How to open a file from any directory in Python
# https://www.reddit.com/r/learnpython/comments/fpegxj/how_to_make_my_python_script_portable_when_it/?tl=fr#:~:text=Section%20des%20commentaires&text=Pour%20un%20script%20tr%C3%A8s%20simple,le%20r%C3%A9pertoire%20que%20tu%20veux   

# we will look for the path to the gfx.py file
current_dir = os.path.dirname(os.path.abspath(__file__)) 
# We'll add it before the sectionary.json file to ensure the correct path.
dictionnary_file_path = os.path.join(current_dir, "dictionnary.json") 

# I use Json to edit constant variables more easily

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
# Please, install the font Minecraft.ttf
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
            visualGridColor[y][x] = color_dict.get(str(core.grid[y][x]), "#FF0000")


def refresh_labels_grid():
    render_grid_txt()
    render_grid_color()
    for line in range(len(visualGridTxt)):
        for col in range(len(visualGridTxt[line])):
            background_color,border_color=visualGridColor[line][col]
            labels[line][col].config(text =visualGridTxt[line][col],
                                        bg=background_color)
            labelBackground[line][col].config(bg=border_color)
            

def refresh_score():
    score_num_lbl.config(text=core.score)

def refresh_combo():
    img_num = str(core.combo) if core.combo <=35 else 35
    image_path = os.path.join(current_dir, "combo", f"cup-{img_num}.png")
    try:
        combo_img = ImageTk.PhotoImage(Image.open(image_path).resize((70,70)))
    except Exception as e:
        print("Error loading combo image:", e)
        combo_img = None

    combo.config(image=combo_img,bg=dictionnary.get("break_color").get(str(core.failComboAttempt)))
    combo.image = combo_img

    combo_txt.config(text=core.combo)

def refresh_screen():
    """
    This function refresh all the widget when the player play or reste the game
    """
    refresh_labels_grid()
    refresh_score()
    refresh_combo()


def start_game(main):
    global visualGridColor, visualGridTxt
    
    core.start_game()

    visualGridColor = core.create_grid(core.SIDE,fill=0)
    visualGridTxt = core.create_grid(core.SIDE,fill=0)

    render_grid_txt() # Initialise the text front-end grid
    render_grid_color() # Initialise the color front-end gridgfx.open_windows()
        
    open_windows(main)

def open_windows(main):
    global score_num_lbl,labels,labelBackground, combo, combo_txt

    
    # Create the Front-end grid referring to the back-end grid
    
    dx=5 # horizontal distance between labels
    dy=5 # vertical distance between labels

    # Grid of the labels on the screen
    labels = core.create_grid(core.SIDE, fill=None)
    labelBackground = core.create_grid(core.SIDE, fill=None)


    top_fr =Frame(main)
    top_fr.pack(side=TOP, fill=X)

    left_fr = Frame(top_fr)
    left_fr.pack(side=LEFT,padx=30,pady=30,ipady=0,ipadx=0)

    title_lbl = Label(left_fr,
                       text=txt_dict.get("title","2048"),
                       font=(DEFAULT_FONT,52,"bold"),
                       fg=color_dict.get("title","#f90303"))
    title_lbl.pack()

    theme = IntVar()
    theme_cb = Checkbutton(left_fr,
                            text="Dark theme",
                            variable=theme,
                            onvalue=1,
                            offvalue=0,
                            command=lambda : changeTheme(main,theme))
    theme_cb.pack()


    right_fr = Frame(top_fr)
    right_fr.pack(side=RIGHT, fill=X,padx=0,pady=0,ipady=0)

    score_fr = Frame(right_fr)
    score_fr.pack()

    score_txt_lbl = Label(score_fr,
                          text="Score : "
                          ,font=(DEFAULT_FONT,18))
    score_txt_lbl.pack(side=LEFT)

    score_num_lbl = Label(score_fr,
                          text="0",
                          font=(DEFAULT_FONT,18,"bold"))
    score_num_lbl.pack(side=RIGHT)

    new_btn = Button(right_fr,
                     text="New Game",
                     font=(DEFAULT_FONT,12),
                     command=newGame)
    new_btn.pack()

    # search on stackoverflow : how to add an image in tkinter ?
    image_combo_path = os.path.join(current_dir, "combo", "cup-0.png")
    try:
        combo_img = ImageTk.PhotoImage(Image.open(image_combo_path).resize((70,70)))
    except Exception as e:
        print("Error loading combo image:", e)
        combo_img = None

    combo = Label(top_fr, image=combo_img,bg="#BABEBE")
    combo.image = combo_img
    combo.place(x=200,y=85)

    combo_txt = Label(top_fr,text="0",font=(DEFAULT_FONT,18,"bold"),bg="#BABEBE")
    combo_txt.place(x=200,y=140)


    game_fr = Frame(main, 
                    bg="#D0D4D4")
    game_fr.pack(fill=Y, side=BOTTOM, padx=10,pady=10)

    # Create the pawn on the windows using the grid
    for line in range(len(visualGridTxt)):
        for col in range(len(visualGridTxt[line])):

            background_color,border_color=visualGridColor[line][col]

            labelBackground[line][col] = Frame(game_fr,bg=border_color)
            labelBackground[line][col].grid(row=line+1,column=col,padx=dx,pady=dy)

            labels[line][col] = Label (labelBackground[line][col],
                                        text =visualGridTxt[line][col],
                                        width=5,
                                        height=3,
                                        font=(DEFAULT_FONT, 19),
                                        bg=background_color
                                        )
            
            labels[line][col].pack(padx=5,pady=5)

    main.bind("<KeyRelease-a>",func=leftPressed)
    main.bind("<KeyRelease-Left>",func=leftPressed)
    main.bind("<KeyRelease-w>",func=upPressed)
    main.bind("<KeyRelease-Up>",func=upPressed)
    main.bind("<KeyRelease-d>",func=rightPressed)
    main.bind("<KeyRelease-Right>",func=rightPressed)
    main.bind("<KeyRelease-s>",func=downPressed)
    main.bind("<KeyRelease-Down>",func=downPressed)

    main.mainloop()


def Play(direction):
    """
    """
    if direction == "left":
        temp_grid = core.playLeft(core.grid)
    elif direction == "right" :
        temp_grid = core.playRight(core.grid)
    elif direction == "up" :
        temp_grid = core.playUp(core.grid)
    elif direction == "down" :
        temp_grid = core.playDown(core.grid)
    
    if not temp_grid:
        print("nothing can move")
    else:
        core.grid = temp_grid
        core.spawn_rdm(core.grid,core.SIDE)
    refresh_screen()


def leftPressed(event):
    Play("left")

def upPressed(event):
    Play("up")

def rightPressed(event):
    Play("right")

def downPressed(event):
    Play("down")

#print(core.rotate_grid("down",[[0, 1, 1, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]))
#print((core.rotate_grid("down",core.rotate_grid("down",[[0, 1, 1, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]))))
#
#print(core.rotate_grid("up",[[0, 1, 1, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]))

def newGame():
    core.failComboAttempt = 0
    core.combo=0
    core.score = 0
    core.start_game()
    refresh_screen()
    return

def changeTheme(win,theme):
    if theme.get() == 1:
        win.configure(background="#313131")
        
    elif theme.get() == 0 :
        win.configure(background="#D9D9D9")
    else :
        print("error")
    print("checkbutton change",win,theme.get())



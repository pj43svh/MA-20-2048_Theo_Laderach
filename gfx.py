# Graphics of the game
# Author : Théo Läderach
# Date : 17.03.2026
# Version : 1.3 Main version
import core

from tkinter import *
from tkinter import messagebox
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

# At the start, player never has 2048.
alreadyHave2048 = False

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
            visualGridColor[y][x] = color_dict.get(str(core.grid[y][x]), ["#FF0000","#000000"])


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
    """
    Creation of the windows and the grid on the interface
    """
    global score_num_lbl,labels,labelBackground, combo, combo_txt,title_lbl

    
    # Create the Front-end grid referring to the back-end grid
    
    dx=5 # horizontal distance between labels
    dy=5 # vertical distance between labels

    # Grid of the labels on the screen
    labels = core.create_grid(core.SIDE, fill=None)
    labelBackground = core.create_grid(core.SIDE, fill=None)


    top_fr =Frame(main,height=159)
    top_fr.pack(side=TOP, fill=X)


    title_lbl = Label(top_fr,
                       text=txt_dict.get("title","2048"),
                       font=(DEFAULT_FONT,52,"bold"),
                       fg=color_dict.get("title","#f90303"))
    title_lbl.place(x=20,y=30)

    theme = BooleanVar()
    theme_cb = Checkbutton(top_fr,
                            text="Dark theme",
                            variable=theme,
                            onvalue=True,
                            offvalue=False,
                            command=lambda : changeTheme(main,theme,widget=[top_fr, theme_cb,score_num_lbl,score_txt_lbl,game_fr]))
    theme_cb.place(x=60,y=100)


    

    score_txt_lbl = Label(top_fr,
                          text="Score : "
                          ,font=(DEFAULT_FONT,15))
    score_txt_lbl.place(x=275,y=30)

    score_num_lbl = Label(top_fr,
                          text="0",
                          font=(DEFAULT_FONT,18,"bold"))
    score_num_lbl.place(x=350,y=30)

    new_btn = Button(top_fr,
                     text="New Game",
                     font=(DEFAULT_FONT,12),
                     width=15,height=1,
                     bg="#717171",activebackground="#8B8B8B",
                     command=newGame)
    new_btn.place(x=280,y=70)

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
    combo_txt.place(x=200,y=135)


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
    main.bind("<Escape>",func=cheatCode)



def Play(direction):
    """
    A function allowing play in different directions,
    the new tiles appear,
    and the end of the game is checked.
    """
    global alreadyHave2048
    # Check if the player made a 2048
    if direction == "left":
        temp_grid,temp_score = core.playLeft(core.grid)
    elif direction == "right" :
        temp_grid,temp_score = core.playRight(core.grid)
    elif direction == "up" :
        temp_grid,temp_score = core.playUp(core.grid)
    elif direction == "down" :
        temp_grid,temp_score = core.playDown(core.grid)
    
    if not temp_grid:
        print("nothing can move")
    else:
        core.score += temp_score
        core.grid = temp_grid
        core.spawn_rdm(core.grid,core.SIDE)
    refresh_screen()

    # Ckeck if you have already win
    if not alreadyHave2048 :
        # if not, verify all the grid to found if it have a 2048
        for row in core.grid:
            # 11 is 2048 in the dictionnary
            if 11 in row:
                alreadyHave2048 = True
                # ask you if you want to continue again or reset the
                if not messagebox.askyesno("You Won !","YOU WON !!!\nYou obtained a 2048 !\nDo you want to continue playing ?"):
                    newGame()
                    return
                
    # Game over conditions:
    # Check if the grid has empty case
    if not core.checkEmptyCase(core.grid,core.SIDE):
        # verify if you can move
        if not core.playUp(core.grid,NoScore=True) and not core.playDown(core.grid,NoScore=True) and not core.playLeft(core.grid,NoScore=True) and not core.playRight(core.grid,NoScore=True) :
        # if you can't move, it's game over.
            print("Game over")
            if messagebox.askretrycancel("Game Over", f"GAME OVER !\nDo you want retry ?\nScore : {core.score}") :
                newGame()
            else:
                exit()
            return
    

    return



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
    """
    reset the game grid, the score and the interface
    """
    global alreadyHave2048
    core.failComboAttempt = 0
    core.combo=0
    
    alreadyHave2048 = False
    core.score = 0
    core.start_game()
    refresh_screen()
    return

def changeTheme(win,theme,widget=[]):
    """
    Function who change the theme when the checkbutton is checked or not
    """
    darkBGcolor = "#313131"
    lightBGcolor = "#EEEDED"
    if theme.get() == True:
        win.configure(background=darkBGcolor)
        title_lbl.config(bg=darkBGcolor)
        for i in widget :
            i.config(bg=darkBGcolor)
            try:
                i.config(fg="white")
            except:
                pass

    elif theme.get() == False :
        win.configure(background=lightBGcolor)
        title_lbl.config(bg=lightBGcolor)
        for i in widget:
            i.config(bg=lightBGcolor)
            try:
                i.config(fg="black")
            except:
                pass
    else :
        print("error")
    print("checkbutton change",win,theme.get())


def cheatCode(event):
    cheatcode_windows = Tk()
    cheatcode_windows.attributes('-topmost', True)
    cheatcode_windows.title("Cheatcode")

    Label(cheatcode_windows,text="Enter a cheat code :").pack(padx=10,pady=10)
    cmd_fr = Frame(cheatcode_windows)
    cmd_fr.pack(fill=X,pady=5)
    Label(cmd_fr,text="Command :").pack(padx=5,side=LEFT)
    cheatcode_entry = Entry(cmd_fr)
    cheatcode_entry.pack(padx=10,pady=10,side=RIGHT)

    arg_fr=Frame(cheatcode_windows)
    arg_fr.pack(fill=X,pady=5)
    Label(arg_fr,text="Argument").pack(padx=5,side=LEFT)
    arg_entry = Entry(arg_fr)
    arg_entry.pack(padx=10,pady=10,side=RIGHT)

    btn_frame = Frame(cheatcode_windows)
    btn_frame.pack(fill=X)
    Button(btn_frame,text="Execute",bg="lime",command=lambda: execute_cheatcode(cheatcode_windows,cheatcode_entry,arg_entry)).pack(side=LEFT,padx=10,pady=10)
    Button(btn_frame,text="Close",bg="red", command=lambda: cheatcode_windows.destroy()).pack(side=RIGHT,padx=10,pady=10)

def execute_cheatcode(win,command_entry,argument_entry):
    command_list = {
        "moveRDM": moveRDM,
        "restart": newGame,
        "spawn":spawn_number,
        "debugMode":switch_to_test_mode,
        "setCombo": setCombo,
        "setScore": setScore,
        "list": displayList
    }
    command = command_entry.get()
    argument = argument_entry.get()

    if command in command_list:
        if argument =="":
            command_list[command]()
        else:
            command_list[command](argument)
        win.destroy()
    else :
        messagebox.showinfo("Command error", "invalid commande name")

        
        
    return

def moveRDM(rep):
    import random
    for i in range(int(rep)):
        move = random.choice(["left","right","up","down"])
        Play(move)
    return

def spawn_number(num):
    if num == "random":
        core.spawn_rdm(core.grid,core.SIDE)
    else:
        try:
            num = int(num)
        except:
            messagebox.showwarning("WARING", "The value must be random or an integer between 1 to 13")
            
        if not 0 < num <= 13:
            messagebox.showwarning("WARING", "The value must be random or an integer between 1 to 13")
            return
        from random import randint

        rdmX = randint(0,core.SIDE-1)
        rdmY = randint(0,core.SIDE-1)
        
        while core.grid[rdmX][rdmY]:
            rdmX = randint(0,core.SIDE-1)
            rdmY = randint(0,core.SIDE-1)
        print("empty case at",rdmX,rdmY)
        core.grid[rdmX][rdmY]=num
    refresh_screen()
    return

def switch_to_test_mode():
    core.TEST_MODE = not core.TEST_MODE
    newGame()

def setCombo(num):
    core.combo = int(num)
    core.failComboAttempt = 0
    refresh_screen()

def setScore(num):
    core.score = num
    refresh_screen()

def displayList():
    messagebox.showinfo("List of command","""moveRDM: move randomely
restart: restart the game
spaw:spawn the number of your choice (1-13)
debugMode: set the grid to normal or all the number
setCombo: set the number of Combo
setScore: setthe score Score
list: show all the command""")
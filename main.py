# Main file
# Author : Théo Läderach
# Date : 12.02.2026
# Version : 1.1 Main version

from tkinter import *

main=Tk()
main.title("2048")
main.geometry("450x580")

# the window is unresizable
main.resizable(width=0,height=0)



import gfx

gfx.start_game(main)


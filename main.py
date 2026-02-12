#  Main file
# Author : Théo Läderach
# Date : 12.02.2026
# Version : 1.0

# Import of the graphics file

from tkinter import *

main=Tk()
main.title("2048")
main.geometry("450x580")



import gfx

gfx.start_game(main)


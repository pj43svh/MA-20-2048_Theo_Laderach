# Mechanics of the game
# Author : Théo Läderach
# Date : 05.02.2026
# Version : 1.1

def create_grid(side):
    grid = []
    for i in range(side):
        row = []
        for j in range(side):
            row.append(0)
        grid.append(row)

    return grid

def spawn_rdm(grid,side):
    from random import randint

    rdmX = randint(0,side-1)
    rdmY = randint(0,side-1)

    if randint(1,10) == 10 :
        num = 2
    else:
        num = 1
    while grid[rdmX][rdmY]:
        rdmX = randint(0,side-1)
        rdmY = randint(0,side-1)
    return rdmX,rdmY,num

def start_game():
    global grid
    grid = create_grid(side)

    default_pawn = 2
    for i in range(default_pawn):
        rdmX,rdmy,num = spawn_rdm(grid,side)
        grid[rdmX][rdmy]=num
    print(grid)

side = 4


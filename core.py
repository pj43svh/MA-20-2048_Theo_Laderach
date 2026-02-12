# Mechanics of the game
# Author : Théo Läderach
# Date : 12.02.2026
# Version : 1.3


SIDE = 4

score=0

def create_grid(side, fill=None):
    """
    Create a square grid made of list and fill with the parameter fill
    code come from another project (MA-24)
    """
    grid = []
    for line in range(side):
        row = []
        for col in range(side):
            row.append(fill)
        grid.append(row)

    return grid

def spawn_rdm(grid,side):
    """
    Function who spawn randomly the number 2 or 4 on the empty case
    """
    empty_case = False
    for line in range(side):
        for col in range(side):
            if grid[line][col] == 0:
                empty_case=True

    if not empty_case:
        print("Any empty case")
        return False
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
    print("empty case at",rdmX,rdmY)
    grid[rdmX][rdmY]=num
    return True

def start_game():
    """
    creation of the grid and sapwn the default number
    """
    global grid
    # Turn the TEST_MODE to True to see the color of all number
    TEST_MODE = False

    if TEST_MODE:
        grid = [[1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12],
                [13, 0, 0, 0]]
    else:
        grid = create_grid(SIDE, fill=0)

        default_pawn = 2
        for i in range(default_pawn):
            spawn_rdm(grid,SIDE)
        print(grid)
    


def leftPressed(event):
    global score
    if spawn_rdm(grid,SIDE):
        score += 1
        

    from gfx import refresh_screen
    refresh_screen()

    print("refresh")
    


def upPressed(event):
    print("up is pressed")


def rightPressed(event):
    print("right is pressed")


def downPressed(event):
    print("down is pressed")
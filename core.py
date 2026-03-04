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
        #grid = [[1, 1, 1, 1], [0, 1, 1, 0], [1, 0, 0, 1], [1, 1, 1, 0]]
    else:
        grid = create_grid(SIDE, fill=0)

        default_pawn = 2
        for i in range(default_pawn):
            spawn_rdm(grid,SIDE)
        print(grid)
    
def play(direction,temp_grid):


    temp_grid = rotate_grid(direction,temp_grid)
    if not temp_grid :
        print("erreur lors de la modification de la grille")
        return
    print(temp_grid)
    
    for row in range(len(temp_grid)) :
        # moving
        temp_grid[row][0],temp_grid[row][1],temp_grid[row][2],temp_grid[row][3] = pack4(temp_grid[row][0],temp_grid[row][1],temp_grid[row][2],temp_grid[row][3])    
    
    print(temp_grid)
    return rotate_grid(direction,temp_grid)
    
def rotate_grid(direction,grid):
    if direction == "left":
        return grid

    elif direction =="right":
        for row in range(len(grid)) :
            grid[row] = grid[row][::-1]

    elif direction == "up" :
        grid2, grid = grid, [[],[],[],[]]
        for row in range(len(grid2)):
            for col in range(len(grid2[row])):
                grid[row].append(grid2[col][row])

    elif direction == "down" :
        grid2, grid = grid, [[],[],[],[]]
        for row in range(len(grid2)):
            for col in range(len(grid2[row])):
                grid[row].append(grid2[col][row])
        for row in range(len(grid)) :
            grid[row] = grid[row][::-1]
        grid=grid[::-1]

    else:
        return

    return grid

def pack4(a,b,c,d):

    # move
    if c == 0:
        c, d = d, 0
    if b == 0:
        b, c, d = c, d, 0
    if a == 0:
        a, b, c, d = b, c, d, 0
   
   # merge
    if c == d and c != 0:
        c,d = c + 1,0
    if a == b and a != 0:
        a,b,c,d = a + 1,c,d,0
        
    if b == c and b != 0:
        b,c,d = b + 1,d,0
    
        
    return a,b,c,d
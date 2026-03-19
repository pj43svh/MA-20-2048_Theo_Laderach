# Mechanics of the game
# Author : Théo Läderach
# Date : 17.03.2026
# Version : 1.3 Main version


SIDE = 4

score=0

combo = 0

failComboAttempt = 0

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

    # We check if it's empty case on the grid
    if not checkEmptyCase(grid,side) :
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

def checkEmptyCase(grid,side):
    """
    Function who check if it's empty case on the grid
    """
    empty_case = False
    for line in range(side):
        for col in range(side):
            if grid[line][col] == 0:
                empty_case=True

    return empty_case

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
        #grid = [[10, 10, 0, 1],
        #        [0, 0, 0, 1], 
        #        [0, 0, 0, 2], 
        #        [0, 0, 0, 3]]
    else:
        grid = create_grid(SIDE, fill=0)

        default_pawn = 2
        for i in range(default_pawn):
            spawn_rdm(grid,SIDE)
        print(grid)
    

def playLeft(temp_grid,NoScore =False):
    """
    Function that allows you to move the grid
    to the left with movement and merging thanks to pack4
    """
    # this variable is needed after for checking if something change.
    nothing_change = True
    merged = False

    score=0

    # Use the Function pack4 for each lines to the left
    for row in range(4) :
            temp_grid[row][0],temp_grid[row][1],temp_grid[row][2],temp_grid[row][3],change,merge,temp_score = pack4(temp_grid[row][0],temp_grid[row][1],temp_grid[row][2],temp_grid[row][3])
            # check if something change
            if change > 0:
                # something change
                nothing_change = False
                score += temp_score
            if merge !=0 :
                merged = True
    
    checkCombo(merged)


    if nothing_change:
        result = False
    else:                   
        result = temp_grid

    if not NoScore :
        result= result,score

    return result

def playRight(temp_grid,NoScore =False) :
    """
    Function that allows you to move the grid
    to the right with movement and merging thanks to pack4.
    To understand the function, read playLeft()
    """
    nothing_change = True
    merged = False

    score = 0

    for row in range(4) :
            temp_grid[row][3],temp_grid[row][2],temp_grid[row][1],temp_grid[row][0],change,merge,temp_score = pack4(temp_grid[row][3],temp_grid[row][2],temp_grid[row][1],temp_grid[row][0])
            if change > 0:
                #something change
                nothing_change = False
            if merge != 0:
                merged = True
                score += temp_score
    
    checkCombo(merged)

    if nothing_change:
        result = False
    else:                   
        result = temp_grid

    if not NoScore :
        result= result,score

    return result

def playUp(temp_grid,NoScore =False):
    """
    Function that allows you to move the grid
    to the up with movement and merging thanks to pack4.
    To understand the function, read playLeft()
    """

    merged = False
    nothing_change = True
    score = 0
    for row in range(4) :
            temp_grid[0][row],temp_grid[1][row],temp_grid[2][row],temp_grid[3][row],change,merge,temp_score = pack4(temp_grid[0][row],temp_grid[1][row],temp_grid[2][row],temp_grid[3][row])
            if change > 0:
                #something change
                nothing_change = False
                score += temp_score

            if merge != 0:
                merged = True

    checkCombo(merged)

    if nothing_change:
        result = False
    else:                   
        result = temp_grid

    if not NoScore :
        result= result,score

    return result

def playDown(temp_grid,NoScore =False):
    """
    Function that allows you to move the grid
    to the down with movement and merging thanks to pack4.
    To understand the function, read playLeft()
    """
    nothing_change = True
    merged = False

    score = 0

    for row in range(4) :
            temp_grid[3][row],temp_grid[2][row],temp_grid[1][row],temp_grid[0][row],change,merge,temp_score = pack4(temp_grid[3][row],temp_grid[2][row],temp_grid[1][row],temp_grid[0][row])
            if change > 0:
                #something change
                nothing_change = False
                score += temp_score
                
            if merge != 0:
                merged = True
    
    checkCombo(merged)

    if nothing_change:
        result = False
    else:                   
        result = temp_grid

    if not NoScore :
        result= result,score

    return result
    

def pack4(a,b,c,d):
    """
    function allowing you to move 
    or merge numbers in a single line.
    """
    # the change and the temp_score is to 0 at the begining
    change = 0
    temp_score = 0

    # MOVING
    # the black squre 0, is the empty space

    # we move only the last number :
    # 4,8,0,16 => 4,8,16,0
    if c == 0 and d != 0:
        c, d = d, 0
        # if something move, we add one change
        change += 1

    # we move the two last number :
    # 4,0,8,16 => 4,8,16,0
    if b == 0 and (c!= 0 or d!= 0):
        b, c, d = c, d, 0
        change += 1
    # we move only the last number :
    # 0,4,8,16 => 4,8,16,0
    if a == 0 and (b != 0 or c!= 0 or d!= 0):
        a, b, c, d = b, c, d, 0
        change += 1
   

   # MERGING
    merge = 0
    # we merge the 2 last number :
    # 16,8,2,2 => 16,8,4,0
    if c == d and c != 0:
        c,d = c + 1,0
        change += 1
        merge += 1
        temp_score += 2**c

    # we merge the 2 middle number :
    # 16,2,2,8 => 16,4,8,0
    if a == b and a != 0:
        a,b,c,d = a + 1,c,d,0

        change += 1
        merge += 1
        temp_score += 2**a

    # we merge the 2 first number :
    # 2,2,16,8 => 4,16,8,0
    if b == c and b != 0 and merge == 0:
        b,c,d = b + 1,d,0
        change += 1
        merge += 1
        temp_score += 2**b
    
        
    return a,b,c,d, change,merge,temp_score

def checkCombo(merged):
    global combo, failComboAttempt

    if merged:
        combo += 1
    else:
        if combo > 0:
            failComboAttempt += 1
            if failComboAttempt > 3:
                combo = 0
                failComboAttempt = 0
###############################################################################
# Mohammd AlKharaan
# CPS-311 project-05
# Solving a maze
# Problem 2: Maze Solver

##
#  ## No backtracking ## 
# I could have used Recursion, but I think the
# whole point of using stacks is not using recursion
# in other words, if solvable by recursion, you can solve it
# by using stacks
##
from grid import *
from arraystack import *

def RowsCols(file):
    ''' Function RowsCols(file):
        opens the file.
        go over the file line by line
        counts the rows and cols
        returns a tuple
    '''
    with open(file) as f:
        grid_data = [i.rstrip() for i in f.readlines()]
        # comprehension comes handy sometimes
    return(len(grid_data),len(grid_data[0]))



def readPopulate(file):
    ''' Function readPopulate(file):
        takes the file as argumenet.
        calls RowsCols function
        creates Grid object
        loop through file
        populate the date from file to the grid
        returns grid object
    '''

    rowsCols = RowsCols(file)
    mazeGrid = Grid(rowsCols[0], rowsCols[1]+1)
    with open(file) as f:
        # loop through the data
        for i, line in enumerate(f.readlines()):
            # populate
            for j, value in enumerate(line):
                if value == '*':
                    value = '-'
                mazeGrid[i][j] = value
        return mazeGrid


def findP(grid):
    ''' Function findP(grid):
        loops through the grid
        finds P
        return tuple of P location
    '''
    for i in range(grid.getHeight()):
        for k in range(grid.getWidth()):
            if grid[i][k] == 'P':
                return(i,k)


def solveMaze(p,grid):
    ''' function solveMaze(p,grid):
        takes p, grid as arguements
        creates an ArrayStack()
        pushes P location to the stack
        while stack is not empty:
            pop an item
            if cell is not +
               change it to +
               check adjecent cells for spaces
               push thier locations to my stack
               and go back to the top of the loop
        returns the modified grid
    '''
    myStack = ArrayStack()
    myStack.push (p)
    while not myStack.isEmpty():
        x,y = myStack.pop()
        if grid[x+1][y] == ' ':
            grid[x+1][y] = '+'
            myStack.push( (x+1,y) )
        if grid[x][y+1] == ' ':
            grid[x][y+1] = '+'
            myStack.push( (x,y+1) )
        if grid[x-1][y] == ' ':
            grid[x-1][y] = '+'
            myStack.push( (x-1,y ))
        if grid[x][y-1] == ' ':
            grid[x][y-1] = '+'
            myStack.push( (x,y-1) )
        if grid[x+1][y] == 'T' or\
           grid[x][y+1] == 'T' or\
           grid[x-1][y] == 'T' or\
           grid[x][y-1] == 'T':
            print('SLOUTION FOUND!')



    return grid

def backTrack(grid,t,x,y):
    ''' For backtracking, no luck figureing it out
    '''
    myStack = ArrayStack()
    myStack.push (t)
    while not myStack.isEmpty():
        x,y = myStack.pop()
        if moreOptions(grid,x+1,y):
            pass


def moreOptions(grid, x,y):
    ''' an attempt to find more than one cell to go to.
        This was done for backtracking, but no luck!.
        This function would mark each cell which from
        you can go to more a direction
    '''
    if grid[x][y] == '+':
        if grid[x][y+1] == ' ' and\
           grid[x+1][y] == ' ':
            options.append((x,y))
            return True
        if grid[x+1][y] == ' ' and\
           grid[x][y-1] == ' ':
            options.append((x,y))
            return True
        if grid[x][y-1] == ' ' and\
           grid[x-1][y] == ' ':
            options.append((x,y))
            return True
        if grid[x-1][y] == ' ' and\
           grid[x][y+1] == ' ':
            options.append((x,y))
            return True
        if grid[x][y+1] == ' ' and\
           grid[x][y-1] == ' ':
            options.append((x,y))
            return True
        if grid[x+1][y] == ' ' and\
           grid[x-1][y] == ' ':
            options.append((x,y))
            return True



### Main program ###
def main():
    validInput = True
    while validInput:
        try:
            userMaze = str(input('Enter the file name: '))
            viewMaze = open(userMaze, 'r')
            gridData = readPopulate(userMaze)
            print('GIVEN MAZE: ')
            print(gridData)
            while validInput:
                solvemaze = str(input('<enter> to see the sloution '))
                if solvemaze == '':
                    p = findP(gridData)
                    mazeSloution = solveMaze(p,gridData)
                    print(mazeSloution)
                    validInput = False # to breake after one round of loop
                else:
                    print('You must press enter to see sloution')
                    continue
        except FileNotFoundError:
            print('File name is not correct')
            print()
            print('Try again')
            print()
            continue # go back to top of the loop and re-prompt
        except IndexError:
            print('Kindly, change the chosen file')
            print()
            # rose-maze, phillips-maze wont't open with my code
            # I tried strip() and rstip() but those files are
            # pain in the neck!
            continue

if __name__ == '__main__':
    main()




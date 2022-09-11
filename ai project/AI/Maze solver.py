import turtle                    # import turtle library
import time
import sys
from collections import deque

wn = turtle.Screen()               # define the turtle screen
wn.bgcolor("black")                # set the background colour
wn.title("MAZE SOLVER USING BFS & BACKTRACKING")
wn.setup(1200,660)                  # setup the dimensions of the working window


# this is the class for the Maze
class Maze(turtle.Turtle):               # define a Maze class
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")            # the turtle shape
        self.color("gold")             # colour of the turtle
        self.penup()                    # lift up the pen so it do not leave a trail / Positional argument
        self.speed(0)

# this is the class for the finish line - green square in the maze
class Green(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("turtle")
        self.color("green")
        self.penup()
        self.speed(0)

class Cyan(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("blue")
        self.penup()
        self.speed(0)


# this is the class for the yellow or turtle
class Red(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("arrow")
        self.color("red")
        self.penup()
        self.speed(0)

class Crimson(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("circle")
        self.color("crimson")
        self.penup()
        self.speed(0)

grid1= [
"+++++++++++++++",
"+s+       + +e+",
"+ +++++ +++ + +",
"+ + +       + +",
"+ +   +++ + + +",
"+ + + +   + + +",
"+   + +   + + +",
"+++++ +   + + +",
"+     +   +   +",
"+++++++++++++++",
]

grid2= [
"+++++++++",
"+ ++s++++",
"+ ++ ++++",
"+ ++ ++++",
"+    ++++",
"++++ ++++",
"++++ ++++",
"+      e+",
"+++++++++",
]

grid3= [
"+++++++++++++++",
"+          e  +",
"+             +",
"+             +",
"+             +",
"+             +",
"+             +",
"+             +",
"+ s           +",
"+++++++++++++++",
]

grid4= [
"+++++++++++++++++++++++++++++++++++++++++++++++++++",
"+             ++                                  +",
"+  ++++++++++  +++++++++++++  +++++++  ++++++++++++",
"+          +                 +               ++   +",
"+  +++++++  +++++++++++++  +++++++++++++++++++++  +",
"+  +     +  +           +  +               s +++  +",
"+  +  +  +  +  +  ++++  +  +  +++++++++++++  +++  +",
"+  +  +  +  +  +  +        +  +  +        +       +",
"+  +  ++++  +  ++++++++++  +  +  ++++  +  +  ++   +",
"+  +     +  +          +   +           +  +  ++  ++",
"+  ++++  +  +++++++ ++++++++  +++++++++++++  ++  ++",
"+     +  +     +              +              ++   +",
"++++  +  ++++++++++ +++++++++++  ++++++++++  +++  +",
"+  +  +                    +     +     +  +  +++  +",
"+  +  ++++  +++++++++++++  +  ++++  +  +  +  ++   +",
"+  +  +     +     +     +  +  +     +     +  ++  ++",
"+  +  +  +++++++  ++++  +  +  +  ++++++++++  ++  ++",
"+                       +  +  +              ++  ++",
"+ ++++++             +  +  +  +  +++        +++  ++",
"+ ++++++ ++++++ +++++++++    ++ ++   ++++++++++  ++",
"+ +    +    +++ +     +++++++++ ++  +++++++    + ++",
"+ ++++ ++++ +++ + +++ +++    ++    ++  e ++ ++ + ++",
"+ ++++    +     + +++ +++ ++ ++++++++ ++ ++ ++   ++",
"+      ++ +++++++++++     ++          ++    +++++++",
"+++++++++++++++++++++++++++++++++++++++++++++++++++",
 ]

grid5= [
"+++++++++++++++++++++++++++++++++++++++++++++++++++",
"+             e+                                  +",
"+++++++++++++++++++++++++++++++++++++++++++++++++++",
"+          +                 +               ++   +",
"+  +++++++  +++++++++++++  ++++++++++++++++++++++++++",
"+  +     +  +           +  +                 +++  +",
"+  +  +  +  +  +  ++++  +  +  +++++++++++++  +++  +",
"+  +  +  +  +  +  +        +  +  +        +       +",
"+  +  ++++  +  ++++++++++  +  +  ++++  +  +  ++   +",
"+  +     +  +          +   +           +  +  ++  ++",
"+  ++++  +  +++++++ ++++++++  +++++++++++++  ++  ++",
"+     +  +     +              +              ++   +",
"++++  +  ++++++++++ +++++++++++  ++++++++++  +++  +",
"+  +  +                    +     +     +  +  +++  +",
"+  +  ++++  +++++++++++++  +  ++++  +  +  +  ++   +",
"+  +  +     +     +     +  +  +     +     +  ++  ++",
"+  +  +  +++++++  ++++  +  +  +  ++++++++++  ++  ++",
"+                       +  +  +              ++  ++",
"+ ++++++             +  +  +  +  +++        +++  ++",
"+ ++++++ ++++++ +++++++++    ++ ++   ++++++++++  ++",
"+ +    +    +++ +     +++++++++ ++  +++++++    + ++",
"+ ++++ ++++ +++ + +++ +++    ++    ++    ++ ++ + ++",
"+ ++++    +     + +++ +++ ++ ++++++++ ++ ++ ++   ++",
"+      ++ +++++++++++     ++          ++   s+++++++",
"+++++++++++++++++++++++++++++++++++++++++++++++++++",
 ]

#grid6= [
#"+++++++++++++++++++++++++++++++++++++++++++++++++++",
#"+             +                                  +",
#"+++++++++++++++++++++++++++++++++++++++++++++++++++",
#"+          +                 +               ++   +",
#"+  +++++++  +++++++++++++  ++++++++++++++++++++++++++",
#"+  +     +  +           +  +                 +++  +",
#"+  +  +  +  +  +  ++++  +  +  +++++++++++++  +++  +",
#"+  +  +  +  +  +  +        +  +  +        +       +",
#"+  +  ++++  +  ++++++++++  +  +  ++++  +  +  ++   +",
#"+  +     +  +          +   +           +  +  ++  ++",
#"+  ++++  +  +++++++ ++++++++  +++++++++++++  ++  ++",
#"+     +  +     +              +              ++   +",
#"++++  +  ++++++++++ +++++++++++  ++++++++++  +++  +",
#"+  +  +                    +     +     +  +  +++  +",
#"+  +  ++++  +++++++++++++  +  ++++  +  +  +  ++   +",
#"+  +  +     +     +     +  +  +     +     +  ++  ++",
#"+  +  +  +++++++  ++++  +  +  +  ++++++++++  ++  ++",
#"+                       +  +  +         es  ++  ++",
#"+ ++++++             +  +  +  +  +++        +++  ++",
#"+ ++++++ ++++++ +++++++++    ++ ++   ++++++++++  ++",
#"+ +    +    +++ +     +++++++++ ++  +++++++    + ++",
#"+ ++++ ++++ +++ + +++ +++    ++    ++    ++ ++ + ++",
#"+ ++++    +     + +++ +++ ++ ++++++++ ++ ++ ++   ++",
#"+      ++ +++++++++++     ++          ++    +++++++",
#"+++++++++++++++++++++++++++++++++++++++++++++++++++",
# ]

#grid7= [
#"+++++++++++++++",
#"+ ++++ +e+",
#"+ +++++ +++ + +",
#"+ + +       + +",
#"+ +   +++ + + +",
#"+ + + +   + + +",
#"+   + +   + + +",
#"+++++ +   + + +",
#"+     +   +   +",
#"+++++++++++++++",
#]

#grid7= [
#"+++++++++++++++",
#"+ ++++ +s+",
#"+ +++++ +++ + +",
#"+ + +       + +",
#"+ +++++ + + +",
#"+ + + +   + + +",
#"+   + +   + + +",
#"+++++ +   + + +",
#"+     +   +   +",
#"+++++++++++++++",
#]

grid= [
"+++++++++++++++++++++++++++++++++++++++++++++++++++",
"+             s+                                  +",
"+  ++++++++++  +++++++++++++  +++++++  ++++++++++++",
"+          +                 +               ++   +",
"+  +++++++  +++++++++++++  +++++++++++++++++++++  +",
"+  +     +  +           +  +                 +++  +",
"+  +  +  +  +  +  ++++  +  +  +++++++++++++  +++  +",
"+  +  +  +  +  +  +        +  +  +        +       +",
"+  +  ++++  +  ++++++++++  +  +  ++++  +  +  ++   +",
"+  +     +  +          +   +           +  +  ++  ++",
"+  ++++  +  +++++++ ++++++++  +++++++++++++  ++  ++",
"+     +  +     +              +              ++   +",
"++++  +  ++++++++++ +++++++++++  ++++++++++  +++  +",
"+  +  +                    +     +     +  +  +++  +",
"+  +  ++++  +++++++++++++  +  ++++  +  +  +  ++   +",
"+  +  +     +     +     +  +  +     +     +  ++  ++",
"+  +  +  +++++++  ++++  +  +  +  ++++++++++  ++  ++",
"+                       +  +  +              ++  ++",
"+ ++++++             +  +  +  +  +++        +++  ++",
"+ ++++++ ++++++ +++++++++    ++ ++   ++++++++++  ++",
"+ +    +    +++ +     +++++++++ ++  +++++++    + ++",
"+ ++++ ++++ +++ + +++ +++    ++    ++    ++ ++ + ++",
"+ ++++    +     + +++ +++ ++ ++++++++ ++ ++ ++   ++",
"+      ++ +++++++e+++     ++          ++    +++++++",
"+++++++++++++++++++++++++++++++++++++++++++++++++++",
 ]


def setup_maze(grid):                          # define a function called setup_maze
    global start_x, start_y, end_x, end_y      # set up global variables for start and end locations
    for y in range(len(grid)):                 # read in the grid line by line
        for x in range(len(grid[y])):          # read each cell in the line
            character = grid[y][x]             # assign the varaible "character" the the x and y location od the grid
            screen_x = -588 + (x * 24)         # move to the x location on the screen staring at -588
            screen_y = 288 - (y * 24)          # move to the y location of the screen starting at 288

            if character == "+":
                maze.goto(screen_x, screen_y)         # move pen to the x and y locaion and
                maze.stamp()                          # stamp a copy of the turtle on the screen
                walls.append((screen_x, screen_y))    # add coordinate to walls list

            if character == " " or character == "e":
                path.append((screen_x, screen_y))     # add " " and e to path list

            if character == "e":
                green.color("cyan")
                green.goto(screen_x, screen_y)       # send green sprite to screen location
                end_x, end_y = screen_x,screen_y     # assign end locations variables to end_x and end_y
                green.stamp()
                green.color("green")

            if character == "s":
                start_x, start_y = screen_x, screen_y  # assign start locations variables to start_x and start_y
                red.goto(screen_x, screen_y)


def endProgram():
    wn.exitonclick()
    sys.exit()

def search(x,y):                    #bfs code starts here
    frontier.append((x, y))
    solution[x,y] = x,y

    while len(frontier) > 0:          # exit while loop when frontier queue equals zero
        time.sleep(0)
        x, y = frontier.popleft()     # pop next entry in the frontier queue an assign to x and y location

        if(x - 24, y) in path and (x - 24, y) not in visited:  # check the cell on the left
            cell = (x - 24, y)
            solution[cell] = x, y    # backtracking routine [cell] is the previous cell. x, y is the current cell
            #blue.goto(cell)        # identify frontier cells
            #blue.stamp()
            frontier.append(cell)   # add cell to frontier list
            visited.add((x-24, y))  # add cell to visited list

        if (x, y - 24) in path and (x, y - 24) not in visited:  # check the cell down
            cell = (x, y - 24)
            solution[cell] = x, y
            #blue.goto(cell)
            #blue.stamp()
            frontier.append(cell)
            visited.add((x, y - 24))
            print(solution)

        if(x + 24, y) in path and (x + 24, y) not in visited:   # check the cell on the  right
            cell = (x + 24, y)
            solution[cell] = x, y
            #blue.goto(cell)
            #blue.stamp()
            frontier.append(cell)
            visited.add((x +24, y))

        if(x, y + 24) in path and (x, y + 24) not in visited:  # check the cell up
            cell = (x, y + 24)
            solution[cell] = x, y
            #blue.goto(cell)
            #blue.stamp()
            frontier.append(cell)
            visited.add((x, y + 24))
        green.goto(x,y)
        green.stamp()


def backRoute(x, y):               #Backtracking starts here 
    yellow.goto(x, y)
    yellow.stamp()
    while (x, y) != (start_x, start_y):    # stop loop when current cells == start cell
        yellow.goto(solution[x, y])        # move the yellow sprite to the key value of solution ()
        yellow.stamp()
        x, y = solution[x, y]               # "key value" now becomes the new key

# set up classes
maze = Maze()
red = Red()
blue = Cyan()
green = Green()
yellow = Crimson()

# setup lists
walls = []
path = []
visited = set()
frontier = deque()
solution = {}                           # solution dictionary


# main program starts here ####
setup_maze(grid)
search(start_x,start_y)
backRoute(end_x, end_y)
wn.exitonclick()

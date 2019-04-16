#Tri (Will) Luong
#Professor Gupta
#COSC - 2316
#Assignment 10: Create a path for a kangaroo to jump throughout an 5x5 table.
#In addition, the kangaroo must be able to hop 3 times and get a flower. Then turn right, hop 2 times, and plant the flower at a newer position
#Afterward, turn left and hop once

#Executtion
# GLOBAL VARIABLES
FLOWER_SPOT = 'F'
INITIAL_SPOT = '#'
KANGAROO_SPOT = 'K'

# board size
row_size = 5
col_size = 5

# initialize boardMatrix
board = [INITIAL_SPOT] * row_size
for i in range(row_size):
    board[i] = [INITIAL_SPOT] * col_size

# initialize kangaroo
kangaroo_position = [0,0]
kangaroo_direction = 0
board[kangaroo_position[0]][kangaroo_position[1]] = KANGAROO_SPOT;

# initialize game state booleans
flowerPickedOrNot = False
flowerPlantedOrNot = False

# initalize flower
flowerRow = 0
flowerColumn = 3
board[flowerRow][flowerColumn] = FLOWER_SPOT

#display output in a nicely formated string output
def toString():
    global flowerPickedOrNot
    if(kangaroo_position != [flowerRow, flowerColumn] and not flowerPickedOrNot):
        board[flowerRow][flowerColumn] = FLOWER_SPOT
    for i in range(row_size):           #FOR LOOP USING THE BOARD AS ITS RANGE
        retStr= ""
        for j in range(col_size):
            retStr += board[i][j] + " "
        print(retStr)
    print()

def movement(hopNum):
    #imported variables to control the function
    global kangaroo_position
    global kangaroo_direction

    for i in range(hopNum):
        board[kangaroo_position[0]][kangaroo_position[1]] = INITIAL_SPOT
        if(kangaroo_direction == 0):
            if(kangaroo_position[0] - 1 >= 0):
                kangaroo_position[0] -= 1
            else:
                print ("Kangaroo cannot move to the north!")
        elif(kangaroo_direction == 1):
            if(kangaroo_position[1] + 1 < col_size):
                kangaroo_position[1] += 1
            else:
                print ("Kangaroo cannot move to the east!")
        elif (kangaroo_direction == 2):
            if(kangaroo_position[0] + 1 < row_size):
                kangaroo_position[0] += 1
            else:
                print ("Kangaroo cannot move to the south!")
        elif(kangaroo_direction == 3):
            if(kangaroo_position[1] - 1 >= 0):
                kangaroo_position[1] -= 1
            else:
                print ("Kangaroo cannot move to the west!")
        board[kangaroo_position[0]][kangaroo_position[1]] = KANGAROO_SPOT
        toString()



def pick():
    #imported global boolean variables to create a game
    global flowerPickedOrNot
    global flowerPlantedOrNot

    if(not flowerPickedOrNot and kangaroo_position == [flowerRow, flowerColumn]):
        flowerPickedOrNot = True
        print("Flower is picked!")

def plant():
    #global variables to assist with the function
    global flowerPickedOrNot
    global flowerPlantedOrNot
    global flowerRow
    global flowerCol
    
    #if the flower is not picked then it is planted
    if(flowerPickedOrNot):
        flowerPlantedOrNot = True
        flowerPickedOrNot = False

        print("The Flower is planted")
        #planting the flower
        flowerRow = kangaroo_position[0]
        flowerCol = kangaroo_position[1]
        board[flowerRow][flowerCol] = FLOWER_SPOT

#kangaroo movment in the entire board
def rightPos():
    #imported variables to assist the function.
    global kangaroo_direction
    #condition of moving right
    kangaroo_direction = kangaroo_direction+1 % 4

def leftPos():
    #imported variables to assist the function.
    global kangaroo_direction
    #condition of moving left
    kangaroo_direction = kangaroo_direction-1 % 4

def main():
    rightPos()
    movement(3)
    pick()
    rightPos()
    movement(2)
    plant()
    leftPos()
    movement(1)

#begin the game
toString()
main()








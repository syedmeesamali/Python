import numpy as np

# create a 3 x 3 board with all zeros in the start
def create_board():
    return np.zeros((3,3))

#Below function will help to place player 1 or 2 in some position
#defined by tuple of length 2 (x and y position)

def place(board, player, position):
    board = create_board()
    if player == 1 or player == 2:
        for i in range(3):
            for j in range(3):
                pos = (i,j)
    else:
        return 0
    

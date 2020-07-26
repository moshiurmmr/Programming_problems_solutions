from random import randint


def knightMovesForNTimes(n, x0, y0):
    """
    #This function makes knight move n number of times and updates the position of the knight
   # x0, y0 is the initial position of the knight
    """
    x_init = x0
    y_init = y0
    for i in range(n):
        # randomly select any of the possible 8 moves of the knight
        move_dir = randint(1, 8)
        x, y = getMovePosition(move_dir, x_init, y_init)

    return x, y


def getMovePosition(move_dir, x_prev, y_prev):
    """
    #This function calculates the new position of the knight after it moves to any of the possible 8 directions
    #assign x_new and y_new to -100 if the knight moves out of the chess board.
    #(-100, -100) is just a signal to the knightMovesForNTimes() function, so that,
    #it does not increment the count of n (number of times the knight should move)
    """
    if move_dir == 1:
        x_new = x_prev + 1
        y_new = y_prev + 2
        # if knight moves outside of the chessboard
        if x_new < 0 or y_new < 0 or x_new > 8 or y_new > 8:
            x_new, y_new = knightJumpsOut()
    elif move_dir == 2:
        x_new = x_prev - 1
        y_new = y_prev + 2
        # if knight moves outside of the chessboard
        if x_new < 0 or y_new < 0 or x_new > 8 or y_new > 8:
            x_new, y_new = knightJumpsOut()
    elif move_dir == 3:
        x_new = x_prev + 1
        y_new = y_prev - 2
        # if knight moves outside of the chessboard
        if x_new < 0 or y_new < 0 or x_new > 8 or y_new > 8:
            x_new, y_new = knightJumpsOut()
    elif move_dir == 4:
        x_new = x_prev - 1
        y_new = y_prev - 2
        # if knight moves outside of the chessboard
        if x_new < 0 or y_new < 0 or x_new > 8 or y_new > 8:
            x_new, y_new = knightJumpsOut()
    elif move_dir == 5:
        x_new = x_prev + 2
        y_new = y_prev + 1
        # if knight moves outside of the chessboard
        if x_new < 0 or y_new < 0 or x_new > 8 or y_new > 8:
            x_new, y_new = knightJumpsOut()
    elif move_dir == 6:
        x_new = x_prev + 2
        y_new = y_prev - 1
        # if knight moves outside of the chessboard
        if x_new < 0 or y_new < 0 or x_new > 8 or y_new > 8:
            x_new, y_new = knightJumpsOut()
    elif move_dir == 7:
        x_new = x_prev - 2
        y_new = y_prev + 1
        # if knight moves outside of the chessboard
        if x_new < 0 or y_new < 0 or x_new > 8 or y_new > 8:
            x_new, y_new = knightJumpsOut()
    else:
        x_new = x_prev - 2
        y_new = y_prev - 1
        # if knight moves outside of the chessboard
        if x_new < 0 or y_new < 0 or x_new > 8 or y_new > 8:
            x_new, y_new = knightJumpsOut()

    return x_new, y_new

def knightJumpsOut():
    """
    #This function is to capture the error condition when the knight moves outside of the chessboard.
    #It's a very rough technique, need to be updated with and elegant (!) solution
    """
    x_new = -100
    y_new = -100
    return x_new, y_new


x0 = 4
y0 = 4

(x, y) = knightMovesForNTimes(1, x0, y0)

print("New knight position is {}".format((x, y)))
from random import randint
from getMovePosition import getMovePosition

def knightMovesForNTimes(n, x0, y0):
    """
    This function makes knight move n number of times and updates the position of the knight
    x0, y0 is the initial position of the knight
    """
    x_init = x0
    y_init = y0
    # last position of the knight.
    # This is needed to tackle situations when the knight moves out of the chessboard.
    x_last = x0
    y_last = y0
    for i in range(n):
        # last position of the knight.
        # This is needed to tackle situations when the knight moves out of the chessboard.
        #x_last = x0
        #y_last = y0
        # randomly select any of the possible 8 moves of the knight
        move_dir = randint(1, 8)
        x, y = getMovePosition(move_dir, x_init, y_init)
        if x != -100 or y != -100:
            # when the knight is inside the chessboard
            x_last = x
            y_last = y
        # if the knight moves out of the chessboard, then the move is invalid
        # make a new move valid move
        #if x == -100 and y == -100:
        else:
            print("The knight moves out of the chessboard.")
            x, y = getMovePosition(move_dir, x_last, y_last)
            #break
            #i = i -1
        print("The knight moves to position ({} {}) for move# {}\n".format(x, y, i+1))

    return x, y
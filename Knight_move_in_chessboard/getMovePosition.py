from knightJumpsOut import knightJumpsOut


def getMovePosition(move_dir, x_prev, y_prev):
    """
    This function calculates the new position of the knight after it moves to any of the possible 8 directions
    assign x_new and y_new to -100 if the knight moves out of the chess board.
    (-100, -100) is just a signal to the knightMovesForNTimes() function, so that,
    it does not increment the count of n (number of times the knight should move)
    """
    if move_dir == 1:
        x_new = x_prev + 1
        y_new = y_prev + 2
        if x_new > 8:
            x_new = x_prev
            y_new = y_prev
            # print a message that the knight moves out of the board, so reverting to previous position
            knightJumpsOut()
        elif y_new > 8:
            x_new = x_prev
            y_new = y_prev
            # print a message that the knight moves out of the board, so reverting to previous position
            knightJumpsOut()

        #print("New position of the knight is ({}, {})\n".format(x_new, y_new))
        # if knight moves outside of the chessboard
        #if x_new < 0 or y_new < 0 or x_new > 8 or y_new > 8:
            #x_new, y_new = knightJumpsOut()
    elif move_dir == 2:
        x_new = x_prev - 1
        y_new = y_prev + 2
        if x_new < 0:
            x_new = x_prev
            y_new = y_prev
            # print a message that the knight moves out of the board, so reverting to previous position
            knightJumpsOut()
        elif y_new > 8:
            x_new = x_prev
            y_new = y_prev
            # print a message that the knight moves out of the board, so reverting to previous position
            knightJumpsOut()
        #print("New position of the knight is ({}, {})\n".format(x_new, y_new))
        # if knight moves outside of the chessboard
        #if x_new < 0 or y_new < 0 or x_new > 8 or y_new > 8:
            #x_new, y_new = knightJumpsOut()
    elif move_dir == 3:
        x_new = x_prev + 1
        y_new = y_prev - 2
        if x_new > 8:
            x_new = x_prev
            y_new = y_prev
            # print a message that the knight moves out of the board, so reverting to previous position
            knightJumpsOut()
        elif y_new < 0:
            x_new = x_prev
            y_new = y_prev
            # print a message that the knight moves out of the board, so reverting to previous position
            knightJumpsOut()
        #print("New position of the knight is ({}, {})\n".format(x_new, y_new))
        # if knight moves outside of the chessboard
        #if x_new < 0 or y_new < 0 or x_new > 8 or y_new > 8:
            #x_new, y_new = knightJumpsOut()
    elif move_dir == 4:
        x_new = x_prev - 1
        y_new = y_prev - 2
        if x_new < 0:
            x_new = x_prev
            y_new = y_prev
            # print a message that the knight moves out of the board, so reverting to previous position
            knightJumpsOut()
        elif y_new < 0:
            x_new = x_prev
            y_new = y_prev
            # print a message that the knight moves out of the board, so reverting to previous position
            knightJumpsOut()
        #print("New position of the knight is ({}, {})\n".format(x_new, y_new))
        # if knight moves outside of the chessboard
        #if x_new < 0 or y_new < 0 or x_new > 8 or y_new > 8:
            #x_new, y_new = knightJumpsOut()
    elif move_dir == 5:
        x_new = x_prev + 2
        y_new = y_prev + 1
        #print("New position of the knight is ({}, {})\n".format(x_new, y_new))
        # if knight moves outside of the chessboard
        #if x_new < 0 or y_new < 0 or x_new > 8 or y_new > 8:
            #x_new, y_new = knightJumpsOut()
        if x_new > 8:
            x_new = x_prev
            y_new = y_prev
            # print a message that the knight moves out of the board, so reverting to previous position
            knightJumpsOut()
        elif y_new > 8:
            x_new = x_prev
            y_new = y_prev
            # print a message that the knight moves out of the board, so reverting to previous position
            knightJumpsOut()
    elif move_dir == 6:
        x_new = x_prev + 2
        y_new = y_prev - 1
        if x_new > 8:
            x_new = x_prev
            y_new = y_prev
            # print a message that the knight moves out of the board, so reverting to previous position
            knightJumpsOut()
        elif y_new < 0:
            x_new = x_prev
            y_new = y_prev
            # print a message that the knight moves out of the board, so reverting to previous position
            knightJumpsOut()
        #print("New position of the knight is ({}, {})\n".format(x_new, y_new))
        # if knight moves outside of the chessboard
        #if x_new < 0 or y_new < 0 or x_new > 8 or y_new > 8:
            #x_new, y_new = knightJumpsOut()
    elif move_dir == 7:
        x_new = x_prev - 2
        y_new = y_prev + 1
        if x_new < 0:
            x_new = x_prev
            y_new = y_prev
            # print a message that the knight moves out of the board, so reverting to previous position
            knightJumpsOut()
        elif y_new > 8:
            x_new = x_prev
            y_new = y_prev
            # print a message that the knight moves out of the board, so reverting to previous position
            knightJumpsOut()
        #print("New position of the knight is ({}, {})\n".format(x_new, y_new))
        # if knight moves outside of the chessboard
        #if x_new < 0 or y_new < 0 or x_new > 8 or y_new > 8:
            #x_new, y_new = knightJumpsOut()
    else:
        x_new = x_prev - 2
        y_new = y_prev - 1
        if x_new < 0:
            x_new = x_prev
            y_new = y_prev
            # print a message that the knight moves out of the board, so reverting to previous position
            knightJumpsOut()
        elif y_new < 0:
            x_new = x_prev
            y_new = y_prev
            # print a message that the knight moves out of the board, so reverting to previous position
            knightJumpsOut()
        #print("New position of the knight is ({}, {})\n".format(x_new, y_new))
        # if knight moves outside of the chessboard
        #if x_new < 0 or y_new < 0 or x_new > 8 or y_new > 8:
            #x_new, y_new = knightJumpsOut()

    return x_new, y_new

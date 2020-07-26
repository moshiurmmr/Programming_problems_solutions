## Problem
This program solves the following problem:

"Consider a chess knight moving on the first quardrant of the plane. It starts at (0,0) and at each step will move two
units in one direction and one unit in the other, such that x >= 0 and y > = 0. At each step the knight randomly
selects a valid move, with uniform probability. For example, from (0, 1), the knight will move to (1, 3), (2, 2), or
(2, 0), each with probability one-third.

After 10 moves, what is the expected Euclidean distance of the knight from the origin? (if the knight is at (2, 1),
its distance is sqrt(2^2 + 1^2) ~ 2.24.)

- If the knight made it a distance of at least 10 from the origin some time during those 10 moves, what is its expected
Euclidean distance at the end of the 10 moves?

- After 100 moves, what is the expected Euclidean distance of the knight from the origin?"

## Solution
There are four parts of this program:
### Knight_move_in_chessboard.py
* initializes the starting positon of the knight in the chessboard
* initializes the number of moves that the knight makes
* calls *knightMovesForNTimes* function to calculate the position of the knight after a single move
* calculates the Euclidean distance between the knight's initial and final posiitons

### knightMovesForNTimes.py
- moves the knight in a random direction with equal probabilities
- calls *getMovePosition* funciton to calculate the knight's position for a single move
- calculates the knight's final position after *n* moves

### getMovePosition.py
- calculates the position of the knight for a single move
- there are 8 possible moves that a knight can make
- takes care of situations when the knight has the possiblility of moving out of the chessboard
- calls *knightJumpsOut* function to display a message when the knight moves out of the chessboard 

### knightJumpsOut.py
- displays a message when the knight moves out of the chessboard 

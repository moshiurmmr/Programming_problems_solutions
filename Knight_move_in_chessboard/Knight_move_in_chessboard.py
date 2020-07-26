"""
This program solves the following problem:
Consider a chess knight moving on the first quardrant of the plane. It starts at (0,0) and at each step will move two
units in one direction and one unit in the other, such that x >= 0 and y > = 0. At each step the knight randomly
selects a valid move, with uniform probability. For example, from (0, 1), the knight will move to (1, 3), (2, 2), or
(2, 0), each with probability one-third.

After 10 moves, what is teh expected Euclidean distance of the knight from the origin? (if the knight is at (2, 1),
its distance is sqrt(2^2 + 1^2) ~ 2.24.)

- If the knight made it a distance of at least 10 from the origin some time during those 10 moves, what is its expected
Euclidean distance at the end of the 10 moves?

- After 100 moves, what is the expected Euclidean distance of the knight from the origin?
"""

from math import  sqrt
from knightMovesForNTimes import knightMovesForNTimes

# starting position (origin) of the knight, it can be changed to any position e.g., (0, 0)
x0 = 4
y0 = 5

# number of moves
n = 10

# print the initial message
print("The knight starts at positon ({}, {}) and it will move for {} times \n".format(x0, y0, n))

# final position of the knight after n number of moves
(x_final, y_final) = knightMovesForNTimes(n, x0, y0)

print("After {} moves, new knight position is {}\n".format(n, (x_final, y_final)))


# calculate the expected Euclidean distance from origin (x0, y0) after n moves
x_distance = x_final - x0
y_distance = y_final - y0
distance = sqrt(x_distance**2 + y_distance**2)

print("The Ecuclidean distance after {} moves is: {}".format(n, distance))
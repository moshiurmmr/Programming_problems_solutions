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


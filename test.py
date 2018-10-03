import numpy as np

x = np.zeros([3, 3], int)

# makes a 2d array which has ones going from the top left
# and runs diagonally to the bottom right
y = np.eye(3, dtype=int)

# fliplr flips our "Eye" matrix
np.fliplr(y)

print(y)
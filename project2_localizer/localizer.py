import pdb
from helpers import normalize, blur

def initialize_beliefs(grid):
    height = len(grid)
    width = len(grid[0])
    area = height * width
    belief_per_cell = 1.0 / area
    beliefs = []
    for i in range(height):
        row = []
        for j in range(width):
            row.append(belief_per_cell)
        beliefs.append(row)
    return beliefs

def sense(color, grid, beliefs, p_hit, p_miss):
    import numpy as np
    new_beliefs = []
    num_row, num_col = np.shape(grid)
    new_beliefs = [ [ _ for _ in range(num_col) ] for _ in range(num_row) ]
    
    for i in range(num_row):
        for j in range(num_col): 
            if grid[i][j] == color:
                new_beliefs[i][j] = beliefs[i][j] * p_hit
            else:
                new_beliefs[i][j] = beliefs[i][j] * p_miss
    

    new_beliefs = np.array(new_beliefs)
    normalizer = np.sum(new_beliefs)
    new_beliefs /= normalizer
    new_beliefs = new_beliefs.tolist()

    return new_beliefs

def move(dy, dx, beliefs, blurring):
    height = len(beliefs)
    width = len(beliefs[0])
    new_G = [[0.0 for i in range(width)] for j in range(height)]
    for i, row in enumerate(beliefs):
        for j, cell in enumerate(row):
            new_i = (i + dy ) % height
            new_j = (j + dx ) % width
            #pdb.set_trace()

            new_G[int(new_i)][int(new_j)] = cell
    return blur(new_G, blurring)
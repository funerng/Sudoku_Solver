import numpy as np
from random import randint

test = [[0, 0, 6, 3, 9, 7, 8, 0, 0],
        [3, 9, 0, 6, 2, 0, 1, 7, 5],
        [0, 0, 0, 1, 0, 0, 9, 3, 0],
        [7, 0, 0, 8, 1, 0, 4, 0, 3],
        [0, 2, 3, 9, 0, 5, 0, 8, 1],
        [0, 0, 1, 2, 4, 0, 5, 9, 0],
        [0, 3, 0, 4, 0, 1, 0, 5, 0],
        [0, 4, 5, 7, 6, 0, 3, 1, 8],
        [1, 8, 7, 5, 0, 9, 0, 6, 4],]

testa = np.matrix(test)

# N is the size of the grid
def placement(x,y ,n):
    global test
    # for a given x and y value, check if it clashes with columns
    for i in range(0,9):
        if test[x][i] == n:
            return False

    # for a given x and y value, check if it clashes with rows
    for i in range(0,9):   
        if test[i][y] == n:
            return False

    # with given x or y, check its square of it clashes with rows
    # hypothetically a 9x9 matrix, has 9 3x3 squares. first row [y0=0, y1 = 2][x0 = 0, x1 = 2] and next cube [y0 = 3, y1=5][x0=0, x1=2]
    # for example if X = 2, Y = 3, the it will be the second square whose region is [x: 0 - 2, y:3-5]
    # so at x = 2, we need it to start at 0, since x !> 3, and y to start at 3 since y>3
    # a factor of 3


    y0 = (y//3)*3 # For example if y = 5, y//3 would be 1, and 1*3 = 3. at y =5, the square is at y=3
    x0 = (x//3)*3 

    for i in range(0,3):
        for j in range(0,3):
            if test[x0+i][y0+j] == n:
                return False 

    return True

def solve():
    global test
    for x in range(0,9):
        for y in range (0,9):
            if test[x][y] is 0:
                for n in range(1,10):
                    if placement(x,y,n) is True:
                        test[x][y] = n # places the value n in the box
                        solve() # runs the script again
                        test[x][y] = 0
                return 
    print(np.matrix(test))


if __name__ == "__main__":
    print("~~~~~~~~~~~~~~~~~Unsolved~~~~~~~~~~~")
    print(np.matrix(test))
    print("~~~~~~~~~~~~~~~~~Solved~~~~~~~~~~~~~~")
    solve()

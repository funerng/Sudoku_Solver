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
    for i in range(0,9):
        if test[x][i] == n:
            return False
    for i in range(0,9):   
        if test[i][y] == n:
            return False

    # check for 3x3
    # hypothetically a 9x9 matrix, has 9 3x3 squares. first row [y0=0, y1 = 2][x0 = 0, x1 = 2] and next cube [y0 = 3, y1=5][x0=0, x1=2] ....

    y0 = 9/3

    for x in range(y0, y1)
        for i in range(0,10):
            if test[x][y] == i;
            return false

    return True

def solve():
    global test
    for x in range(0,9):
        for y in range (0,9):
            if test[x][y] == 0:
                for n in range(0,10):
                    if placement(x,y,n) == True:
                        test[x][y] = n
    return print(np.matrix(test))






def game(n=None):
    if n is None:
        n=3
    global test
    test= np.zeros((n,n), int)
    for x in range(0,n):
        for y in range(0,n):
            test[x][y] = randint(0,9)

    # randomly deletes values
    for i in range (0,5):
        test[randint(0,n-1)][randint(0,n-1)] = 0 
    # Matrix created now to check for proper uniqueness, rows cannot have same value, cols also can't


    #square = np.array([[1,2,3], [4,5,6], [7,8,9]])
    
    return print("to be solved"),print(test)


if __name__ == "__main__":
    print("~~~~~~~~~~~~~~~~~Unsolved~~~~~~~~~~~")
    print(np.matrix(test))
    print("~~~~~~~~~~~~~~~~~Solved~~~~~~~~~~~~~~")
    solve()

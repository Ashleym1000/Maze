# 10/17/20
# maze program, make it through a maze
# maze size
N = 4

# fn PRINTS solution matrix sol
def printSolution(sol):

    for i in sol:
        for j in i:
            print(str(j) + " ", end="")
        print("")

# fn CHECKS if x, y is valid for matrix N*N
def isSafe( maze, x, y):

    if (x>=0 and x<N and y>=0 and y<N and maze[x][y] ==1):
        return True
    else:
        return False

# fn SOLVES the maze problem
# if no path, returns False
# if path, returns path and True
def solveMaze( maze):

    # create matrix
    sol = [ [0 for j in range (4)] for i in range(4)]

    if solveMazeUtil(maze, 0, 0, sol) == False:
        print("Solution doesn't exist");
        return False
    else:
        printSolution(sol)
        return True

# RECURSION UTILITY fn t solve maze problem
def solveMazeUtil(maze,x,y,sol):

    # if (x,y is goal) return true
    if x==N-1 and y==N-1 and maze[x][y]==1:
        sol[x][y] =1
        return True

    # Check if maze [x][y] is valid
    if isSafe(maze,x,y) ==True:
        # mark x,y as part of the path
        sol[x][y] =1

        # move forward in x direction
        if solveMazeUtil(maze,x+1,y,sol) == True:
            return True

        # move down in y direction
        if solveMazeUtil(maze,x,y+1,sol) == True:
            return True

        # if neither above movements work, then BACKTRACK and unmark x,y
        sol[x][y] = 0
        return False

#test
if __name__ == "__main__":
    # initializing maze
    maze = [[1, 1, 1, 1],
            [1, 1, 0, 1],
            [1, 0, 0, 1],
            [1, 1, 1, 1]]
    solveMaze(maze)

import copy

def createColumns(grid):
    columns = []
    for column in range(0,9):
        array = []
        for line in range(0,9):
            array.append(grid[line][column])
        columns.append(array)
    return columns

def createSquares(grid):
    squares = []
    indexLine = 0
    indexColumn = 0
    array = []
    while len(squares)!=9:
        if len(array) == 9:
            squares.append(copy.deepcopy(array))
            array = []
        if len(squares)!=0 and len(squares)%3==0:
            indexLine = indexLine+3
            indexColumn = 0
        if len(squares) != 9:
            for lineIndex in range(indexLine,indexLine+3):
                array.extend(grid[lineIndex][indexColumn:indexColumn+3])
        indexColumn = indexColumn + 3
    return squares

def checkRow(line, col, grid):
    if grid[line].count(grid[line][col])>1 and grid[line][col]!=0:
        return False
    return True

def checkCol(line, col, grid):
    columns = createColumns(grid)
    if columns[col].count(grid[line][col])>1 and grid[line][col]!=0:
        print("B")
        return False
    return True

def checkSquare(line, col, grid):
    squares = createSquares(grid)
    if squares[line//3*3+col//3].count(grid[line][col])>1 and grid[line][col]!=0:
        print("C")
        return False
    return True
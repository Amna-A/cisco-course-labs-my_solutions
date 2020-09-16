correct = [[2,9,5,7,4,3,8,6,1],
           [4,3,1,8,6,5,9,2,7],
           [8,7,6,1,9,2,5,4,3],
           [3,8,7,4,5,9,2,1,6],
           [6,1,2,3,8,7,4,9,5],
           [5,4,9,2,1,6,7,3,8],
           [7,6,3,5,2,4,1,8,9],
           [9,2,8,6,7,1,3,5,4],
           [1,5,4,9,3,8,6,7,2]]

incorrect = [[1,9,5,7,4,3,8,6,2],
             [4,3,1,8,6,5,9,2,7],
             [8,7,6,1,9,2,5,4,3],
             [3,8,7,4,5,9,2,1,6],
             [6,1,2,3,8,7,4,9,5],
             [5,4,9,2,1,6,7,3,8],
             [7,6,3,5,2,4,1,8,9],
             [9,2,8,6,7,1,3,5,4],
             [2,5,4,9,3,8,6,7,1]]

xx = [[1,3,2],
    [2,1,3],
    [3,2,1]]

yy = [[1,2,4,3],
    [2,3,1,3],
    [3,1,2,3],
    [4,2,2,4]]

def checkset(board):
    x = len(board)
    rows_list=[]
    
    while x<9:
        for row in board:
            for digits in row:
                if row.count(digits) > 1:
                    return "wrong sudoku"
                else:
                    x+=1
    
    while x>0:
        for row in board:
            rows_list.append(row[x-1])
        for digits in row:
            if rows_list.count(digits) > 1:
                return "wrong sudoku"
            elif not isinstance(digits,float) or digits<1:
                return "wrong sudoku"
            else:
                rows_list=[]
                x-=1
        return "correct sudoku"

print(checkset(incorrect))
print(checkset(correct))
print(checkset(xx))
print(checkset(yy))

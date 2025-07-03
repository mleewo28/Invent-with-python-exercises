def getChessSquareColour(row,column): 
    
    for row in range(0,8):
        for column in range(0,8): 
            if (row % 2 == 0 and column % 2 == 0) or (row % 2 == 1 and column % 2 == 1): 
                return 'white'
            else: 
                return 'black'
            
assert getChessSquareColour(0, 0) == 'white'

assert getChessSquareColour(1, 0) == 'black'

assert getChessSquareColour(0, 1) == 'black'

assert getChessSquareColour(7, 7) == 'white'

assert getChessSquareColour(0, 8) == ''

assert getChessSquareColour(2, 9) == ''
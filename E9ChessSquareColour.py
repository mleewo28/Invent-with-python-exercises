def getChessSquareColour(column,row): 
    
    #Account for arguments outside of the 0 to 7 range for 'row' and 'column'
    if row > 7 or row < 0 or column > 7 or column < 0:
        return ''
    elif (row % 2 == 0 and column % 2 == 0) or (row % 2 == 1 and column % 2 == 1): 
        return 'white'
    else: 
        return 'black'
            
assert getChessSquareColour(0, 0) == 'white'

assert getChessSquareColour(1, 0) == 'black'

assert getChessSquareColour(0, 1) == 'black'

assert getChessSquareColour(7, 7) == 'white'

assert getChessSquareColour(0, 8) == ''

assert getChessSquareColour(2, 9) == ''
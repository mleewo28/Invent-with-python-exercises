def printMultiplicationTable():
    print(' | 1  2  3  4  5  6  7  8  9  10')
    print('--+-----------------------------')
    for row in range(1,11):
        print(f"{row}".rjust(2)+'|', end='')
        for column in range(1,11):
            product = column*row 
            print(f"{product}".rjust(2) +" ",end='')
        print() #print a new line after every row 



printMultiplicationTable()
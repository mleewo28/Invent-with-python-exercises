def drawPyramid(height):
    row = 1 
    while height > 0:

        for i in range(height - row):
            print(' ', end = '')

        for j in range(2*row-1):
            print('#', end = '')
        print() 
        height -= 1 
        row += 1 

drawPyramid(5)
drawPyramid(2)
drawPyramid(10)
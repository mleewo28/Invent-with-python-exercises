# def test():
#     string = '+--------------+'
#     length = len(string)

#     return length 

# print(test())

def drawBorder(width,height):
    if width < 2 or height < 2: 
        print() 

    #print top row 
    print('+', end = '')
    for i in range(width - 2):
        print('-', end='')
    print('+')

    #loop through to complete all rows expect for the top and bottom row 
    for j in range(height - 2):
        print('|', end = '')
        print(' ', end = '')
        print('|')

    #bottom row 
    print('+', end = '')
    for i in range(width - 2):
        print('-', end='')
    print('+')


drawBorder(5,4)



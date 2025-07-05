def printASCIITable(): 

    #loop through integers up to and including 126 
    for i in range(32,127): 
        #store ASCII text character in varialbe char
        char = chr(i)
        print(f'{i} {char}')

printASCIITable() 
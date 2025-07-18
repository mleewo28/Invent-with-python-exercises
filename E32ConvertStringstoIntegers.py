def convertStrToInt(strNum): 
    FROM_str_to_int = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5,'6':6,'7':7,'8':8,'9':9}

    integerNum = 0 
    #check if the number is negative 

    isNegative = strNum[0] == '-'

    if isNegative:
        strNum = strNum[1:]

    length = len(strNum)

    for i in range(length):
        integerNum = (integerNum*10) +FROM_str_to_int[strNum[i]]

    if isNegative:
        return (-1)*(integerNum) 
    
    return integerNum

#assert statements 
for i in range(-10000, 10000):

    assert convertStrToInt(str(i)) == i


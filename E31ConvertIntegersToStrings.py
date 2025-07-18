def convertIntToStr(integerNum):
    if integerNum == 0: 
        return '0'
    
    isNegative = integerNum < 0 
    
    
    FROM_digits_To_Str = {0:'0',1:'1',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9'}
    strNum = ''

    integerNum = abs(integerNum)

    while integerNum > 0:
        ones_digit = integerNum % 10 
        #print(integerNum)
        strNum = FROM_digits_To_Str[ones_digit] + strNum
        integerNum = integerNum//10 
    
    if isNegative:
        return '-' + strNum
    
    print(strNum)

    return strNum 

convertIntToStr(-1000)

for i in range(-10000,10000):

    assert convertIntToStr(i) == str(i)
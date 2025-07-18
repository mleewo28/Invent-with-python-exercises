def convertIntTo(integerNum):
    if integerNum == 0: 
        return '0'
    
    FROM_digits_To_Str = {0:'0',1:'1',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9'}
    strNum = ''

    while integerNum > 0:
        ones_digit = integerNum % 10 
        strNum = FROM_digits_To_Str[ones_digit] + strNum
        integerNum = integerNum//10 
    
    return strNum 
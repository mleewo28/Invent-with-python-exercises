def commaFormat(number):

    str_num = str(number)

    #check if the number has a fractional part and store it in a variable 
    if '.' in str_num: 
        fractional = str_num[str_num.index('.'):]
        str_num = str_num[:str_num.index('.')]
    else: 
        fractional = '' 

    triplet = ''
    comma_num = ''

    for i in range(len(str_num)-1,-1,-1 ):
        triplet = str_num[i] + triplet 
        if len(triplet) == 3: 
            comma_num = triplet + ',' + comma_num
            triplet = ''
    
    if triplet != '':
        comma_num = triplet + ',' + comma_num

    return comma_num[:-1] + fractional 

assert commaFormat(1) == '1'

assert commaFormat(10) == '10'

assert commaFormat(100) == '100'

assert commaFormat(1000) == '1,000'

assert commaFormat(10000) == '10,000'

assert commaFormat(100000) == '100,000'

assert commaFormat(1000000) == '1,000,000'

assert commaFormat(1234567890) == '1,234,567,890'

assert commaFormat(1000.123456) == '1,000.123456'
        

    
#     #check if the number is less than 999

#     if number < 999: 
#         return str(number)
    
#     comma_format = ''
#     str_number = str(number)

#     #check for a decimal place 
#     rev_str_num = str_number[::-1]
#     if '.' in str_number: 
#         start_index = str_number.index('.') + 1 

#         # Begin to loop through the numbers and add commas
#         for i in range(len(rev_str_num[start_index:])):
#             comma_format += rev_str_num[start_index + i]
#             if len(comma_format) % 3 ==0:
#                 comma_format += ','

#         return comma_format[::-1]
    
#     #for integers 
#     for i in range(len(rev_str_num)):
#         comma_format += rev_str_num[i] 
#         if len(comma_format) % 3 == 0: 
#             comma_format += ','

#     return comma_format[::-1]


# assert commaFormat(1) == '1'

# assert commaFormat(10) == '10'

# assert commaFormat(100) == '100'

# assert commaFormat(1000) == '1,000'

# assert commaFormat(10000) == '10,000'

# assert commaFormat(100000) == '100,000'

# assert commaFormat(1000000) == '1,000,000'

# assert commaFormat(1234567890) == '1,234,567,890'

# assert commaFormat(1000.123456) == '1,000.123456'

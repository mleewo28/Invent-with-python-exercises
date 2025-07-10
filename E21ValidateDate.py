import E20LeapYear

def isValidDate(year,month,day):
    if not (1<= month <=12):
        return False
    if not (1<= day <=31):
        return False 
    
    if E20LeapYear.isLeapYear(year):
        if month ==2:
            if not (1<= day <=29):
                return False
    else: 
        if month ==2:
            if not (1<= day <=28):
                return False
            
    if month in (4,6,9,11):
        if not (1<= day <=30):
            return False
        
    return True


assert isValidDate(1999, 12, 31) == True

assert isValidDate(2000, 2, 29) == True

assert isValidDate(2001, 2, 29) == False

assert isValidDate(2029, 13, 1) == False

assert isValidDate(1000000, 1, 1) == True

assert isValidDate(2015, 4, 31) == False

assert isValidDate(1970, 5, 99) == False

assert isValidDate(1981, 0, 3) == False

assert isValidDate(1666, 4, 0) == False

 

import datetime

d = datetime.date(1970, 1, 1)

oneDay = datetime.timedelta(days=1)

for i in range(1000000):

    assert isValidDate(d.year, d.month, d.day) == True

    d += oneDay
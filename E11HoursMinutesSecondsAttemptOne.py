def getHoursMinutesSeconds(totalSeconds): 
    #create variable called remainder that stores the remaining seconds
    remainder = totalSeconds
    hours = 0 
    mins = 0 
    seconds = 0

    if totalSeconds ==0: 
        return '0s'
    
    while remainder > 0: 

        if remainder >= 3600: 
            hours = remainder//3600 
            wholeHrinSec = hours*60*60 
            remainder -= wholeHrinSec
            #print(f"in if {remainder}")

        elif remainder >= 60: 
            mins = remainder//60 
            wholeMinInSec = mins*60 
            remainder -= wholeMinInSec
            #print(f"in elif {remainder}")

        else: 
            seconds = remainder
            remainder = 0 

    conversion = '' 
    if hours != 0: 
        conversion += str(hours) + 'h '
    if mins != 0: 
        conversion += str(mins) + 'm '
    if seconds != 0: 
        conversion += str(seconds) + 's'
    
    return conversion.strip() 
 


assert getHoursMinutesSeconds(3661) == '1h 1m 1s'

assert getHoursMinutesSeconds(30) == '30s'

assert getHoursMinutesSeconds(60) == '1m'

assert getHoursMinutesSeconds(90) == '1m 30s'

assert getHoursMinutesSeconds(3600) == '1h'

assert getHoursMinutesSeconds(3601) == '1h 1s'

assert getHoursMinutesSeconds(3661) == '1h 1m 1s'

assert getHoursMinutesSeconds(90042) == '25h 42s'

assert getHoursMinutesSeconds(0) == '0s'
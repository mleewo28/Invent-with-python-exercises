def getHoursMinutesSeconds(totalSeconds): 
    #create variable called remainder that stores the remaining seconds
    remainder = totalSeconds
    hours = 0 
    mins = 0 
    seconds = 0
    while remainder > 0: 

        if remainder > 3600: 
            hours = remainder//3600 
            wholeHrinSec = hours*60*60 
            remainder -= wholeHrinSec
            #print(f"in if {remainder}")

        elif remainder > 60: 
            mins = remainder//60 
            wholeMinInSec = mins*60 
            remainder -= wholeMinInSec
            #print(f"in elif {remainder}")

        else: 
            seconds = remainder
            remainder = 0 

    return f"{hours}h {mins}m {seconds}s"


assert getHoursMinutesSeconds(3661) == '1h 1m 1s'
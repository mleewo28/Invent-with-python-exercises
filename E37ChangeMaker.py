def makeChange(amount):

    #create empty dictionary to store results 
    change =  {} 
    quarters = 0 
    dimes = 0 
    nickels = 0 
    pennies = 0 

    if amount >= 25: 
        quarters = amount//25
        amount = amount % 25

    if amount >= 10: 
        dimes = amount//10 
        amount = amount%10 

    if amount >= 5: 
        nickels = amount//5 
        amount = amount % 5 

    if amount > 0: 
        pennies = amount 

    if quarters >0:
        change['quarters'] = quarters

    if dimes > 0: 
        change['dimes'] = dimes 
    
    if nickels > 0: 
        change['nickels'] = nickels

    if pennies > 0: 
        change['pennies'] = pennies

    return change 

# print(makeChange(30))


assert makeChange(30) == {'quarters': 1, 'nickels': 1}

assert makeChange(10) == {'dimes': 1}

assert makeChange(57) == {'quarters': 2, 'nickels': 1, 'pennies': 2}

assert makeChange(100) == {'quarters': 4}

assert makeChange(125) == {'quarters': 5}

def getCostOfCoffee(numOfCoff,pricePerCoff):

    if numOfCoff < 8:
        price = pricePerCoff*numOfCoff

    else: 
        #calculate the number of tickets to know how many groups of 
        #8 were paid for 
        num_ticket = numOfCoff//9
        paid_coffees = num_ticket*8
        # [56 + (67-63)] x price 
        price = (paid_coffees + (numOfCoff - 9*num_ticket))*pricePerCoff

    return price 


assert getCostOfCoffee(7, 2.50) == 17.50

assert getCostOfCoffee(8, 2.50) == 20

assert getCostOfCoffee(9, 2.50) == 20

assert getCostOfCoffee(10, 2.50) == 22.50

 

for i in range(1, 4):

    assert getCostOfCoffee(0, i) == 0

    assert getCostOfCoffee(8, i) == 8 * i

    assert getCostOfCoffee(9, i) == 8 * i

    assert getCostOfCoffee(18, i) == 16 * i

    assert getCostOfCoffee(19, i) == 17 * i

    assert getCostOfCoffee(30, i) == 27 * i
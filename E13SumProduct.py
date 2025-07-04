def calculateSum(numbers):
    length = len(numbers)

    if length ==0: 
        return 0 
    
    else: 
        sum = numbers[0]
        for i in range(length -1):
            sum += numbers[i+1]
        return sum 
    

def calculateProduct(numbers):
    length = len(numbers)

    if length ==0: 
        return 1 
    
    else: 
        prod = numbers[0]
        for i in range(length -1):
            prod *= numbers[i+1]
        return prod

assert calculateSum([]) == 0

assert calculateSum([2, 4, 6, 8, 10]) == 30

assert calculateProduct([]) == 1

assert calculateProduct([2, 4, 6, 8, 10]) == 3840 
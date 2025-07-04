def average(numbers):
    length = len(numbers)

    if length ==0: 
        return None 
    
    else: 
        sum = numbers[0]
        for i in range(length -1):
            sum += numbers[i+1]
        return sum/length 
    

assert average([1, 2, 3]) == 2

assert average([1, 2, 3, 1, 2, 3, 1, 2, 3]) == 2

assert average([12, 20, 37]) == 23

assert average([0, 0, 0, 0, 0]) == 0

import random

random.seed(42)

testData = [1, 2, 3, 1, 2, 3, 1, 2, 3]

for i in range(1000):

    random.shuffle(testData)

    assert average(testData) == 2


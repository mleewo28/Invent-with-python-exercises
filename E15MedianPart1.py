#This exercise was written using python's sort function 

def median(numbers):
    length = len(numbers)
    
    #Account for empty list 
    if length ==0: 
        return None 
    else: 
        sorted = numbers.sort() 
        if length % 2 == 1: 
            index = length//2 
            return sorted[index]
        else: 
            index_one = length//2
            index_two = (length//2) - 1
            median = (sorted[index_one] + sorted[index_two])/2
            return median 
        
assert median([]) == None

assert median([1, 2, 3]) == 2

assert median([3, 7, 10, 4, 1, 9, 6, 5, 2, 8]) == 5.5

assert median([3, 7, 10, 4, 1, 9, 6, 2, 8]) == 6

import random

random.seed(42)

testData = [3, 7, 10, 4, 1, 9, 6, 2, 8]

for i in range(1000):

    random.shuffle(testData)

    assert median(testData) == 6
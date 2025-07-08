def mode(numbers):
    length = len(numbers)

    if length ==0: 
        return None 
    
    old_highest_count = 1 
    new_highest_count = 1
    for i in range(length-1):
        for j in range(i+1,length):
            if numbers[j] == numbers[i]:
                new_highest_count +=1
                if new_highest_count > old_highest_count:
                    mode =numbers[j]
                    old_highest_count = new_highest_count
    
    return mode 

assert mode([]) == None

assert mode([1, 2, 3, 4, 4]) == 4

assert mode([1, 1, 2, 3, 4]) == 1

assert mode([8,5,1,1,3,2,4,7,1,2,4,4,6,1,3]) == 1

import random

random.seed(42)

testData = [1, 2, 3, 4, 4]

for i in range(1000):

    random.shuffle(testData)

    assert mode(testData) == 4
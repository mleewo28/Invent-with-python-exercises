def getSmallest(numbers):
    length = len(numbers)

    #Account for empty list 
    if length == 0:
        return None
    
    else: 
        min_value = numbers[0]
        for i in range(length -1):
            next_value = numbers[i+1]

            if next_value < min_value:
                min_value = next_value
        
        return min_value


def getLargest(numbers):
    length = len(numbers)

    #Account for empty list 
    if numbers =='':
        return None
    
    else: 
        max_value = numbers[0]
        for i in range(length -1):
            next_value = numbers[i+1]

            if next_value > max_value:
                max_value = next_value
        
        return max_value 


assert getSmallest([1, 2, 3]) == 1

assert getSmallest([3, 2, 1]) == 1

assert getSmallest([28, 25, 42, 2, 28]) == 2

assert getSmallest([1]) == 1

assert getSmallest([]) == None

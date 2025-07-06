def sortList(numbers): 
    length = len(numbers)

    for i in range(length - 1): 
        for j in range(i,length):
            current = numbers[i] 
            compare = numbers[j]
            if compare < current:
                #swap 
                numbers[i] = compare 
                numbers[j] = current 
    
    return numbers


assert sortList([5,3,0,6]) == [0,3,5,6]
assert sortList([82,6,1,20,4,75]) == [1,4,6,20,75,82]
assert sortList([10,9,8,7,6,5,4,3,2,1]) == [1,2,3,4,5,6,7,8,9,10]
assert sortList([3, 1, 2]) == [1, 2, 3]
assert sortList([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
assert sortList([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]  # Already sorted
assert sortList([]) == []  # Empty list
assert sortList([10]) == [10]  # Single element
assert sortList([2, 2, 2]) == [2, 2, 2]  # All elements the same
assert sortList([-3, -1, -2, 0, 1]) == [-3, -2, -1, 0, 1]  # Negative numbers
        
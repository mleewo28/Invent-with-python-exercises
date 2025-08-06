def bubbleSort(numbers):

    for i in range(len(numbers)):
        for j in range(i, len(numbers)):
            if numbers[j] < numbers[i]:
                numbers[i],numbers[j] = numbers[j],numbers[i] 

    return numbers



assert bubbleSort([2, 0, 4, 1, 3]) == [0, 1, 2, 3, 4]
assert bubbleSort([9,2,5,7,1,8,4,3,6]) == [1,2,3,4,5,6,7,8,9]
assert bubbleSort([2, 2, 2, 2]) == [2, 2, 2, 2]

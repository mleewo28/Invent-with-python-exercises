def mergeTwoLists(list1,list2):
    sorted_list = []

    #initialize the indexes 
    i1 = 0 
    i2 = 0 

    while i1 < len(list1) and i2 < len(list2):

        if list1[i1] < list2[i2]: 
            sorted_list.append(list1[i1])
            i1 += 1 
        else: 
            sorted_list.append(list2[i2])
            i2 += 1 
    
    if i1 < len(list1): 
        #all elements of list two have been appended 
        for i in range(i1,len(list1)):
            sorted_list.append(list1[i])

    else: 
        for i in range(i2,len(list2)):
            sorted_list.append(list2[i])

    
    return sorted_list 




assert mergeTwoLists([1, 3, 6], [5, 7, 8, 9]) == [1, 3, 5, 6, 7, 8, 9]

assert mergeTwoLists([1, 2, 3], [4, 5]) == [1, 2, 3, 4, 5]

assert mergeTwoLists([4, 5], [1, 2, 3]) == [1, 2, 3, 4, 5]

assert mergeTwoLists([2, 2, 2], [2, 2, 2]) == [2, 2, 2, 2, 2, 2]

assert mergeTwoLists([1, 2, 3], []) == [1, 2, 3]

assert mergeTwoLists([], [1, 2, 3]) == [1, 2, 3]
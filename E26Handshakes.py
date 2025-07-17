def printHandshakes(people):
    length = len(people)
    numberOfShakes = 0 

    for i in range(length-1):
        for j in range((i+1),length):
            print(f"{people[i]} shakes hands with {people[j]}")
            numberOfShakes += 1 

    return numberOfShakes

printHandshakes(['Alice', 'Bob', 'Carol', 'David']) 

assert printHandshakes(['Alice', 'Bob']) == 1

assert printHandshakes(['Alice', 'Bob', 'Carol']) == 3

assert printHandshakes(['Alice', 'Bob', 'Carol', 'David']) == 6



            
        
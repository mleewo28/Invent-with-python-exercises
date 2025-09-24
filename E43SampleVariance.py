def sample_variance(numbers): 
    variance_sum = 0 
    for i in numbers: 
        variance_sum += (i-(sum(numbers)/len(numbers)))**2

    sample_variance = variance_sum/(len(numbers)-1)
    
    return sample_variance

#print(sample_variance([3.4,2.5,4.8,2.9,3.6,2.8,3.3,5.6,3.7,2.8,4.4,4.0,5.2,3.0,4.8]))
#print(sample_variance([227,222,218,217,225,218,216,229,228,221]))
print(sample_variance([]))
# Variance 

Variance measures how far a data set is spread out. It is mathematically defined as the average of the squared differences from the mean.

Given a dataset X, variance can be calculated by the equation:  

Variance = Sum((x - mean(X))^2)/n

With n is the number of data points in the dataset X.

Example:

    X = [1, 1, 2, 2, 3, 1, 4]
    
    # mean(X) = 2
    total = 0
    for i in range(len(X)):
        total = total + (X[i] - mean(X))**2
    var(X) = total/len(X)
    var(X)
    
Output:
    
    8/7
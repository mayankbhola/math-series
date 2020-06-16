"""
    Series indentifier : (first, second)  # first and second element of series
    Series : Actual series corresponding to series-indentifiers

    series_collector : {
        series-indentifiers1 : series1
        series-indentifiers2 : series2
    }

    Example ::

    series_collector : {
        (0, 1) : [0, 1, 1, 2, 3, 5, 8, 13, ...]     # fibonacci series
        (2, 1) : [2, 1, 3, 4, 7, 11, 18, 29, ...]   # lucal seires
        ...
    }
"""
series_collector = dict()

""" A bottom up approach to calculate any series of type X(n) = X(n-1) + X(n-2)
    Time complexity : O(n)
    Optimisation : No re-computation of any index if once computed
"""
def sum_series(index, first=0, second=1) :
    
    if (first, second) not in series_collector :
        series_collector[(first, second)] = [first, second]

    series = series_collector[(first, second)]
    
    if index < len(series): 
        return series[index]

    for i in range(len(series), index+1) :
        series.append(series[i-1] + series[i-2])

    return series[index]


""" Takes input as index and returns fibonacci[index] 
    Fibonacci series : 0, 1, 1, 2, 3, 5, 8, 13, ...
"""
def fibonacci(index) :
    return sum_series(index)


""" Takes input as index and returns lucas[index] 
    Lucas series : 2, 1, 3, 4, 7, 11, 18, 29, ...
"""
def lucas(index) :
    return sum_series(index, 2, 1)



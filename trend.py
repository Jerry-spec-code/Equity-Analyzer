# Computes the weighted moving average of the dataset relative to the number of periods
def movingAverage(dataSet, periods):

    ls = []
    curMean = 0
    for i in range(0, len(dataSet)):
        if i < periods:
            curMean = curMean + (dataSet[i] - curMean) * 2 / (i + 2)
        
        else:
            curMean = curMean + (dataSet[i] - curMean) * 2 / (periods + 1)

        ls.append(curMean)

    return ls

# Computes the linear moving average of the dataset relative to the number of periods
def linearMovingAverage(dataSet, periods):

    ls = []
    curMean = 0
    for i in range(0, len(dataSet)):
        if i < periods:
            curMean = (curMean * i + dataSet[i]) / (i + 1)
        
        else:
            curMean = (curMean * periods + dataSet[i] - dataSet[i - periods]) / (periods)

        ls.append(curMean)

    return ls

# # Computes the mean of the dataset
# def mean(dataSet):
#     sum = 0
#     for num in dataSet:
#         sum += num

#     return sum / len(dataSet)

# # populates an empty list with num a specified number of times
# def populateEmptyList(num, size):
#     ls = []
#     for i in range(0, size):
#         ls.append(num)
    
#     return ls 
    
# # populates a sequential list incrimenting by factor with size number of elements   
# def populateSequentialList(size, factor):
#     ls = []
#     for i in range(0, size):
#         ls.append(i * factor)
    
#     return ls
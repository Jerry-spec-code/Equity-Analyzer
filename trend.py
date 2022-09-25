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
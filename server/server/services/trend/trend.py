# Computes the weighted moving average of the dataset relative to the number of periods
def moving_average(data_set, periods):
    res = []
    cur_mean = 0
    for i in range(0, len(data_set)):
        if i < periods:
            cur_mean = cur_mean + (data_set[i] - cur_mean) * 2 / (i + 2)
        
        else:
            cur_mean = cur_mean + (data_set[i] - cur_mean) * 2 / (periods + 1)

        res.append(cur_mean)

    return res

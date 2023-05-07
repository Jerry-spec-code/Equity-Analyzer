# Computes the weighted moving average of the dataset relative to the number of periods
def moving_average(data_set, periods):

    ls = []
    cur_mean = 0
    for i in range(0, len(data_set)):
        if i < periods:
            cur_mean = cur_mean + (data_set[i] - cur_mean) * 2 / (i + 2)
        
        else:
            cur_mean = cur_mean + (data_set[i] - cur_mean) * 2 / (periods + 1)

        ls.append(cur_mean)

    return ls

# Computes the linear moving average of the dataset relative to the number of periods
def linear_moving_average(data_set, periods):

    ls = []
    cur_mean = 0
    for i in range(0, len(data_set)):
        if i < periods:
            cur_mean = (cur_mean * i + data_set[i]) / (i + 1)
        
        else:
            cur_mean = (cur_mean * periods + data_set[i] - data_set[i - periods]) / (periods)

        ls.append(cur_mean)

    return ls
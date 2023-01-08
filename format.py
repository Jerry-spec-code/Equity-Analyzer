import trend as tr

def interpretAllData(data):
    possibleGraphs = ["", "Opening", "High", "Low", "Closing", "AdjClose", "Volume"]
    res = {}
    res["x-data"] = data[0]
    for i, title in enumerate(possibleGraphs):
        if i == 0: #x-axis data
            continue 
        res[title] = formatData(data[i])
    res["status"] = "success"
    return res

def formatData(data):
    return {
        "y-data" : data,
        "20-day-average" : tr.movingAverage(data, 20),
        "50-day-average" : tr.movingAverage(data, 50),
    }

def processDate(date):
    return date[0:date.find('T')]

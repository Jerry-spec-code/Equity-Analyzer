import csv

PRICES_TXT = 'txtPrices.txt'
PRICES_CSV = 'csvPrices.csv'

def write_to_txt(filename, contents):
    with open(filename, 'w') as f:
        f.write(contents)

def write_to_csv(filename, header, body):
    with open(filename, 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(body)

def read_daily_prices(filename):
    lst = []
    with open(filename) as file:
        for i, line in enumerate(file):
            if i < 2: 
                continue
            else:
                temp = []
                for word in line.split():
                    temp.append(word)
                lst.append(temp)
    return lst

def column_to_list(data):
    return [row for row in data]
import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename = 'death_valley_2014.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    # print(header_row)

    #
    # for index,column_header in enumerate(header_row):
    #     print(index,column_header)
    #
    # high = []
    #
    # for rows in reader:
    #     high.append(rows[1])

    # print(high)
    # count = 0
    # for i in reader:
    #     # print(i)
    #     count +=1
    #     print(i)
    # print(count)

    # convert high string into int


    high ,dates,low = [],[],[]

    for rows in reader:
        try:
            current_date = datetime.strptime(rows[0],"%Y-%m-%d")
            lows = int(rows[3])
            highs = int(rows[1])
        except ValueError:
            print(current_date,'missing data')
        else:
            high.append(highs)
            dates.append(current_date)
            low.append(lows)

    print(dates,high)

    fig = plt.figure(dpi = 125,figsize=(10,6))
    plt.plot(dates, high, c='red',alpha = 0.5)
    plt.plot(dates,low,c = 'blue',alpha = 0.5)

    plt.fill_between(dates,high,low,facecolor = 'blue',alpha = 0.1)

    plt.title('daily high temperature  2014',fontsize = 14)
    fig.autofmt_xdate()
    plt.xlabel (' ',fontsize = '14')
    plt.ylabel ('temperature',fontsize = 14)
    plt.tick_params(axis='both',which = 'major',labelsize = 14)


    plt.show()
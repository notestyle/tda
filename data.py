import pandas as pd
import datetime

# import from csv data
def loadData(limit):
    df = pd.read_csv('DAT_ASCII_EURUSD_M1_2000.csv')
    if limit:
        df = df[:limit]
    arr_value = []

    # convert values to columns
    for row in df['Values']:
        arr_value.append(row.split(';'))

    # merge all converted columns
    df2 = pd.DataFrame(arr_value, columns=['time', 'open', 'high', 'low', 'close', 'volume']) 
    df = df.join(df2)
    # print(df)

    # fix date values and create
    arr_value = []
    for index, row in df.iterrows():
        date, time, close = str(row['Date']), str(row['time']), row['close']
        date_time = datetime.datetime(int(date[:4]), int(date[4:6]), int(date[6:8]), int(time[:2]), int(time[2:4]), int(time[4:6]) )
        # print(date_time, close)
        arr_value.append([date_time, close])

    # clean memory
    df = None
    df2 = None

    df = pd.DataFrame(arr_value, columns=['date_time', 'close']) 
    return df
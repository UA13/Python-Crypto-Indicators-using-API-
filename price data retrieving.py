from binance import Client
import pandas as pd
import datetime
from matplotlib import pyplot as plt

my_API_Key = "API_KEY"
my_API_Secret = "API_SECRET"

def give(shareName, timeframe, limit):
    symbol = shareName + 'USDT'
    API_Key = my_API_Key
    API_Secret = my_API_Secret
    client = Client(API_Key, API_Secret)
    klines = client.get_historical_klines(symbol=symbol, interval=timeframe, limit=limit)
    return klines

def create_excel(shareName, timeframe, limit):
    data = give(shareName, timeframe, limit)
    df = pd.DataFrame(
        data,
        columns=[
            'Open Time', 'Open', 'High', 'Low', 'Close', 'Volume',
            'Close Time', 'Quote asset volume', 'Number of trades',
            'Taker buy base asset volume', 'Taker buy quote asset volume', 'Ignore'
        ]
    )
    df['Datetime'] = pd.to_datetime(df['Open Time'], unit='ms')
    df.index = df['Datetime']
    columns_to_convert = ['Open', 'High', 'Low', 'Close']
    df[columns_to_convert] = df[columns_to_convert].astype(float)
    df.drop(
        [
            'Ignore', 'Open Time', 'Close Time', 'Quote asset volume',
            'Taker buy base asset volume', 'Taker buy quote asset volume'
        ],
        axis=1,
        inplace=True
    )
    return df

data = give('BTC', '1m', 100)
print(data)
df = pd.DataFrame(
    data,
    columns=[
        'Open Time', 'Open', 'High', 'Low', 'Close', 'Volume',
        'Close Time', 'Quote asset volume', 'Number of trades',
        'Taker buy base asset volume', 'Taker buy quote asset volume', 'Ignore'
    ]
)
print(df)

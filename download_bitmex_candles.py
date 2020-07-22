import gzip

import pandas as pd
import requests

url = 'https://1337research-candles.s3-ap-southeast-1.amazonaws.com/bitmex_BTCUSD_1h.csv.gz'
response = requests.get(url)
decompressed = gzip.decompress(response.content)

with open('downloaded_data.csv', 'wb') as f:
    f.write(decompressed)

candles = [line.split(',') for line in decompressed.decode().splitlines()]

df = pd.DataFrame(candles, columns=['startTime', 'open', 'high', 'low', 'close', 'volume'])
df.set_index('startTime', inplace=True)
df.index = pd.to_datetime(df.index, unit='ms')

print(df.tail())

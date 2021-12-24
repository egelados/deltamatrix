import streamlit as st
import yfinance as yf
import numpy as np
import pandas as pd

from urllib.request import urlopen
from PIL import Image

st.write(""" # Delta Matrix """)
#st.title(""" first test """)
#st.header(""" first test """)
st.sidebar.header(""" Delta Matrix """)

def get_ticker(name):
    company = yf.Ticker(name)
    return company

tickers = ["BTC-USD", "ETH-USD", "BNB-USD", "SOL-USD", "ADA-USD", 
           "XRP-USD", "LUNA1-USD", "AVAX-USD", "DOT-USD", "DOGE-USD"]

data = []

for tick in tickers:
    data.append(get_ticker(tick))

histories = []

for datum in data:
    histories.append(datum.history(period="max"))

aths = []

for history in histories:
    aths.append(history["High"].max())

st.table(aths)

df = pd.DataFrame(
    np.random.randn(10, 5),
    columns=('col %d' % i for i in range(5)))

st.table(df)

data = {'Name':['BTC', 'ETH', 'BNB', 'SOL', 'ADA', 'XRP', 'LUNA1', 'AVAX', 'DOT', 'DOGE'],
        'marks':[data[0].info["regularMarketPrice"], data[1].info["regularMarketPrice"], data[2].info["regularMarketPrice"], data[3].info["regularMarketPrice"], data[4].info["regularMarketPrice"], data[5].info["regularMarketPrice"], data[6].info["regularMarketPrice"], data[7].info["regularMarketPrice"], data[8].info["regularMarketPrice"], data[9].info["regularMarketPrice"] ]}
  
# Creates pandas DataFrame.
df2 = pd.DataFrame(data, index =['rank1', 'rank2', 'rank3', 'rank4', 'rank5', 'rank6', 'rank7', 'rank8', 'rank9', 'rank10'])

# data = {'Name':['BTC', 'ETH', 'BNB'],
#         'marks':[data[0].info["regularMarketPrice"], data[1].info["regularMarketPrice"], data[2].info["regularMarketPrice"]]}
  
# # Creates pandas DataFrame.
# df2 = pd.DataFrame(data, index =['rank1', 'rank2', 'rank3'])

st.table(df2)

#pprint(yf.Ticker("BTC-USD").info["regularMarketPrice"])

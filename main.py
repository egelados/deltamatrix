import streamlit as st
import yfinance as yf
import pandas as pd

from urllib.request import urlopen
from PIL import Image

st.write(""" # ATH Delta Matrix """)
st.sidebar.header(""" Thx to @joed4lton from GCC for the idea. Had a few DANG moments preparing this :) """)

def get_ticker(name):
    coin = yf.Ticker(name)
    return coin

tickers = ["BTC-USD", "ETH-USD", "BNB-USD", "SOL-USD", "ADA-USD", 
           "XRP-USD", "LUNA1-USD", "AVAX-USD", "DOT-USD", "DOGE-USD",
           "SHIB-USD", "MATIC-USD"]

data = []
for tick in tickers:
    data.append(get_ticker(tick))

histories = []
for datum in data:
    histories.append(datum.history(period="max"))

aths = []
for history in histories:
    aths.append(history["High"].max())

data2 = {'Coin':[i for i in tickers],
         'ATH': [l for l in aths],
        'Price':[j.history(period="1m")["Close"].values[0] for j in data]}
data2['ATH'][8] = 55.13
data2['Delta'] = [-((l / m) - 1)*100 for l, m in zip(data2['Price'], data2['ATH'])]    

df2 = pd.DataFrame(data2)
df3 = df2.sort_values(by=['Delta'])
styler = df3.style.hide_index().format(subset=['Delta'], decimal=',', precision=4).bar(subset=['Delta'], align="mid")

st.table(styler)

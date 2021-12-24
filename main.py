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
           "LUNA1-USD", "AVAX-USD", "DOT-USD", "DOGE-USD",
           "SHIB-USD", "MATIC-USD", "CRO-USD", "UNI1-USD", "LTC-USD", 
           "LINK-USD", "ALGO-USD"]

logos = [1, 1027, 1839, 5426, 2010, 
         4172, 5805, 6636, 74, 
         5994, 3890, 3635, 7083, 2,
         1975, 4030]

data = []
for tick in tickers:
    data.append(get_ticker(tick))

histories = []
for datum in data:
    histories.append(datum.history(period="max"))

aths = []
for history in histories:
    aths.append(history["High"].max())

data2 = {'Coin': ["<img src=https://s2.coinmarketcap.com/static/img/coins/64x64/"+str(f)+".png width=24 height=24>" for f in logos] ,
         'Ticker': [i for i in tickers],
         'ATH': [l for l in aths],
        'Price': [j.history(period="1m")["Close"].values[0] for j in data]}
data2['ATH'][7] = 55.13
data2['Delta'] = [-((l / m) - 1)*100 for l, m in zip(data2['Price'], data2['ATH'])]    

df2 = pd.DataFrame(data2)
df3 = df2.sort_values(by=['Delta'])

styler2 = df3.style.hide_index().format(subset=['Delta'], decimal=',', precision=2).bar(subset=['Delta'], align="mid")

st.write(styler2.to_html(), unsafe_allow_html=True)

import streamlit as st
import yfinance as yf
import numpy as np
import pandas as pd

from urllib.request import urlopen
from PIL import Image

st.write(""" # Delta Matrix """)
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

data2 = {'Coin':[i for i in tickers],
         'ATH': [l for l in aths],
        'Price':[j.history(period="1m")["Close"].values[0] for j in data]}
data2['ATH'][8] = 55.13

data2['Delta'] = [-((l / m) - 1)*100 for l, m in zip(data2['Price'], data2['ATH'])]    

df2 = pd.DataFrame(data2)
df3 = df2.sort_values(by=['Delta'])
styler = df3.style.hide_index().format(subset=['Delta'], decimal=',', precision=4).bar(subset=['mean'], align="mid")

st.table(styler.to_html(), unsafe_allow_html=True)
#st.table(df2)

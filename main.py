import streamlit as st
import yfinance as yf
import pandas as pd

st.write(""" # ATH Delta Matrix """)
st.sidebar.header(""" Thx to @joed4lton from GCC for the idea. Had a few DANG moments preparing this :) """)

def get_ticker(name):
    coin = yf.Ticker(name)
    return coin

symbols = ["BTC-USD", "ETH-USD", "BNB-USD", "SOL-USD", "ADA-USD", 
           "LUNA1-USD", "AVAX-USD", "DOT-USD", "DOGE-USD",
           "SHIB-USD", "MATIC-USD", "CRO-USD", "UNI1-USD", "LTC-USD", 
           "LINK-USD", "ALGO-USD"]

logos = [1, 1027, 1839, 5426, 2010, 
         4172, 5805, 6636, 74, 
         5994, 3890, 3635, 7083, 2,
         1975, 4030]

tickers = []
for symbol in symbols:
    tickers.append(get_ticker(symbol))

histories = []
for datum in tickers:
    histories.append(datum.history(period="max"))

aths = []
for history in histories:
    aths.append(history["High"].max())

data = {'Coin': ["<img src=https://s2.coinmarketcap.com/static/img/coins/64x64/"+str(f)+".png width=24 height=24>" for f in logos] ,
         'Ticker': [i for i in symbols],
         'ATH': [l for l in aths],
        'Price': [j.history(period="1m")["Close"].values[0] for j in tickers]}
data['ATH'][7] = 55.13 # ugly ath price fix for DOT because of yahoo's finance error
data['Delta'] = [-((l / m) - 1)*100 for l, m in zip(data['Price'], data['ATH'])]    

dataframe = pd.dataFrame(data)
sorted_dataframe = dataframe.sort_values(by=['Delta'])

styled_sorted_dataframe = sorted_dataframe.style.hide_index().format(subset=['Delta'], decimal=',', precision=2).bar(subset=['Delta'], align="mid")

st.write(styled_sorted_dataframe.to_html(), unsafe_allow_html=True)

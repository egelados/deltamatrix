import streamlit as st
import yfinance as yf
import pandas as pd

def get_ticker(name, unit):
    coin = yf.Ticker(name + "-" + unit)
    return coin

st.write(""" # ATH Delta Matrix """)
st.sidebar.header(""" Thx to @joed4lton from GCC for the idea. Had a few DANG moments preparing this :) """)
unit_of_denomination = st.sidebar.checkbox('Denominate in sats instead of fiat')

symbols = ["BTC", "ETH", "BNB", "SOL", "ADA", 
           "LUNA1", "AVAX", "DOT", "DOGE", "MANA",
           "SHIB", "MATIC", "CRO", "UNI1", "LTC", 
           "LINK", "ALGO", "ATOM", "VET", "EGLD"]

logos = [1, 1027, 1839, 5426, 2010, 
         4172, 5805, 6636, 74, 1966,
         5994, 3890, 3635, 7083, 2,
         1975, 4030, 3794, 3077, 6892]

tickers = []
for symbol in symbols:
    if unit_of_denomination:
        tickers.append(get_ticker(symbol,"BTC"))
    else:
        tickers.append(get_ticker(symbol,"USD"))

histories = []
for ticker in tickers:
    histories.append(ticker.history(period="max"))

aths = []
for history in histories:
    aths.append(history["High"].max())

imgsrc_prefix = "<img src=https://s2.coinmarketcap.com/static/img/coins/64x64/"
imgsrc_suffix = ".png width=24 height=24>"

if unit_of_denomination:
        data = {'Coin': [imgsrc_prefix+ str(logo) + imgsrc_suffix for logo in logos[1:]] ,
            'Ticker': [symbol for symbol in symbols[1:]],
            'ATH': [ath for ath in aths[1:]],
            'Price': [ticker.history(period="1m")["Close"].values[0] for ticker in tickers[1:]]}
else:
        data = {'Coin': [imgsrc_prefix+ str(logo) + imgsrc_suffix for logo in logos] ,
            'Ticker': [symbol for symbol in symbols],
            'ATH': [ath for ath in aths],
            'Price': [ticker.history(period="1m")["Close"].values[0] for ticker in tickers]}

data['ATH'][5] = 101.27 # ugly ath price fix for LUNA because of yahoo's finance error
data['ATH'][7] = 55.13 # ugly ath price fix for DOT because of yahoo's finance error
data['Delta'] = [-((price / ath) - 1)*100 for price, ath in zip(data['Price'], data['ATH'])]    

dataframe = pd.DataFrame(data)
sorted_dataframe = dataframe.sort_values(by=['Delta'])

styled_sorted_dataframe = sorted_dataframe.style.hide_index().format(subset=['ATH','Price','Delta'], decimal='.', precision=2).bar(subset=['Delta'], align="mid")

st.write(styled_sorted_dataframe.to_html(), unsafe_allow_html=True)

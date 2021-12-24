def get_ticker(name):
    company = yf.Ticker(name)
    return company

c1 = get_ticker(""" AAPL """)
apple = yf.download("AAPL", start="2021-01-01", end="2021-12-31")

data1 = c1.history(period="3mo")

st.write(" ### Apple ")
st.write(c1.info['longBusinessSummary'])
st.write(apple)
st.line_chart(data1.values)

Bitcoin = "BTC-USD"
BTC_DATA = yf.Ticker(Bitcoin)
BTCHis = BTC_DATA.history(period="max")

BTC = yf.download(Bitcoin, start="2021-12-22", end="2021-12-22")

st.write(""" Bitcoin """)
imageBTC = Image.open(urlopen("https://s2.coinmarketcap.com/static/img/coins/64x64/1.png"))
st.image(imageBTC)
bla = BTCHis["High"].max()
st.write(bla)
st.table(BTC)
st.bar_chart(BTCHis.Close)

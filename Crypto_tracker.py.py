import urllib.request as ur
import json
import streamlit as st
import pandas as pd
import plotly.express as px

url = ur.urlopen('https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd')

data = json.load(url)
name = []
values = []
id = []
m_cap = []
vol = []
high = []
low = []
ts = []
rank = []


def mo(namee):
    for i in range(len(name)):
        if name[i] == namee:
            break
    return i

for i in range(len(data)):
    data2 = data[i]
    id.append(data2['id'])
    name.append(data2['name'])
    values.append(data2['current_price'])
    m_cap.append(data2['market_cap'])
    vol.append(data2['total_volume'])
    high.append(data2['high_24h'])
    low.append(data2['low_24h'])
    ts.append(data2['total_supply'])
    rank.append(data2['market_cap_rank'])


df = pd.DataFrame({
  'Name': name[0:10],
  'Total Supply': ts[0:10],
  'Rank': rank[0:10],
  'Market Capital': m_cap[0:10],
  'High Value' : high[0:10],
  'Low Value' : low[0:10],
})

df = df.set_index('Rank')
barg = px.bar(df,x='Name',y='Total Supply',color='Name')
bar2 = px.bar(df,x='Name',y='Market Capital',color='Name')


st.title('Crypto')
#st.markdown("Select Currency")

#st,st = st.columns([6,4])

opt = st.selectbox("Select Currency", name, index=0,)# format_func=mo,)

pr = st.markdown('Current Value: '+str(values[mo(opt)])+'$')
mc = st.markdown('Market Capital Value: '+str(m_cap[mo(opt)])+'$')
volu = st.markdown('Total Volume Sale: '+str(vol[mo(opt)]))
hi = st.markdown('Highest Value: '+str(high[mo(opt)])+'$')
lo = st.markdown('Lowest Value: '+str(low[mo(opt)])+'$')
#no = st.markdown(name[0:10])

st.markdown('        ')
st.markdown('        ')
st.markdown('        ')
st.markdown('Top 10 Current Currency by Market Rank')
st.write(df)

st.markdown('        ')
st.markdown('        ')
st.markdown('        ')

st.markdown('Top 10 Current Total Supply')
st.plotly_chart(barg)
st.markdown('Top 10 Current Market Capital')
st.plotly_chart(bar2)


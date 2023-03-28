import streamlit as st
from datetime import datetime

from Functions.Class.order import Order

@st.cache_data
def reading_orders(df):
    orders = []
    for _, row in df.iterrows():
        source = row['Source']
        symbol = row['Symbol']
        timestamp = row['Timestamp']
        bid = row['Bid']
        ask = row['Ask']
        is_buy = row['BuySELL'].upper() == 'BUY'
        executed_volume = row['ExecuteVolume']
        send_volume = row['SendVolume']
        price = row['Price']
        order = Order(source, symbol, timestamp, bid, ask, is_buy, executed_volume, send_volume, price)
        orders.append(order)
    return orders


def show_orders(orders):
    for i, order in enumerate(orders, 1):
        st.write(f"Order {i}: {order}")
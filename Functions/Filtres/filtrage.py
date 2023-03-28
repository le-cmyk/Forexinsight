import pandas as pd

def filter_orders(df_orders, symbol=None, date=None, start_hour=None, end_hour=None, is_buy=None, threshold=None):
    filtered_orders = []
    for index, order in df_orders.iterrows():
        # Filter by symbol
        if symbol is not None and order['Symbol'] != symbol:
            continue
        
        # Filter by date
        if date is not None and order['Timestamp'].date() != date:
            continue
        
        # Filter by hour
        if start_hour is not None and order['Timestamp'].hour < start_hour:
            continue
        if end_hour is not None and order['Timestamp'].hour > end_hour:
            continue
        
        # Filter by buy/sell
        if is_buy is not None and order['BuySELL'] != is_buy:
            continue
        
        # Filter by executed volume proportion
        if threshold is not None:
            proportion = order['ExecuteVolume'] / order['SendVolume']
            if proportion < threshold / 100:
                continue
        
        # Add to filtered orders
        filtered_orders.append(order)
        
    return pd.DataFrame(filtered_orders)

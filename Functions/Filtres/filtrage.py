def filter_orders(orders, symbol=None, start_date=None, end_date=None, start_hour=None, end_hour=None, is_buy=None, threshold=None):
    filtered_orders = []
    for order in orders:
        # Filter by symbol
        if symbol is not None and order.symbol != symbol:
            continue
        
        # Filter by date
        if start_date is not None and order.timestamp < start_date:
            continue
        if end_date is not None and order.timestamp > end_date:
            continue
        
        # Filter by hour
        if start_hour is not None and order.timestamp.hour < start_hour:
            continue
        if end_hour is not None and order.timestamp.hour >= end_hour:
            continue
        
        # Filter by buy/sell
        if is_buy is not None and order.isBuy != is_buy:
            continue
        
        # Filter by executed volume proportion
        if threshold is not None:
            proportion = order.executedVolume / order.sendVolume
            if proportion < threshold / 100:
                continue
        
        # Add to filtered orders
        filtered_orders.append(order)
        
    return filtered_orders

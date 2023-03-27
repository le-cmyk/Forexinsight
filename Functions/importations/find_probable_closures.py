from typing import List


from Functions.Class.order import Order
from Functions.Class.pairorder import Pairorder

def Find_probable_closures(orders : List[Order]) -> List[Order]:
    # Filter the orders to get only the opening orders
    opening_orders = [order for order in orders if order.isBuy]

    # Sort the opening orders by their execution time
    opening_orders.sort(key=lambda o: o.Timestamp())

    # Create a stack to keep track of the opening orders that haven't been closed yet
    opening_order_stack = []

    # Create a list to hold the pairs of opening and closing orders
    probable_closures = []

    # Iterate over all the orders, looking for closing orders for each opening order
    for order in orders:
        if not order.isBuy:
            # This is a closing order, so look for a matching opening order on the stack
            if len(opening_order_stack) > 0:
                opening_order = opening_order_stack[-1]
                if opening_order.Symbol() == order.Symbol(): # We have not taking into acount the volue executed  && opening_order.executed_volume == order.executed_volume
                    # This closing order probably matches the opening order, so add them to the list of probable closures
                    probable_closures.append((opening_order, order))
                    opening_order_stack.pop()
        else:
            # This is an opening order, so add it to the stack of opening orders
            opening_order_stack.append(order)

    return probable_closures


def CreatePairorder ( listorders) -> List[Pairorder]:
    l_paire_order=Find_probable_closures(listorders)
    res=[]
    for pair in l_paire_order:
        element=Pairorder(pair[0].price,pair[1].price,0,pair[1].timestamp-pair[0].timestamp,pair[0].sendVolume)
        res.append(element)
    return res


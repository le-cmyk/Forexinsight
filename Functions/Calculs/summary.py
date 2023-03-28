def info_list_order(orders):
    res={}
    volume=0
    benef=0
    simulated_benef=0
    if orders[0].isBuy:
        res["start"]="Positif"
    else : 
        res["start"]=f'Negatif of {orders[0].executedVolume} (volume)'
        volume=orders[0].executedVolume
        simulated_benef=orders[0].executedVolume*orders[0].price

    for i in range(len(orders)):
        order=orders[i]

        if order.isBuy:
            volume+=order.executedVolume
            simulated_benef-=order.executedVolume*order.price

        else:
            volume-=order.executedVolume
            simulated_benef+=order.executedVolume*order.price
    
    res["position"]=volume
    res["benefice"]=simulated_benef

    return res
    


from datetime import datetime
from Functions.Class.entry import Entry

class Order(Entry):
    def __init__(self, source="", symbol="", timestamp=datetime.now(), bid=0, ask=0, isBuy=True, executedVolume=0, sendVolume=0, price=0):
        super().__init__(source, symbol, timestamp, bid, ask)
        self.isBuy = isBuy
        self.executedVolume = executedVolume
        self.sendVolume = sendVolume
        self.price = price

    @property
    def IsBuy(self):
        return self.isBuy

    @property
    def ExecutedVolume(self):
        return self.executedVolume

    @property
    def SendVolume(self):
        return self.sendVolume

    @property
    def Price(self):
        return self.price

    def __str__(self):
        if self.isBuy:
            return super().__str__() + f" ,Buy Volume : {self.sendVolume} ,Buy Volume Executed : {self.executedVolume} ,at : {self.price}"
        else:
            return super().__str__() + f" ,Sell Volume : {self.sendVolume} ,Sell Volume Executed : {self.executedVolume} ,at : {self.price}"

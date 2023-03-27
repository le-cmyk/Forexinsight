from datetime import datetime

class Entry:
    def __init__(self, source="", symbol="", timestamp=datetime.now(), bid=0, ask=0):
        self.source = source
        self.symbol = symbol
        self.timestamp = timestamp
        self.bid = bid
        self.ask = ask
        self.mid = bid + ask / 2

    def Source(self):
        return self.source

    def Symbol(self):
        return self.symbol

    def Timestamp(self):
        return self.timestamp

    def Bid(self):
        return self.bid

    def Ask(self):
        return self.ask

    def Mid(self):
        return self.mid

    def __str__(self):
        return f"{self.symbol} {self.timestamp.strftime('%Y-%m-%d %H:%M:%S.%fZ')} ,Bid : {self.bid} ,Ask : {self.ask}"



import pandas as pd
from datetime import datetime
from typing import List

from Functions.Class.currencyExchangeRate import CurrencyExchangeRate


def Read_exchange_rates_csv(filename: str) -> List[CurrencyExchangeRate]:
    # Read the CSV file into a Pandas DataFrame
    df = pd.read_csv(filename, delimiter=";")

    # Convert the data to a list of CurrencyExchangeRate objects
    exchangeRates: List[CurrencyExchangeRate] = []
    for index, row in df.iterrows():
        date = datetime.strptime(row["Date"], "%d/%m/%Y %H:%M:%S")
        bid = float(row["Bid"].replace(",", "."))
        ask = float(row["Ask"].replace(",", "."))
        exchangeRates.append(CurrencyExchangeRate(date, bid, ask))

    return exchangeRates

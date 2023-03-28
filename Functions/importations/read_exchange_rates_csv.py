import pandas as pd
from datetime import datetime
from typing import List
import os
import streamlit as st

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


def get_exchange_rates_by_date( df: pd.DataFrame,desired_date,end_date=None, plus=1) -> pd.DataFrame:
    start_time = desired_date-pd.Timedelta(seconds=plus*2)
    
    if end_date is not None:
        end_time = end_date + pd.Timedelta(hours=plus)
    else:
        end_time = desired_date + pd.Timedelta(hours=plus)
    df= df.query('Timestamp >= @start_time and Timestamp < @end_time')

    df = df.set_index('Timestamp')
    df = df.resample('1S').ffill()
    df = df.reset_index()
    return df




#Find the file for a specific order
def find_data(order)-> str:
    # Extract symbol and year from the order
    symbol = order.symbol
    year = order.timestamp.year
    
    # Define the folder name based on the symbol and year
    folder_name = f"Exness_{symbol}m_{year}"
    
    # Define the file name based on the date of the order
    file_name = f"{order.timestamp.date()}.csv"

    # Define the path to the file
    file_path = "Data/DATA/"+folder_name
    st.write()

    # Check if the file exists, return the file path if it does
    if file_name in os.listdir(file_path):
        return file_path+"/"+file_name
    else:
        raise ValueError(f"No data file found for order {order}")



def generate_exanche_rates(orders,hour=1)-> List[CurrencyExchangeRate]:

    file_path=find_data(orders[0])
    df=pd.read_csv(file_path)
    # Convertir la colonne Timestamp en datetime
    df["Timestamp"] = pd.to_datetime(df["Timestamp"], format="%Y-%m-%d %H:%M:%S.%fZ")

    res=get_exchange_rates_by_date(df,orders[0].timestamp,orders[-1].timestamp,1)
    return res




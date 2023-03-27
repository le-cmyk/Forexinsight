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


def get_exchange_rates_by_date(desired_date , df: pd.DataFrame,plushour=1 ) -> List[CurrencyExchangeRate]:

    # Création d'une liste pour stocker les données extraites du DataFrame
    exchange_rates = []

    # Parcours de toutes les données du DataFrame
    for index, row in df.iterrows():
        # Extraction des données de la ligne actuelle
        date = row['Timestamp']
        bid = row['Bid']
        ask = row['Ask']

        # Vérification si la date correspond à celle souhaitée
        if date >= desired_date and date <= desired_date.replace(hour=desired_date.hour + plushour):
            # Ajout des données extraites à la liste
            exchange_rates.append(CurrencyExchangeRate(date, bid, ask))

    return exchange_rates


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


def generate_exanche_rate(order,hour=1)-> List[CurrencyExchangeRate]:

    file_path=find_data(order)
    df=pd.read_csv(file_path)
    # Convertir la colonne Timestamp en datetime
    df["Timestamp"] = pd.to_datetime(df["Timestamp"], format="%Y-%m-%d %H:%M:%S.%fZ")


    res=get_exchange_rates_by_date(order.timestamp,df)

    return res




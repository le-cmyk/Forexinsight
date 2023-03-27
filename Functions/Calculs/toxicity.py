from typing import List
from datetime import datetime, timedelta
import numpy as np
from pandas import DataFrame
import streamlit as st

from Functions.Class.order import Order

def Toxicity(entries: List[Order], n: int = -1) -> List[float]:
    # If no length of study specified we check the whole dataset
    if n == -1:
        n = len(entries)
    # Sort entries by timestamp using quicksort
    entries.sort(key=lambda x: x.Timestamp())
    # Lists to store returns, addtoxicity, toxicity and durations
    returns = [0.0] * n
    addtoxicity = [0.0] * n
    toxicity = [0.0] * n
    durations = [timedelta(0)] * n
    # Calculate returns, durations, addtoxicity, and toxicity in a single loop
    for i in range(n):
        if i == 0:
            # For the first entry, set duration and return to 0
            durations[i] = timedelta(0)
            returns[i] = 0.0
        else:
            # For other entries, calculate duration and return
            durations[i] = entries[i].Timestamp() - entries[0].Timestamp()
            returns[i] = (entries[i].Mid() / entries[0].Mid() - 1) * 10000
            addtoxicity[i] = (durations[i].total_seconds() - durations[i-1].total_seconds()) * returns[i]
            toxicity[i] = toxicity[i-1] + addtoxicity[i]
    return toxicity




def show_Toxicity(list_orders):
    list_toxic=Toxicity(list_orders)
    st.write(list_toxic)

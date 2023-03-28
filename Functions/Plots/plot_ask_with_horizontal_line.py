import plotly.graph_objs as go
import streamlit as st
import pandas as pd

from Functions.importations.read_exchange_rates_csv import generate_exanche_rates


def Plot_ask_with_horizontal_line(orders):

    df=generate_exanche_rates(orders)
    df_2 = df.set_index('Timestamp')

    fig = go.Figure()
    # Add general evolution of Ask column
    fig.add_trace(go.Scatter(x=df_2.index, y=df_2['Ask'], name='Ask'))

    

    for i in range(len(orders)):
        order=orders[i]
        start_time = order.timestamp
        ask_value = order.price

        if not order.isBuy:
            fig.add_trace(
                go.Scatter(
                    x=[start_time],
                    y=[ask_value],
                    mode='markers',
                    marker=dict(size=10, symbol='triangle-down', color='green'),
                    name=f'Sell (order n°{i})'
                )
            )
        else :
            # Add horizontal line
            fig.add_shape(
                go.layout.Shape(
                    type='line',
                    x0=start_time,
                    y0=ask_value,
                    x1=start_time +  pd.Timedelta(hours=1),
                    y1=ask_value,
                    line=dict(color='red', width=2, dash='dash'),
                    name=f'Buy (order n°{i})'
                )
            )
    fig.update_layout(title='Ask with horizontal line',
                      xaxis_title='Timestamp',
                      yaxis_title='Ask')
    return fig



import plotly.graph_objs as go
import streamlit as st

from Functions.importations.read_exchange_rates_csv import generate_exanche_rate

def Plot_ask_with_horizontal_line(order):

    df=generate_exanche_rate(order)
    start_time=order.timestamp
    ask_value=order.price
    df_2 = df.set_index('Timestamp')

    fig = go.Figure()
    # Add general evolution of Ask column
    fig.add_trace(go.Scatter(x=df_2.index, y=df_2['Ask'], name='Ask'))
    
    # Add horizontal line
    fig.add_shape(
        go.layout.Shape(
            type='line',
            x0=start_time,
            y0=ask_value,
            x1=df_2.index.max(),
            y1=ask_value,
            line=dict(color='red', width=2, dash='dash')
        )
    )

    fig.update_layout(title='Ask with horizontal line',
                      xaxis_title='Timestamp',
                      yaxis_title='Ask')
    return fig

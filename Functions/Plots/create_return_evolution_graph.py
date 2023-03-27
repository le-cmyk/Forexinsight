import plotly.graph_objects as go
import streamlit as st

@st.cache_data
def Create_return_evolution_graph(orders):
    # Initialize the plot figure
    fig = go.Figure()
    fig.update_layout(title="Return Evolution Graph")

    # Create two scatter traces for buy and sell orders
    buy_trace = go.Scatter(x=[], y=[], mode='markers', marker=dict(symbol='circle', size=5, color='blue'), name="Buy")
    sell_trace = go.Scatter(x=[], y=[], mode='markers', marker=dict(symbol='square', size=5, color='red'), name="Sell")

    # Iterate through the orders and add the corresponding data points to the appropriate trace
    for order in orders:
        x = order.Duration
        y = order.Position * (order.Prix_fin - order.Prix_debut) / order.Prix_debut

        if order.Position > 0:
            buy_trace['x'].append(x)
            buy_trace['y'].append(y)
        else:
            sell_trace['x'].append(x)
            sell_trace['y'].append(y)

    # Add the traces to the figure
    fig.add_trace(buy_trace)
    fig.add_trace(sell_trace)

    # Show legend
    fig.update_layout(showlegend=True, legend=dict(x=1, y=0, bgcolor='rgba(255, 255, 255, 0.5)'))

    return fig

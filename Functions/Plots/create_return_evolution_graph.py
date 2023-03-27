import plotly.graph_objs as go

def Afficher_investissements(pairorders):
    investissements = []
    for pairorder in pairorders:
        investissement = (pairorder.Prix_fin - pairorder.Prix_debut) * pairorder.Volume
        investissements.append(investissement)

    trace = go.Bar(
        x=list(range(len(pairorders))),
        y=investissements,
        marker=dict(
            color='rgba(50, 171, 96, 0.6)',
            line=dict(
                color='rgba(50, 171, 96, 1.0)',
                width=2
            )
        ),
        opacity=0.6
    )

    layout = go.Layout(
        title='Investissements pour chaque Pairorder',
        xaxis=dict(
            title='Number of Order',
            tickmode='linear',
            tick0=0,
            dtick=1
        ),
        yaxis=dict(
            title='Return'
        ),
        bargap=0.2,
        bargroupgap=0.1
    )

    fig = go.Figure(data=[trace], layout=layout)
    return fig


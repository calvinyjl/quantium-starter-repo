import pandas
from dash import Dash, html, dcc
from plotly.express import line

data = pandas.read_csv("./combined.csv")
data = data.sort_values(by="date")

app = Dash()

fig = line(data, x="date", y="sales", title="Pink Morsel Sales")

app.layout = html.Div(
    html.H1(children="Pink Morsel Sales"),

    dcc.Graph(id='morsel-graph', figure=fig)
)

if __name__ == '__main__':
    app.run()
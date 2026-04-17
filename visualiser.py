import pandas
from dash import Dash, html, dcc, Input, Output
from plotly.express import line

COLORS = {
    "primary": "#1E2A3A",
    "secondary": "#2E4A6A",
    "font": "#E8F4FD"
}

data = pandas.read_csv("./combined.csv")
data = data.sort_values(by="date")

app = Dash()

def generate_figure(data):
    fig = line(data, x="date", y="sales", title="Pink Morsel Sales")
    fig.update_layout(
        plot_bgcolor=COLORS["secondary"],
        paper_bgcolor=COLORS["primary"],
        font_color=COLORS["font"]
    )
    return fig

region_picker = dcc.RadioItems(
    ["north", "east", "south", "west", "all"],
    "north",
    id="region_picker",
    inline=True,
)

@app.callback(
    Output("morsel-graph", "figure"),
    Input("region_picker", "value")
)
def update_graph(region):
    if region == "all":
        trimmed_data = data
    else:
        trimmed_data = data[data["region"] == region]
    return generate_figure(trimmed_data)

app.layout = html.Div(
    [
        html.H1(children="Pink Morsel Sales", id='header'),

        dcc.Graph(id='morsel-graph', figure=generate_figure(data)),

        html.Div(
            [region_picker],
            style={"font-size": "150%"}
        )
    ],
    style={
        "textAlign": "center",
        "background-color": COLORS["primary"],
        "color": "white",
        "border-radius": "20px"
    }
)

if __name__ == '__main__':
    app.run()
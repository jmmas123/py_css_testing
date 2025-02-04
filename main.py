import dash
from dash import dcc, html
import dash_bootstrap_components as dbc

app = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.CYBORG],  # Keep Bootstrap theme
)

app.layout = html.Div(
    [
        # Background container (behind everything)
        html.Div(className="background-container"),

        # Blur Overlay Layer
        html.Div(className="overlay"),

        # Main Dashboard Content
        dbc.Container(
            [
                dbc.Row(
                    [
                        dbc.Col(html.Div("Sidebar", className="sidebar-container"), width=2),
                        dbc.Col(html.Div("Main Content", className="content-container"), width=10),
                    ],
                    className="main-container",
                )
            ],
            fluid=True,
            className="dash-container",
            style={"background": "transparent"},  # <== This ensures it remains transparent
        ),
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)
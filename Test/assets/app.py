import dash
import dash_bootstrap_components as dbc
from dash import html

# Initialize the Dash app with Bootstrap theme
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Apply custom font
app.index_string = '''
<!DOCTYPE html>
<html>
    <head>
        <title>Financial Inclusion Dashboard</title>
        <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600&display=swap" rel="stylesheet">
    </head>
    <body style="font-family: 'Inter', sans-serif;">
        {%app_entry%}
        <footer>{%config%}{%scripts%}{%renderer%}</footer>
    </body>
</html>
'''

# Layout
app.layout = dbc.Container([
    html.H1("📘 Financial Inclusion Dashboard", className="display-4 text-center mb-4", style={"fontWeight": "600"}),

    html.P(
        "Explore how financial inclusion has evolved globally over the past decade. "
        "Analyze key demographic trends, barriers, and clusters using interactive visualizations.",
        className="lead text-center mb-5"
    ),

    dbc.Row([
        dbc.Col(dbc.Card([
            dbc.CardBody([
                html.H5("📊 Trends", className="card-title"),
                html.P("Track how financial inclusion has evolved globally and regionally.", className="card-text")
            ])
        ], className="mb-4 shadow-sm h-100"), md=3),

        dbc.Col(dbc.Card([
            dbc.CardBody([
                html.H5("👤 Demographics", className="card-title"),
                html.P("Explore the role of age, gender, education, and income.", className="card-text")
            ])
        ], className="mb-4 shadow-sm h-100"), md=3),

        dbc.Col(dbc.Card([
            dbc.CardBody([
                html.H5("🚧 Barriers", className="card-title"),
                html.P("Identify key obstacles to financial access across groups.", className="card-text")
            ])
        ], className="mb-4 shadow-sm h-100"), md=3),

        dbc.Col(dbc.Card([
            dbc.CardBody([
                html.H5("🌐 Clusters", className="card-title"),
                html.P("See how countries group based on financial behavior patterns.", className="card-text")
            ])
        ], className="mb-4 shadow-sm h-100"), md=3),
    ], justify="center"),

], fluid=True, style={
    "background": "linear-gradient(120deg, #e0f7fa 0%, #ffffff 100%)",
    "minHeight": "100vh",
    "padding": "50px 20px"
})

# Run the app
if __name__ == "__main__":
    app.run_server(debug=True)

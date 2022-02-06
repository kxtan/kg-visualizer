import dash
from dash.dependencies import Input, Output
import plotly.express as px
from modules.util import Util
from modules.layout import Layout
from modules.callbacks import register_callbacks
import dash_bootstrap_components as dbc

util = Util()
layout = Layout()

default_elements = util.process_df(util.read_sample_data())

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.LUMEN])
server = app.server
app.layout = layout.main_layout(default_elements)
register_callbacks(app)

if __name__ == '__main__':
    app.run_server()
import dash
from dash.dependencies import Input, Output
import plotly.express as px
from modules.util import Util
from modules.layout import Layout
from modules.callbacks import register_callbacks

util = Util()
layout = Layout()

default_elements = util.process_df(util.read_sample_data())

app = dash.Dash(__name__)
app.layout = layout.main_layout(default_elements)
register_callbacks(app)

app.run_server(debug=True)
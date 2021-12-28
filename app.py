import dash
from dash.dependencies import Input, Output
import plotly.express as px
from modules.util import Util
from modules.layout import Layout

util = Util()
layout = Layout()

default_elements = util.process_df(util.read_sample_data())

app = dash.Dash(__name__)
app.layout = layout.main_layout(default_elements)

app.run_server(debug=True)
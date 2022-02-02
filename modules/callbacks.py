from dash.dependencies import Input, Output, State
from modules.util import Util
import base64
import pandas as pd
import io


def register_callbacks(app):

    @app.callback(
        Output('kg-cytoscape', 'elements'),
        [Input("upload-data", "filename"), Input("upload-data", "contents")],
    )
    def update_kg(filename, contents):
        """Save uploaded files and regenerate the file list."""

        util = Util()

        if contents is None:
            elements = util.process_df(util.read_sample_data())
            return elements

        _, content_string = contents.split(",")
        
        decoded = base64.b64decode(content_string)
        df = pd.read_csv(io.StringIO(decoded.decode('utf-8')))
        elements = util.process_df(df)

        return elements

    @app.callback(Output('test', 'children'),
        Input('kg-cytoscape', 'tapNodeData'), 
        State('kg-cytoscape', 'elements')
    )
    def node_selected(data, elements):
        
        node = data["label"]
        util = Util()
        df = util.df_from_cytoscape_list(elements)
        
        return f"Selected Node : {node}"
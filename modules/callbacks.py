from dash.dependencies import Input, Output
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

        content_type, content_string = contents.split(",")
        print(content_type)
        decoded = base64.b64decode(content_string)

        df = pd.read_csv(io.StringIO(decoded.decode('utf-8')))

        elements = util.process_df(df)

        return elements
from dash import html
from dash import dcc
import dash_cytoscape as cyto
import dash_bootstrap_components as dbc


class Layout:
    """Layout for Dash Cytoscape knowledge graph visualizer
    """

    def main_layout(self, kg_elements):

        return html.Div(
            [
                self.upload_layout(),
                self.kg_layout(kg_elements),
            ]
        )

    def upload_layout(self):

        return html.Div(
            [
                #dbc.Row(dbc.Col(html.H1("Knowledge Graph Visualizer"))),
                dbc.Row(
                    dbc.NavbarSimple(
                        brand="Knowledge Graph Visualizer",
                        brand_href="#",
                        color="primary",
                        dark=True,
                    )
                ),
                #dbc.Row(dbc.Col(html.H2("Upload"))),
                dbc.Row(
                    dbc.Col(
                        dcc.Upload(
                            id="upload-data",
                            children=html.Div(
                                ["Drag and drop or click to select a file to upload."]
                            ),
                            style={
                                "width": "100%",
                                "height": "60px",
                                "lineHeight": "60px",
                                "borderWidth": "1px",
                                "borderStyle": "dashed",
                                "borderRadius": "5px",
                                "textAlign": "center",
                                "margin": "10px",
                            },
                            multiple=False,
                        ),
                        width={"size": 6, "offset": 3},
                    )
                ),
            ]
        )

    def kg_layout(self, kg_elements:list)-> html.Div:
        """Main layout for knowledge graph visualizer

        Args:
            kg_elements (list): cytoscape friendly items for knowledge graph

        Returns:
            html.Div: html object for main layout
        """

        return html.Div(
            [
                #dbc.Row(dbc.Col(html.H2("Knowledge Graph"))),
                dbc.Row(
                    dbc.Col(
                        dbc.Spinner(
                            cyto.Cytoscape(
                                id='kg-cytoscape',
                                elements=kg_elements,
                                #layout={'name': 'breadthfirst'},
                                style={'width': '100%', 'height': '700px'},
                                stylesheet=[
                                    {
                                        'selector': 'edge', 
                                        'style': { 
                                            'label': 'data(label)',
                                            'target-arrow-shape': 'triangle',
                                            'target-arrow-color': 'black',
                                            'source-arrow-color': 'black',
                                            'line-color': '#333',
                                            #'width': "100%",
                                            'curve-style': 'bezier'
                                        },
                                    },
                                    {'selector': 'node', 'style': { 'label': 'data(label)'}},
                                ],
                            )
                        )
                    )
                )
            ]
        )
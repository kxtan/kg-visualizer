from dash import html
from dash import html
import dash_cytoscape as cyto


class Layout:
    """Layout for Dash Cytoscape knowledge graph visualizer
    """

    def main_layout(kg_elements:list)-> html.Div:
        """Main layout for knowledge graph visualizer

        Args:
            kg_elements (list): cytoscape friendly items for knowledge graph

        Returns:
            html.Div: html object for main layout
        """

        html.Div([
            html.P("Dash Cytoscape:"),
            cyto.Cytoscape(
                id='cytoscape',
                elements=kg_elements,
                layout={'name': 'breadthfirst'},
                style={'width': '2000px', 'height': '4000px'},
                stylesheet=[
                    {
                        'selector': 'edge', 
                        'style': { 
                            'label': 'data(label)',
                            'target-arrow-shape': 'triangle',
                            'target-arrow-color': 'black',
                            'source-arrow-color': 'black',
                            'line-color': '#333',
                            'width': 1.5,
                            'curve-style': 'bezier'
                        },
                    },
                    {'selector': 'node', 'style': { 'label': 'data(label)'}},
                ],
            )
        ])
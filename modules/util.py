import pandas as pd


class Util:
    """Utility class for knowledge graph visualizer
    """

    def read_sample_data(self, sample_path="data/sample.csv") -> pd.DataFrame:
        """[summary]

        Args:
            sample_path (str, optional): [description]. Defaults to "data/sample.csv".

        Returns:
            pd.DataFrame: [description]
        """

        return pd.read_csv(sample_path)


    def process_df(self, df:pd.DataFrame, subj_col="subject", 
        pred_col="predicate", obj_col="object") -> list:
        """Process csv file to generate cytoscape friendly format

        Args:
            df (pd.DataFrame): [description]
            subj_col (str, optional): [description]. Defaults to "subject".
            pred_col (str, optional): [description]. Defaults to "predicate".
            obj_col (str, optional): [description]. Defaults to "object".

        Returns:
            list: [description]
        """
        subj_lst = df[subj_col].values
        pred_lst = df[pred_col].values
        obj_lst = df[obj_col].values

        return self.cytoscape_kg_lst(subj_lst=subj_lst, pred_lst=pred_lst, obj_lst=obj_lst) 


    def cytoscape_kg_lst(subj_lst:list, pred_lst:list, obj_lst:list) -> list:
        """Returns list of dictionaries in a cytoscape friendly to generate knowledge graph.


        Args:
            subj_lst (list): list of subjects
            pred_lst (list): list of predicates
            obj_lst (list): list of objects

        Returns:
            list: list of items to generate a knowledge graph
        """

        elements = []

        for sub, pred, obj in zip(subj_lst, pred_lst, obj_lst):
            
            nodes = [
                {'data': {'id': sub, 'label': sub}},
                #{'data': {'id': pred, 'label': pred}},
                {'data': {'id': obj, 'label': obj}}
            ]

            relations = [
                {'data': {'source': sub, 'target': obj, 'label': pred}}
            ]

            elements += nodes
            elements += relations

        return elements
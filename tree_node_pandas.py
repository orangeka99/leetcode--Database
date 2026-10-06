import pandas as pd

def tree_node(tree: pd.DataFrame) -> pd.DataFrame:
    tree = tree.merge(tree,left_on='id',right_on='p_id',how='left')
    tree['new_stat'] = "Inner"
    tree.loc[(tree['id_y'].isna() & tree['p_id_y'].isna()), 'new_stat'] = "Leaf"
    tree.loc[(tree['p_id_x'].isna()), 'new_stat'] = "Root"
    tunique = tree.drop_duplicates(subset=['id_x', 'new_stat'])
    return pd.DataFrame({'id':tunique['id_x'],
                         'type':tunique['new_stat']})        
    
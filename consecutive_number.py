import pandas as pd

def consecutive_numbers(logs: pd.DataFrame) -> pd.DataFrame:
    block_id = logs['num'].ne(logs['num'].shift().fillna(1)).cumsum()
    num_mat = logs['num'][logs.groupby(block_id).cumcount() == 2].unique()
    return pd.DataFrame({'ConsecutiveNums':num_mat})

        

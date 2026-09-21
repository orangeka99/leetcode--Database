import pandas as pd

def consecutive_numbers(logs: pd.DataFrame) -> pd.DataFrame:
    block_id = logs['num'].ne(logs['num'].shift().fillna(1)).cumsum()
    logs['row_num'] = logs.groupby(block_id).cumcount() + 1
    logs = logs[logs['row_num'] == 3]
    logs = logs.drop_duplicates(subset=['num', 'row_num'])
    return pd.DataFrame({'ConsecutiveNums':logs['num']})
    # return pd.DataFrame([])
        

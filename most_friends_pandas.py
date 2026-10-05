import pandas as pd

def most_friends(request_accepted: pd.DataFrame) -> pd.DataFrame:
    result = pd.concat([request_accepted['requester_id'], request_accepted['accepter_id']], ignore_index=True).to_frame(name='ids')
    result['re_c'] = result.groupby('ids')['ids'].transform('count')
    max_ret = result.loc[result['re_c'].idxmax()]
    return pd.DataFrame({'id':[max_ret['ids']],
                         'num':[max_ret['re_c']]})
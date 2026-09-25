import pandas as pd

def trips_and_users(trips: pd.DataFrame, users: pd.DataFrame) -> pd.DataFrame:
    trips = trips.sort_values(by=['request_at','status'], ascending=True)
    merge = (
        trips.merge(users, left_on='client_id', right_on='users_id', suffixes=('_t1','_t2'))
             .merge(users, left_on='driver_id', right_on='users_id', suffixes=('_t4','_t3'))
             .query("banned_t4 == 'No' and banned_t3 == 'No' and '2013-10-01' <= request_at <= '2013-10-03'")
             [['id','status','request_at']]
            )
    merge['cancel'] = merge.groupby(['request_at','status'])['status'].transform('count')
    merge['total'] = merge.groupby('request_at')['request_at'].transform('count')
    merge['first_row'] = merge.groupby('request_at').cumcount() + 1
    merge['summ'] = merge['cancel'] / merge['total']
    merge = merge.query("first_row == 1")
    merge['count_row'] = len(merge)
    merge['new_sat'] = merge['summ']
    merge.loc[(merge['summ'] == 1),'new_sat'] = 0
    merge.loc[(merge['count_row'] == 1) & (merge['status'] != 'completed') & (merge['summ'] == 1),'new_sat'] = 1
    merge.loc[(merge['count_row'] == 1) & (merge['status'] == 'completed') & (merge['summ'] == 1),'new_sat'] = 0
    merge['new_sat'] = merge['new_sat'].round(2)
    return pd.DataFrame({'Day':merge['request_at'],
                         'Cancellation Rate': merge['new_sat']})
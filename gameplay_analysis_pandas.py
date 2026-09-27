import pandas as pd

def gameplay_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    activity = activity.sort_values(by=['player_id','event_date'], ascending=True)
    activity['check_rows'] = activity.groupby('player_id')['player_id'].cumcount() + 1
    total_players = activity['player_id'].nunique()
    tt = ((activity['player_id'] == activity['player_id'].shift(1)) & (activity['event_date'] == activity['event_date'].shift(1) + pd.Timedelta(days=1)))
    activity = activity[tt]
    activity = activity.query('check_rows == 2')
    fraction =  round(len(activity) / total_players,2)
    return pd.DataFrame({'fraction':[fraction]})


# For ai fix performance lesser Runtime but mem better
# def gameplay_analysis(activity: pd.DataFrame) -> pd.DataFrame:
#     activity['first_date'] = activity.groupby('player_id')['event_date'].transform('min')
#     logged_day_2 = activity[activity['event_date'] == activity['first_date'] + pd.Timedelta(days=1)]
#     total_players = activity['player_id'].nunique()
#     fraction = round(logged_day_2['player_id'].nunique() / total_players, 2)
#     return pd.DataFrame({'fraction':[fraction]})
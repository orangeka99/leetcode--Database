import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    activity = activity.sort_values(by=['player_id','event_date'],ascending=True)
    activity['row_count'] =  activity.groupby('player_id').cumcount() + 1
    activity = activity.query('row_count == 1')
    return pd.DataFrame({'player_id':activity['player_id'],
                         'first_login': activity['event_date']})
import pandas as pd

def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    weather = weather.sort_values(by='recordDate')
    tt = ((weather['temperature'] > weather['temperature'].shift(1)) & (weather['recordDate'].shift(1) + pd.Timedelta(days=1) == weather['recordDate']))
    weather = weather[tt]
    return pd.DataFrame({'id':weather['id']})
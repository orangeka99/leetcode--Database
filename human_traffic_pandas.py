import pandas as pd

def human_traffic(stadium: pd.DataFrame) -> pd.DataFrame:
    stadium['ch1'] = ((stadium['people'] >= 100) & (stadium['people'].shift(-2) >= 100) & (stadium['people'].shift(-1) >= 100))
    stadium['ch2'] = ((stadium['people'] >= 100) & (stadium['people'].shift(2) >= 100) & (stadium['people'].shift(1) >= 100))
    stadium['ch3'] = ((stadium['people'] >= 100) & (stadium['people'].shift(-1) >= 100) & (stadium['people'].shift(1) >= 100))
    stadium = stadium[(stadium['ch1'] == True) | (stadium['ch2'] == True) | (stadium['ch3'] == True)]
    return pd.DataFrame({'id':stadium['id'],
                         'visit_date':stadium['visit_date'],
                         'people':stadium['people']})
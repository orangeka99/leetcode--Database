import pandas as pd

def find_investments(insurance: pd.DataFrame) -> pd.DataFrame:
    insurance['r1'] = insurance.groupby(['lat','lon'])['pid'].transform('count')
    insurance['r2'] = insurance.groupby('tiv_2015')['pid'].transform('count')
    insurance = insurance[(insurance['r1'] < 2) & (insurance['r2'] > 1)]
    t_sum = round(insurance['tiv_2016'].sum(axis=0),2)
    return pd.DataFrame({'tiv_2016': [t_sum]})
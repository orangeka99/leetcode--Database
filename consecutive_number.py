import pandas as pd

def consecutive_numbers(logs: pd.DataFrame) -> pd.DataFrame:
    s = logs['num']
    num_mat = (s == s.shift(1)) & (s == s.shift(2))
    return pd.DataFrame({'ConsecutiveNums': s[num_mat].unique()})
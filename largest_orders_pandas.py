import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    orders['r1'] = orders.groupby('customer_number')['customer_number'].transform('count')
    orders = orders.sort_values(by='r1', ascending=False)
    m1 = orders['customer_number'].iloc[0]
    return pd.DataFrame({'customer_number':[m1]})
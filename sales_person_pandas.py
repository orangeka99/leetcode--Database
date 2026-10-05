import pandas as pd

def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    merge = orders.merge(company,on='com_id', how='inner').query("name == 'RED'")
    result = sales_person[~sales_person['sales_id'].isin(merge['sales_id'])]
    return pd.DataFrame({'name':result['name']})

    
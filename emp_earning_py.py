import pandas as pd

def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    merge = pd.merge(employee, employee, left_on='managerId', right_on='id', how='left')
    result = merge[merge['salary_x'] > merge['salary_y']]
    return pd.DataFrame({'Employee':result['name_x']})
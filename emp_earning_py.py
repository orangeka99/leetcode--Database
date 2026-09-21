import pandas as pd

def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    left_emp = employee.sort_values('salary')
    right_emp = employee.sort_values('salary')
    merge = pd.merge(employee, employee, left_on='managerId', right_on='id', how='left')
    condition = (merge['salary_x'] > merge['salary_y'])
    result = merge[condition]
    # merge = pd.merge_asof(left_emp, right_emp, left_on='salary', right_on='salary', left_by='managerId', right_by='id', direction='forward',suffixes=('_left', '_right'))
    # print(result)
    return pd.DataFrame({'Employee':result['name_x']})
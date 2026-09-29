import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    employee['count_mana'] = employee.groupby('managerId')['managerId'].transform('count')
    employee = pd.merge(
                    employee, employee,
                    left_on='id',
                    right_on='managerId',
                    how='inner',    
                    suffixes=('_t1', '_t2')
                    ).query("count_mana_t2 > 4").filter(items=['id_t1','name_t1'])
    employee = employee[['id_t1','name_t1']].drop_duplicates()
    return pd.DataFrame({'name': employee['name_t1']})